from datetime import date, timedelta


def current_streak(days, today=None):
    """Count consecutive checked-in days ending today, or yesterday if today is not done yet."""
    # Design choice: today not being done yet does NOT break your streak until tonight.
    if today is None:
        today = date.today()
    checked = set(days)
    day = today
    if day.isoformat() not in checked:
        day = today - timedelta(days=1)
    streak = 0
    while day.isoformat() in checked:
        streak += 1
        day -= timedelta(days=1)
    return streak
