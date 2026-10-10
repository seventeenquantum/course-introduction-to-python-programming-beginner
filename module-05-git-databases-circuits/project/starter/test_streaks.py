from datetime import date

from streaks import current_streak

TODAY = date(2026, 9, 10)


def test_three_day_streak_including_today():
    days = ["2026-09-10", "2026-09-09", "2026-09-08", "2026-09-05"]
    assert current_streak(days, TODAY) == 3


def test_today_not_done_yet_keeps_streak():
    assert current_streak(["2026-09-09", "2026-09-08"], TODAY) == 2


def test_gap_resets_streak():
    assert current_streak(["2026-09-07"], TODAY) == 0


def test_no_checkins():
    assert current_streak([], TODAY) == 0
