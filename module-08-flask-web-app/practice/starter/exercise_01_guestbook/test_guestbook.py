import guestbook


def make_client(tmp_path, monkeypatch):
    monkeypatch.setattr(guestbook, "DB", str(tmp_path / "g.db"))
    return guestbook.app.test_client()


def test_empty_name_shows_error(tmp_path, monkeypatch):
    client = make_client(tmp_path, monkeypatch)
    r = client.post("/", data={"name": "", "message": "hi"})
    assert b"Name must be 1 to 30 characters." in r.data


def test_valid_entry_appears_newest_first(tmp_path, monkeypatch):
    client = make_client(tmp_path, monkeypatch)
    client.post("/", data={"name": "Ada", "message": "first"})
    client.post("/", data={"name": "Ben", "message": "second"})
    page = client.get("/").data.decode()
    assert page.index("second") < page.index("first")


def test_script_tags_are_escaped(tmp_path, monkeypatch):
    client = make_client(tmp_path, monkeypatch)
    client.post("/", data={"name": "Eve", "message": "<script>alert(1)</script>"})
    page = client.get("/").data.decode()
    assert "<script>alert(1)</script>" not in page
    assert "&lt;script&gt;" in page
