from pathlib import Path

from organiser import category_for, plan_moves


def test_category_for():
    assert category_for(Path("a.JPG")) == "Images"
    assert category_for(Path("b.pdf")) == "Documents"
    assert category_for(Path("c")) == "Other"


def test_plan_moves_does_not_move_anything(tmp_path):
    (tmp_path / "a.txt").write_text("x")
    moves = plan_moves(tmp_path)
    assert len(moves) == 1
    assert (tmp_path / "a.txt").exists()
    assert moves[0][1] == tmp_path / "Documents" / "a.txt"


def test_name_clash_gets_a_number(tmp_path):
    (tmp_path / "Documents").mkdir()
    (tmp_path / "Documents" / "a.txt").write_text("old")
    (tmp_path / "a.txt").write_text("new")
    moves = plan_moves(tmp_path)
    assert moves[0][1].name == "a (1).txt"
