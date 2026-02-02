import sys
from pathlib import Path

from project_inspector.cli import main


def test_cli_outputs_tree_and_class_details(tmp_path: Path, capsys) -> None:
    project_root = tmp_path / "MusicProject"
    project_root.mkdir()
    (project_root / "README.md").write_text("readme", encoding="utf-8")

    cs_file = project_root / "NotePlayer.cs"
    cs_file.write_text(
        """
namespace Music.Core
{
    public class NotePlayer
    {
        public void Play(string note) { }
    }
}
""".strip(),
        encoding="utf-8",
    )

    argv = [
        "project_inspector",
        str(project_root),
        "--tree",
        "--classes",
    ]
    original_argv = sys.argv
    sys.argv = argv
    try:
        main()
    finally:
        sys.argv = original_argv

    captured = capsys.readouterr().out
    assert "Project Tree" in captured
    assert "NotePlayer" in captured
    assert "**File:**" in captured
    assert "**Namespace:**" in captured
