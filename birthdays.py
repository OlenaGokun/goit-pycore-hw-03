from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users):
    today = date.today()
    upcoming_birthdays = []

    for user in users:
        # Конвертуємо рядок у дату, некоректні записи пропускаємо
        try:
            birthday = datetime.strptime(
                user["birthday"], "%Y.%m.%d"
            ).date()
        except (ValueError, TypeError, KeyError):
            continue

        # Підставляємо поточний рік
        try:
            birthday_this_year = birthday.replace(year=today.year)
        except ValueError:
            # Цей виняток можливий тільки якщо ми намагаємося створити 
            # 29 лютого у невисокосному році. В такому випадку вітаємо 1 березня.
            birthday_this_year = date(today.year, 3, 1)

        # Якщо день народження вже минув, беремо наступний рік
        if birthday_this_year < today:
            try:
                birthday_this_year = birthday.replace(year=today.year + 1)
            except ValueError:
                # 29 лютого у наступному невисокосному році
                birthday_this_year = date(today.year + 1, 3, 1)

        # Перевіряємо найближчі 7 днів, включаючи сьогодні
        if (birthday_this_year - today).days >= 7:
            continue

        # Переносимо привітання з вихідних на понеділок
        weekday = birthday_this_year.weekday()
        if weekday >= 5:
            birthday_this_year += timedelta(days=7 - weekday)

        # Додаємо користувача до результату
        upcoming_birthdays.append({
            "name": user["name"],
            "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
        })

    return upcoming_birthdays
