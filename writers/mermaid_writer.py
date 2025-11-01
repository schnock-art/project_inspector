class MermaidWriter:
    def render(self, classes):
        lines = ["```mermaid", "classDiagram"]

        for cls in classes:
            for base in cls.inherits:
                lines.append(f"{base} <|-- {cls.name}")  # inheritance

            for dep in cls.uses:
                # Skip primitives & system types
                if dep in {"int", "float", "double", "string", "bool", "void"}:
                    continue
                lines.append(f"{cls.name} ..> {dep}")  # usage

        lines.append("```")
        return "\n".join(lines)
