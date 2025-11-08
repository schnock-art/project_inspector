import re
from pathlib import Path
from typing import List
from .models import ClassModel, MethodModel


class CSharpParser:
    """
    Fast C# doc + dependency parser (Unity-friendly)
    """

    # Regex for class definitions
    CLASS_RE = re.compile(
        r"(?:\/\/\/\s*<summary>\s*(?P<class_summary>.*?)\s*<\/summary>\s*)?"
        r"(?:\[.*?\]\s*)*"
        r"(?:public|internal|private|protected)?\s*"
        r"(class|interface)\s+(?P<name>\w+)"
        r"(?:\s*:\s*(?P<inherits>[\w,\s]+))?",
        re.DOTALL
    )

    # Regex for methods
    METHOD_RE = re.compile(
        r"(?:\/\/\/\s*<summary>\s*(?P<summary>.*?)\s*<\/summary>\s*)?"
        r"(?:\[.*?\]\s*)*"
        r"(?:public|private|protected|internal|static)+\s+(readonly\s+)?"
        r"(?P<return>\w+(<\w+(,\s+\w+)?>)?)\s+"
        r"(?P<name>\w+)\s*"
        r"\((?P<params>[^)]*)\)",
        re.DOTALL
    )

    FIELD_RE = re.compile(
        r"(?:public|private|protected|internal|static)+\s+(readonly\s+)?"
        r"(?P<type>\w+(<\w+(,\s+\w+)?>)?)\s+"
        r"(?P<name>\w+)"
        r"(?:\s*=\s*[^;]+)?;",
        re.MULTILINE
    )

    PARAM_RE = re.compile(r"(?P<type>[\w<>?]+)\s+(?P<name>\w+)")

    # 🚫 Noise filter
    CS_KEYWORDS = {
        "var","return","yield","else","if","for","foreach","while","switch","case",
        "new","private","public","protected","internal","static","readonly","partial",
        "true","false","null","class","interface","struct","enum","void",
        "get","set","value","in","out","ref","using","params","override"
    }
    UNITY_EDITOR_WORDS = {
        "GUILayout","EditorGUILayout","GUILayoutOption","Editor","target","GUILayoutOption[]"
    }
    BUILTINS = {
        "int","float","double","string","bool","char","object","decimal","byte",
        "long","short","uint","ulong","ushort","float?","int?","void"
    }
    UNITY_ATTRIBUTES = {"Tooltip","Header","Range","Space","SerializeField", "HideInInspector"}

    COLLECTION_TYPES = {"List", "Dictionary", "HashSet", "Queue", "Stack", "IReadOnlyCollection"}

    IGNORE_TYPES = CS_KEYWORDS | UNITY_EDITOR_WORDS | \
                 BUILTINS | UNITY_ATTRIBUTES | COLLECTION_TYPES

    def _filter_type(self, t: str) -> List[str]:
        """
        Extract meaningful type names (handles generics like List<Note>)
        """
        # Remove symbols
        t = re.sub(r"[^\w<>]", "", t)

        # Extract classes inside generics: List<Chord> → Chord
        parts = re.findall(r"[A-Z]\w+", t)

        # Add raw if it looks like a type
        if re.match(r"[A-Z]\w+", t):
            parts.append(t)

        return [p for p in parts if p not in self.IGNORE_TYPES]

    @staticmethod
    def extract_comment_above(code: str, pattern: str):
        idx = code.find(pattern)
        if idx == -1:
            return None

        lines = code[:idx].splitlines()
        xml_lines = []

        for line in reversed(lines):
            s = line.strip()
            if not s.startswith("///"):
                if xml_lines:
                    break
                continue
            xml_lines.append(s.lstrip("/ ").strip())

        xml_lines.reverse()
        if not xml_lines:
            return None

        return " ".join(xml_lines).strip()
    
    def process_class(self, c, text, path):
        class_name = c.group("name")
        inherits = c.group("inherits")
        class_summary = c.group("class_summary") or ""

        if not class_summary:
            class_summary = self.extract_comment_above(text, f"class {class_name}") or ""

        model = ClassModel(
            name=class_name,
            summary=class_summary.strip(),
            namespace=self._find_namespace(text),
            inherits=[i.strip() for i in inherits.split(",")] if inherits else [],
            filename=str(path)
        )

        class_block = self._extract_class_block(text, class_name)

        class_block_clean = re.sub(
            r"=\s*new\s+[A-Za-z_]\w*\s*\([^;]*?\);",
            "= new(/*...*/);",
            class_block
        )

        # ✅ Fields
        for f in self.FIELD_RE.finditer(class_block_clean):
            f_type = f.group("type")
            model.fields.append({"name": f.group("name"), "type": f_type})
            for t in self._filter_type(f_type):
                model.uses.add(t)

        # ✅ Methods
        for m in self.METHOD_RE.finditer(class_block_clean):
            raw_params = m.group("params").strip()
            params = [
                (p.group("type"), p.group("name"))
                for p in self.PARAM_RE.finditer(raw_params)
            ] if raw_params else []

            method_name = m.group("name")
            is_constructor = (method_name == class_name)
            return_type = None if is_constructor else m.group("return")

            method_summary = m.group("summary") or ""
            if not method_summary:
                method_summary = self.extract_comment_above(class_block, method_name) or ""

            model.methods.append(MethodModel(
                name=method_name,
                return_type=return_type,
                params=params,
                summary=method_summary,
                is_constructor=is_constructor
            ))

            if return_type:
                for t in self._filter_type(return_type):
                    model.uses.add(t)

            for p_type, _ in params:
                for t in self._filter_type(p_type):
                    model.uses.add(t)

        # Base classes
        for base in model.inherits:
            for t in self._filter_type(base):
                model.uses.add(t)

        model.uses.discard(model.name)

        model.uses = {u for u in model.uses if u not in self.IGNORE_TYPES}
        print(model.uses)
        return model

    # -------------------- PARSER CORE --------------------
    def parse_file(self, path: Path) -> List[ClassModel]:
        raw = path.read_text(encoding="utf-8")

        # Strip inspector attributes & non-XML comments
        text = self._clean_text(raw)
        classes = []

        for c in self.CLASS_RE.finditer(text):
            classes.append(
                self.process_class(c=c,text=text,path=path)
            )
        return classes

    # -------------------- UTILS --------------------
    @staticmethod
    def _find_namespace(text: str):
        m = re.search(r"namespace\s+([\w\.]+)", text)
        return m.group(1) if m else None

    @staticmethod
    def _extract_class_block(text: str, class_name: str) -> str:
        start = text.find(f"class {class_name}")
        if start == -1:
            start = text.find(f"interface {class_name}")
        if start == -1:
            return ""

        brace = text.find("{", start)
        depth = 0
        for i in range(brace, len(text)):
            if text[i] == "{": depth += 1
            elif text[i] == "}": depth -= 1
            if depth == 0:
                return text[start:i+1]
        return text[start:]

    def _clean_text(self, text: str) -> str:
        # Remove Unity inspector attributes
        text = re.sub(r"\[(Tooltip|Header|Range|Space|SerializeField|HideInInspector)[^\]]*\]", "", text)

        # Remove block comments
        text = re.sub(r"/\*[\s\S]*?\*/", "", text)

        # Remove // comments but keep ///
        text = re.sub(r"(^|[^:])//(?!/)(?!/).*", r"\1", text)

        # Remove inline "throw new Whatever(...);" to avoid confusing parser
        text = re.sub(r"throw\s+new\s+\w+\([^)]*\);?", "", text)

        # Optional: normalize whitespace (Prevents weird matching issues)
        # text = re.sub(r"\s{2,}", " ", text)

        return text
