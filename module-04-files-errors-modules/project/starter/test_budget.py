from budget import summarise


def test_summarise_one_month():
    data = [
        {"date": "2026-09-01", "type": "income", "category": "salary", "amount": 1000.0},
        {"date": "2026-09-05", "type": "expense", "category": "food", "amount": 200.0},
        {"date": "2026-09-09", "type": "expense", "category": "food", "amount": 50.0},
        {"date": "2026-10-01", "type": "expense", "category": "rent", "amount": 500.0},
    ]
    result = summarise(data, "2026-09")
    assert result["income"] == 1000.0
    assert result["expenses"] == 250.0
    assert result["net"] == 750.0
    assert result["by_category"] == {"food": 250.0}
