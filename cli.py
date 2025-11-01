#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

from writers.md_writer import MarkdownWriter
from writers.txt_writer import TextWriter
from writers.html_writer import HTMLWriter

from analyzers.folder_tree import FolderTreeAnalyzer
from analyzers.cs_parser import CSharpParser

def main():
    parser = argparse.ArgumentParser(
        prog="musicdoc",
        description="Generate documentation for a Unity C# music system."
    )

    parser.add_argument("project_path", help="Path to Unity project root or Assets folder")

    parser.add_argument("--tree", action="store_true", help="Print project folder tree")
    parser.add_argument("--classes", action="store_true", help="List classes")
    parser.add_argument("--methods", action="store_true", help="List methods")
    parser.add_argument("--summaries", action="store_true", help="Extract XML doc summaries")

    parser.add_argument("--output", "-o", type=str, help="Write to file instead of stdout")
    parser.add_argument("--format", "-f", default="md", choices=["md", "txt", "html"],
                        help="Output format (default: md)")

    args = parser.parse_args()

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

    if args.classes:
        parser = CSharpParser()
        for file in project_path.rglob("*.cs"):
            models = parser.parse_file(file)
            for cls in models:
                content += f"\n### {cls.name}: \n"
                if cls.summary and args.summaries:
                    content += f"> {cls.summary}\n\n"
                content += f"**File:** `{cls.filename}`\n\n"
                if cls.inherits:
                    content += f"**Inherits:** {', '.join(cls.inherits)}\n\n"
                
                if args.methods:
                    content += "**Methods:**\n"
                    for m in cls.methods:
                        params = ", ".join(f"{t} {n}" for t, n in m.params)
                        content += f"- `{m.return_type} {m.name}({params})`\n"
                        if m.summary and args.summaries:
                            content += f"  - *{m.summary}*\n"


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
