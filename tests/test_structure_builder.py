from pathlib import Path

from project_inspector.structure_builder import TreeStructureBuilder


def test_builds_tree_structure(tmp_path: Path) -> None:
    tree_content = """
SampleProject
├── Assets/
│   └── Scripts/
│       └── MusicPlayer.cs
└── README.md
""".strip()

    tree_file = tmp_path / "tree.md"
    tree_file.write_text(tree_content, encoding="utf-8")

    target_root = tmp_path / "output"
    builder = TreeStructureBuilder(tree_file, target_root)

    root_path, created = builder.build()

    expected_root = target_root / "SampleProject"
    assert root_path == expected_root
    assert expected_root.is_dir()

    expected_paths = [
        expected_root / "Assets",
        expected_root / "Assets" / "Scripts",
        expected_root / "Assets" / "Scripts" / "MusicPlayer.cs",
        expected_root / "README.md",
    ]
    for path in expected_paths:
        assert path.exists()

    created_set = {path for path in created}
    for path in expected_paths:
        assert path in created_set
