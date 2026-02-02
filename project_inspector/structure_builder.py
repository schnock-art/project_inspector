from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple


TREE_LINE_RE = re.compile(
    r"^(?P<prefix>(?:\│   |    )*)(?P<branch>├── |└── )?(?P<name>.+)$"
)

KNOWN_FILES = {
    "LICENSE",
    "LICENSE.md",
    "LICENSE.txt",
    "README",
    "README.md",
    "README.txt",
    "Makefile",
    "Dockerfile",
    ".gitignore",
    ".gitattributes",
    ".gitmodules",
    ".env",
    ".dockerignore",
    ".editorconfig",
}


@dataclass(frozen=True)
class TreeEntry:
    depth: int
    name: str
    has_branch: bool


class TreeStructureBuilder:
    def __init__(self, tree_file: Path, target_root: Path):
        self.tree_file = tree_file
        self.target_root = target_root

    def parse_entries(self) -> List[TreeEntry]:
        if not self.tree_file.exists():
            raise FileNotFoundError(f"Tree file not found: {self.tree_file}")

        lines = self.tree_file.read_text(encoding="utf-8").splitlines()
        entries: List[TreeEntry] = []

        for raw in lines:
            line = raw.rstrip()
            if not line.strip():
                continue
            stripped = line.strip()
            if stripped.startswith(("```", "#", ">")):
                continue
            if stripped.startswith("📂"):
                continue

            match = TREE_LINE_RE.match(line)
            if not match:
                continue
            name = match.group("name").strip()
            if not name:
                continue
            prefix = match.group("prefix") or ""
            branch = match.group("branch")
            depth = len(prefix) // 4
            entries.append(TreeEntry(depth=depth, name=name, has_branch=branch is not None))

        return entries

    def build(self) -> Tuple[Path, List[Path]]:
        entries = self.parse_entries()
        if not entries:
            raise ValueError("No tree entries found to build.")

        first = entries[0]
        has_root = first.depth == 0 and not first.has_branch
        created: List[Path] = []

        if has_root:
            root_is_dir = self._is_directory(first.name, entries, 0)
            root_name = self._clean_name(first.name)
            root_path = self.target_root / root_name
            if root_is_dir:
                root_path.mkdir(parents=True, exist_ok=True)
            else:
                root_path.parent.mkdir(parents=True, exist_ok=True)
                root_path.touch(exist_ok=True)
            created.append(root_path)
            entries = entries[1:]
        else:
            root_path = self.target_root

        paths_by_depth = {-1: root_path}
        for idx, entry in enumerate(entries):
            raw_name = entry.name
            name = self._clean_name(raw_name)
            depth = entry.depth
            parent = paths_by_depth.get(depth - 1, root_path)
            current_path = parent / name

            is_dir = self._is_directory(raw_name, entries, idx)
            if is_dir:
                current_path.mkdir(parents=True, exist_ok=True)
                paths_by_depth[depth] = current_path
            else:
                current_path.parent.mkdir(parents=True, exist_ok=True)
                current_path.touch(exist_ok=True)
            created.append(current_path)

        return root_path, created

    def _clean_name(self, name: str) -> str:
        return name.rstrip("/").strip()

    def _is_directory(self, name: str, entries: List[TreeEntry], index: int) -> bool:
        if name.endswith("/"):
            return True
        if index < len(entries) - 1:
            next_entry = entries[index + 1]
            if next_entry.depth > entries[index].depth:
                return True
        path_name = Path(name).name
        if path_name in KNOWN_FILES:
            return False
        if Path(path_name).suffix:
            return False
        return True
