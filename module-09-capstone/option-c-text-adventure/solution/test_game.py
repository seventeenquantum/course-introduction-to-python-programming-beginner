from game import (
    describe,
    go,
    load_game,
    new_player,
    new_world,
    parse_command,
    save_game,
    take,
)


def test_parse_command():
    assert parse_command("GO North") == ("go", "north")
    assert parse_command("   ") == ("", "")
    assert parse_command("take old key") == ("take", "old key")


def test_valid_exit_changes_room():
    world, player = new_world(), new_player()
    go(world, player, "north")
    assert player["room"] == "library"


def test_wall_does_not_move_player():
    world, player = new_world(), new_player()
    assert "can't go" in go(world, player, "west")
    assert player["room"] == "hall"


def test_vault_is_locked_without_key():
    world, player = new_world(), new_player()
    go(world, player, "north")
    assert "locked" in go(world, player, "east")
    assert player["room"] == "library"


def test_take_moves_item_to_inventory_and_vault_opens():
    world, player = new_world(), new_player()
    take(world, player, "key")
    assert "key" in player["inventory"]
    assert "key" not in world["hall"]["items"]
    go(world, player, "north")
    go(world, player, "east")
    assert player["room"] == "vault"
    assert "win" in take(world, player, "treasure")


def test_save_and_load_roundtrip(tmp_path):
    world, player = new_world(), new_player()
    take(world, player, "key")
    path = tmp_path / "save.json"
    save_game(path, world, player)
    loaded_world, loaded_player = load_game(path)
    assert loaded_player["inventory"] == ["key"]
    assert loaded_world["hall"]["items"] == []


def test_load_missing_or_damaged_file(tmp_path):
    assert load_game(tmp_path / "nope.json") is None
    bad = tmp_path / "bad.json"
    bad.write_text("{broken")
    assert load_game(bad) is None


def test_describe_lists_items_and_exits():
    text = describe(new_world(), new_player())
    assert "key" in text and "north" in text
