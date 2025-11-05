
import re
class MermaidWriter:  
    def render(self, classes):
        lines = ["```mermaid", "classDiagram"]
        
        def clean_type(name: str) -> str:
            return re.sub(r"<.*?>", "", name)   # remove <T>
        
        for cls in classes:
            for base in cls.inherits:
                lines.append(f"{base} <|-- {cls.name}")  # inheritance

            for dep in cls.uses:
                dep = clean_type(dep)
                # Skip primitives & system types
                if dep in {"int", "float", "double", "string", "bool", "void", "List"}:
                    continue
                cls_name = clean_type(cls.name)
                lines.append(f"{cls_name} ..> {dep}")  # usage

        lines.append("```")
        return "\n".join(lines)
