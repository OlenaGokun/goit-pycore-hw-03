from random import sample

def get_numbers_ticket(min: int, max: int, quantity: int):
    if min < 1 or max > 1000 or max < min:
        print(f"Помилка диапазону: від {min} до {max}")
        return []

    if quantity > (max - min):
        print(f"В дипазоні від {min} до {max} немає {quantity} чисел")
        return []

    if quantity < 1:
        print(f"Кількість чисел {quantity} менша за одиницю")
        return []

    return sorted(sample(range(min, max + 1), quantity))