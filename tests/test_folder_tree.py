from pathlib import Path

from project_inspector.analyzers.folder_tree import FolderTreeAnalyzer


def test_folder_tree_generation(tmp_path: Path) -> None:
    project_root = tmp_path / "MyProject"
    assets = project_root / "Assets"
    assets.mkdir(parents=True)
    (assets / "foo.cs").write_text("// test", encoding="utf-8")
    (project_root / "README.md").write_text("readme", encoding="utf-8")

    analyzer = FolderTreeAnalyzer(project_root)
    output = analyzer.generate()

    assert "📂 **Project Tree: MyProject**" in output
    assert "MyProject" in output
    assert "├── Assets" in output
    assert "└── README.md" in output
    assert "└── foo.cs" in output
