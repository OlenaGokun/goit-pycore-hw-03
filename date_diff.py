from datetime import datetime

def get_days_from_today(date: str):
    try:
        dateVal = datetime.fromisoformat(date)
    except (ValueError):
        print(f"Wrong date format in string {date}")
        return None
    else:
        delta = datetime.today() - dateVal
        return delta.days
