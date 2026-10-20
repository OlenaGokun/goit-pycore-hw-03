from random import sample

def get_numbers_ticket(min: int, max: int, quantity: int):
    if min < 1 or max > 1000 or max < min:
        print(f"Помилка диапазону: від {min} до {max}")
        return []

    if quantity > (max - min + 1):
        print(f"В дипазоні від {min} до {max} немає {quantity} чисел")
        return []

    if quantity < 1:
        print(f"Кількість чисел {quantity} менша за одиницю")
        return []

    return sorted(sample(range(min, max + 1), quantity))


# #####   Тести   #####

# def test_ticket(min_val, max_val, quantity, description, is_valid=True):
#     result = get_numbers_ticket(min_val, max_val, quantity)

#     if is_valid:
#         passed = (
#             len(result) == quantity
#             and len(set(result)) == quantity
#             and result == sorted(result)
#             and all(min_val <= num <= max_val for num in result)
#         )
#         expected = f"{quantity} unique sorted numbers in [{min_val}, {max_val}]"
#     else:
#         passed = result == []
#         expected = []

#     print(f"{description} | expected output: {expected}, actual output: {result}, {'PASS' if passed else 'FAIL'}")


# # Звичайні випадки
# test_ticket(1, 49, 6, "Standard lottery")
# test_ticket(1, 100, 10, "Larger range")
# test_ticket(10, 20, 5, "Small range")
# test_ticket(1, 1000, 100, "Large quantity")

# # Граничні випадки
# test_ticket(1, 1, 1, "Single number")
# test_ticket(1000, 1000, 1, "Maximum allowed number")
# test_ticket(1, 1000, 1000, "Full allowed range")
# test_ticket(1, 10, 10, "Quantity equals range size")
# test_ticket(1, 1000, 1, "Minimum quantity")
# test_ticket(999, 1000, 2, "Upper boundary")

# # Некоректні діапазони
# test_ticket(0, 49, 6, "Minimum below 1", False)
# test_ticket(-10, 49, 6, "Negative minimum", False)
# test_ticket(1, 1001, 6, "Maximum above 1000", False)
# test_ticket(1, 10000, 6, "Maximum far above 1000", False)
# test_ticket(50, 10, 6, "Maximum less than minimum", False)
# test_ticket(1000, 999, 1, "Reversed boundary", False)

# # Некоректна кількість
# test_ticket(1, 49, 0, "Zero quantity", False)
# test_ticket(1, 49, -1, "Negative quantity", False)
# test_ticket(1, 49, -100, "Large negative quantity", False)
# test_ticket(1, 49, 50, "Quantity exceeds range", False)
# test_ticket(1, 1, 2, "Quantity exceeds single-number range", False)
# test_ticket(1, 1000, 1001, "Quantity exceeds maximum range", False)

# # Комбінації некоректних параметрів
# test_ticket(0, 1001, 1002, "All parameters out of bounds", False)
# test_ticket(50, 10, 0, "Invalid range and zero quantity", False)
# test_ticket(-5, -1, 3, "Entirely negative range", False)
# test_ticket(1001, 1002, 1, "Entirely above maximum range", False)