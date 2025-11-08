
import re
class MermaidWriter:  
    def render(self, classes):
        lines = ["```mermaid", "classDiagram"]
        if len(classes)==0:
            return ""
        def clean_type(name: str) -> str:
            return re.sub(r"<.*?>", "", name)   # remove <T>
        
        edges = []
        for cls in classes:
            for base in cls.inherits:
                edges.append(f"{base} <|-- {cls.name}")

            for dep in cls.uses:
                dep = clean_type(dep)
                # Skip primitives & system types
                if dep in {"int", "float", "double", "string", "bool", "void", "List", "IReadOnlyCollection"}:
                    continue
                cls_name = clean_type(cls.name)
                edges.append(f"{cls_name} ..> {dep}")

        # 🧹 If no edges at all, don't output diagram
        if not edges:
            return "\n"

        lines.extend(edges)
        lines.append("```")
        return "\n".join(lines)
