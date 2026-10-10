from app import app


def post(value, from_unit, to_unit):
    return app.test_client().post(
        "/", data={"value": value, "from_unit": from_unit, "to_unit": to_unit}
    ).data.decode()


def test_valid_conversion():
    assert "10 km = 6.21 miles" in post("10", "km", "miles")


def test_bad_number():
    assert "Please enter a number." in post("abc", "km", "miles")


def test_incompatible_units():
    assert "Cannot convert km to kg." in post("5", "km", "kg")
