from datetime import datetime

def get_days_from_today(date: str):
    try:
        dateVal = datetime.fromisoformat(date).date()
    except (ValueError):
        print(f"Wrong date format in string {date}")
        return None
    else:
        delta = datetime.today().date() - dateVal
        return delta.days



#####   Тести   #####

# from datetime import timedelta, date
# today = date.today()

# # Звичайні дати
# print(f"Past date | expected output: {(today - date(2024, 1, 1)).days}, actual output: {get_days_from_today('2024-01-01')}")
# print(f"Future date | expected output: {(today - date(2030, 12, 31)).days}, actual output: {get_days_from_today('2030-12-31')}")
# print(f"Today | expected output: 0, actual output: {get_days_from_today(today.isoformat())}")

# # Граничні випадки
# print(f"Yesterday | expected output: 1, actual output: {get_days_from_today((today - timedelta(days=1)).isoformat())}")
# print(f"Tomorrow | expected output: -1, actual output: {get_days_from_today((today + timedelta(days=1)).isoformat())}")
# print(f"First supported date | expected output: {(today - date.min).days}, actual output: {get_days_from_today('0001-01-01')}")
# print(f"Last supported date | expected output: {(today - date.max).days}, actual output: {get_days_from_today('9999-12-31')}")

# # Високосні роки
# print(f"Leap year (valid) | expected output: {(today - date(2024, 2, 29)).days}, actual output: {get_days_from_today('2024-02-29')}")
# print(f"Leap year (invalid) | expected output: None, actual output: {get_days_from_today('2025-02-29')}")
# print(f"Century leap year (valid) | expected output: {(today - date(2000, 2, 29)).days}, actual output: {get_days_from_today('2000-02-29')}")
# print(f"Century leap year (invalid) | expected output: None, actual output: {get_days_from_today('1900-02-29')}")

# # Некоректні дати
# print(f"Invalid month | expected output: None, actual output: {get_days_from_today('2025-13-01')}")
# print(f"Invalid day | expected output: None, actual output: {get_days_from_today('2025-04-31')}")
# print(f"Day zero | expected output: None, actual output: {get_days_from_today('2025-01-00')}")
# print(f"Month zero | expected output: None, actual output: {get_days_from_today('2025-00-15')}")

# # Некоректні формати
# print(f"Empty string | expected output: None, actual output: {get_days_from_today('')}")
# print(f"Random text | expected output: None, actual output: {get_days_from_today('hello')}")
# print(f"European format | expected output: None, actual output: {get_days_from_today('20.10.2026')}")
# print(f"Slash separator | expected output: None, actual output: {get_days_from_today('2026/10/20')}")
# print(f"Extra characters | expected output: None, actual output: {get_days_from_today('2026-10-20abc')}")