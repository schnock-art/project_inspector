#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

from project_inspector.writers.md_writer import MarkdownWriter
from project_inspector.writers.txt_writer import TextWriter
from project_inspector.writers.html_writer import HTMLWriter
from project_inspector.writers.mermaid_writer import MermaidWriter


from project_inspector.analyzers.folder_tree import FolderTreeAnalyzer
from project_inspector.analyzers.cs_parser import CSharpParser
from project_inspector.structure_builder import TreeStructureBuilder


def main():
    parser = argparse.ArgumentParser(
        prog="musicdoc",
        description="Generate documentation for a Unity C# music system."
    )

    parser.add_argument(
        "project_path",
        nargs="?",
        help="Path to Unity project root or Assets folder",
    )

    parser.add_argument("--tree", action="store_true", help="Print project folder tree")
    parser.add_argument("--classes", action="store_true", help="List classes")
    parser.add_argument("--methods", action="store_true", help="List methods")
    parser.add_argument("--summaries", action="store_true", help="Extract XML doc summaries")
    parser.add_argument("--mermaid", action="store_true", help="Generate Mermaid class diagram")
    parser.add_argument("--version", action="version", version="project-inspector 0.1.0")
    parser.add_argument("--output", "-o", type=str, help="Write to file instead of stdout")
    parser.add_argument("--format", "-f", default="md", choices=["md", "txt", "html"],
                        help="Output format (default: md)")
    parser.add_argument(
        "--build-tree",
        type=str,
        help="Create folders/files from a folder_tree_structure.md file",
    )
    parser.add_argument(
        "--target",
        type=str,
        default=".",
        help="Target root for --build-tree (default: current directory)",
    )

    args = parser.parse_args()

    if args.build_tree:
        tree_file = Path(args.build_tree)
        target_root = Path(args.target)
        builder = TreeStructureBuilder(tree_file, target_root)
        try:
            root_path, created = builder.build()
        except (FileNotFoundError, ValueError) as exc:
            print(f"❌ {exc}")
            sys.exit(1)
        print(f"✅ Created {len(created)} paths under {root_path}")
        if not (args.tree or args.classes or args.methods or args.summaries or args.mermaid):
            return

    if not args.project_path:
        print("❌ project_path is required unless --build-tree is used.")
        sys.exit(1)

    project_path = Path(args.project_path)
    if not project_path.exists():
        print(f"❌ Path not found: {project_path}")
        sys.exit(1)

    # placeholder: results will be collected from analyzers later
    content = "# ProjectDoc Output\n\n"
    content += f"Scanned folder: `{project_path}`\n\n"

    if args.tree:
        analyzer = FolderTreeAnalyzer(project_path)
        content += analyzer.generate()

    if args.mermaid:
        mermaid_writer = MermaidWriter()
        mermaid_content = ""
    all_classes = []  # ✅ collect everything once
    if args.classes or args.mermaid:
        cs_parser = CSharpParser()
        for file in project_path.rglob("*.cs"):
            models = cs_parser.parse_file(file)
            all_classes.extend(models)  # ✅ store globally

            for cls in models:
                content += f"\n### {cls.name}: \n"
                if cls.summary and args.summaries:
                    content += f"> {cls.summary}\n\n"
                content += f"**File:** `{cls.filename}`\n\n"
                content += f"**Namespace:** `{cls.namespace}`\n\n"

                if cls.inherits:
                    content += f"**Inherits:** {', '.join(cls.inherits)}\n\n"
                
                if args.methods:
                    content += "**Methods:**\n"
                    for m in cls.methods:
                        params = ", ".join(f"{t} {n}" for t, n in m.params)
                        if m.is_constructor:
                            content += f"- `[constructor] {m.return_type} {m.name}({params})`\n"
                        else:
                            content += f"- `{m.return_type} {m.name}({params})`\n"
                        if m.summary and args.summaries:
                            content += f"  - *{m.summary}*\n"

                if args.mermaid:
                    current_class_mermaid = mermaid_writer.render([cls]) + "\n\n"
                    mermaid_content += current_class_mermaid
                    content += current_class_mermaid

    # -------------------------------
    # 🌍 GLOBAL UML ARCHITECTURE DIAGRAM
    # -------------------------------
    if args.mermaid and all_classes:
        content += "\n## Global Architecture Diagram\n"
        content += "```mermaid\nclassDiagram\n"

        class_names = {cls.name for cls in all_classes}

        edges = set()

        for cls in all_classes:
            # inheritance edges
            for base in cls.inherits:
                if base in class_names:
                    edges.add(f"{base} <|-- {cls.name}")

            # usage edges
            for dep in cls.uses:
                if dep in class_names:
                    edges.add(f"{cls.name} --> {dep}")

        for e in sorted(edges):
            content += e + "\n"


    # Choose writer
    writer = {
        "md": MarkdownWriter,
        "txt": TextWriter,
        "html": HTMLWriter
    }[args.format]()

    output = writer.render(content)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"✅ Output written to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
