"""
Домашнее задание №1
Функции и структуры данных
"""
def power_numbers(numbers):
    sq = []

    for n in numbers:
        power = n ** 2
        sq.append(power)

    return sq

print(power_numbers(numbers = [1,2,3,5]))



# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i ** 2 <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 6
    return True

def filter_numbers(numbers, filter_type):
    filtered_numbers = []
    if filter_type == ODD:
        filtered_numbers = [num for num in numbers if num % 2 != 0]
    elif filter_type == EVEN:
        filtered_numbers = [num for num in numbers if num % 2 == 0]
    elif filter_type == PRIME:
        filtered_numbers = [num for num in numbers if prime(num)]
    return filtered_numbers

print(filter_numbers([1, 2, 3], ODD))
print(filter_numbers([2, 3, 4, 5], EVEN))
print(filter_numbers([2, 3, 4], PRIME))
