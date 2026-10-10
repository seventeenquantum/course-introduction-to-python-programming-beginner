import app as app_module
import db


def make_client(tmp_path, monkeypatch):
    path = str(tmp_path / "test.db")

    def fake_connect():
        return db.connect(path)

    monkeypatch.setattr(app_module, "connect", fake_connect)
    return app_module.app.test_client()


def test_add_and_duplicate(tmp_path, monkeypatch):
    client = make_client(tmp_path, monkeypatch)
    r = client.post("/add", data={"name": "read"}, follow_redirects=True)
    assert b"Added read." in r.data
    r = client.post("/add", data={"name": "read"}, follow_redirects=True)
    assert b"already exists" in r.data


def test_checkin_flow(tmp_path, monkeypatch):
    client = make_client(tmp_path, monkeypatch)
    client.post("/add", data={"name": "read"})
    r = client.get("/")
    assert b"0 day streak" in r.data
    r = client.post("/checkin/1", follow_redirects=True)
    assert b"Checked in" in r.data
    assert b"1 day streak" in r.data
    assert b"(done today)" in r.data
    r = client.post("/checkin/1", follow_redirects=True)
    assert b"already checked in" in r.data


def test_unknown_habit_is_404(tmp_path, monkeypatch):
    client = make_client(tmp_path, monkeypatch)
    assert client.post("/checkin/99").status_code == 404
