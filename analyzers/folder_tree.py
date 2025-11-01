from pathlib import Path

INDENT = "│   "
LAST_INDENT = "└── "
MID_INDENT = "├── "

class FolderTreeAnalyzer:
    def __init__(self, root: Path, ignore=None, max_depth=20):
        self.root = root
        self.ignore = ignore or ["Library", "Temp", "Logs", "obj", ".git", ".vs", ".idea"]
        self.max_depth = max_depth

    def _is_ignored(self, path: Path):
        return any(part in self.ignore for part in path.parts)

    def _tree(self, path: Path, depth=0):
        if depth > self.max_depth:
            return ""

        entries = [e for e in sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
                   if not self._is_ignored(e)]

        buf = ""

        for i, entry in enumerate(entries):
            connector = LAST_INDENT if i == len(entries) - 1 else MID_INDENT
            buf += f"{INDENT * depth}{connector}{entry.name}\n"

            if entry.is_dir():
                buf += self._tree(entry, depth + 1)
        return buf

    def generate(self):
        result = f"📂 **Project Tree: {self.root.name}**\n\n```\n"
        result += f"{self.root.name}\n"
        result += self._tree(self.root)
        result += "```\n"
        return result
