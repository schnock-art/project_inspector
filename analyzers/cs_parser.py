import re
from pathlib import Path
from typing import List
from .models import ClassModel, MethodModel


class CSharpParser:
    """
    A lightweight C# source parser for documentation extraction.
    Supports:
      ✅ class name + inheritance
      ✅ method signatures
      ✅ XML doc comments (/// <summary>)
      ❌ full C# grammar (not a compiler — fast & pragmatic)
    """

    # Regex for class definitions w/ optional XML <summary> above
    CLASS_RE = re.compile(
        r"(?:\/\/\/\s*<summary>\s*(?P<class_summary>.*?)\s*<\/summary>\s*)?"
        r"(?:\[.*?\]\s*)*"  # attributes
        r"(?:public|internal|private|protected)?\s*"
        r"(class|interface)\s+(?P<name>\w+)"
        r"(?:\s*:\s*(?P<inherits>[\w,\s]+))?",
        re.DOTALL
    )

    # Regex for method signatures w/ optional XML <summary> above
    METHOD_RE = re.compile(
        r"(?:\/\/\/\s*<summary>\s*(?P<summary>.*?)\s*<\/summary>\s*)?"
        r"(?:\[.*?\]\s*)*"  # attributes
        r"(?:public|private|internal|protected)?\s*"
        r"(?P<return>\w[\w<>?]*)\s+"
        r"(?P<name>\w+)\s*"
        r"\((?P<params>[^)]*)\)",
        re.DOTALL
    )

    FIELD_RE = re.compile(
        r"(?:public|private|protected|internal|static|\s)+"
        r"(?P<type>[\w<>\[\]?]+)\s+"
        r"(?P<name>\w+)"
        r"(?:\s*=\s*[^;]+)?;",
        re.MULTILINE
    )

    PARAM_RE = re.compile(r"(?P<type>[\w<>?]+)\s+(?P<name>\w+)")

    # ----------------------
    # COMMENT EXTRACTION
    # ----------------------
    @staticmethod
    def extract_comment_above(code: str, pattern: str):
        """
        Looks above a code pattern and extracts ONLY XML doc triple-slash comments.
        Avoids polluting summaries with inline // comments or banners.
        """
        idx = code.find(pattern)
        if idx == -1:
            return None

        lines = code[:idx].splitlines()
        xml_lines = []

        for line in reversed(lines):
            line = line.strip()

            # Stop once we hit non-XML-comment after collecting docs
            if not line.startswith("///"):
                if xml_lines:
                    break
                continue

            xml_lines.append(line.lstrip("/ ").strip())

        xml_lines.reverse()
        if not xml_lines:
            return None

        # Clean repeated dashes or banners if any slipped through
        text = " ".join(xml_lines)
        text = re.sub(r"[-=]{3,}", "", text).strip()
        return text or None

    # ----------------------
    # MAIN FILE PARSER
    # ----------------------
    def parse_file(self, path: Path) -> List[ClassModel]:
        raw = path.read_text(encoding="utf-8")

        # ✅ REMOVE noise comments before regex scanning
        text = self.strip_non_xml_comments(raw)
        classes = []

        for c in self.CLASS_RE.finditer(text):
            class_name = c.group("name")
            inherits = c.group("inherits")
            class_summary = c.group("class_summary") or ""

            # If summary missing — try raw XML extractor
            if not class_summary:
                class_summary = self.extract_comment_above(text, f"class {class_name}") or ""

            model = ClassModel(
                name=class_name,
                summary=class_summary.strip(),
                namespace=self._find_namespace(text),
                inherits=[i.strip() for i in inherits.split(",")] if inherits else [],
                filename=str(path)
            )

            # Extract methods inside this class block
            class_block = self._extract_class_block(text, class_name)
            # Inside parse_file, right after extracting class_block
            # Strip constructor-style field initializers like: = new KeyScale(...)
            class_block_clean = re.sub(
                r"=\s*new\s+[A-Za-z_]\w*\s*\([^;]*?\);",
                "= new(/*...*/);",
                class_block
            )
            for f in self.FIELD_RE.finditer(class_block_clean):
                model.fields.append({
                    "name": f.group("name"),
                    "type": f.group("type")
                })
            for m in self.METHOD_RE.finditer(class_block_clean):

                raw_params = m.group("params").strip()
                params = [
                    (p.group("type"), p.group("name"))
                    for p in self.PARAM_RE.finditer(raw_params)
                ] if raw_params else []

                is_constructor = (m.group("name") == class_name)
                if is_constructor:
                    return_type = None
                else:
                    return_type = m.group("return")

                method_summary = m.group("summary") or ""
                if not method_summary:
                    method_summary = self.extract_comment_above(class_block_clean, m.group("name")) or ""

                model.methods.append(MethodModel(
                    name=m.group("name"),
                    return_type=return_type,
                    params=params,
                    summary=method_summary,
                    is_constructor=is_constructor
                ))

            classes.append(model)

        return classes

    # ----------------------
    # HELPERS
    # ----------------------
    @staticmethod
    def _find_namespace(text: str) -> str:
        match = re.search(r"namespace\s+([\w\.]+)", text)
        return match.group(1) if match else None

    @staticmethod
    def _extract_class_block(text: str, class_name: str) -> str:
        """Return only the body of this class (brace-matched), excluding nested types."""

        # Find class or interface start
        start = text.find(f"class {class_name}")
        if start == -1:
            start = text.find(f"interface {class_name}")
        if start == -1:
            return ""

        # Find first {
        brace_start = text.find("{", start)
        if brace_start == -1:
            return ""

        depth = 0
        for i in range(brace_start, len(text)):
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    # End of this class block
                    return text[start:i+1]

        return text[start:]  # fallback (unbalanced braces)
    
    @staticmethod
    def strip_non_xml_comments(text: str) -> str:
        """
        Removes all non-XML comments:
        - // comments (unless they start with ///)
        - /* block comments */
        Keeps XML doc comments (///).
        """

        # Remove block comments /* ... */
        text = re.sub(r"/\*[\s\S]*?\*/", "", text)

        # Remove // comments but preserve /// XML comments
        text = re.sub(r"(^|[^/])//(?!/).*", r"\1", text)

        # Remove Exception
        #text = re.sub(r"throw\s+new\s+\w+\([^)]*\);?", "", text)

        return text
