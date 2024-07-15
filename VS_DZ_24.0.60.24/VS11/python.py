# Завдання 1

# try:
#     name = input("Введіть ім'я: ")
#     age = int(input("Введіть вік: "))

#     if age < 0 or age > 130:
#         raise ValueError("Некоректний вік!")

#     print(f"Привіт, {name}! Твій вік — {age}")

# except ValueError as e:
#     print(f"Помилка: {e}")

# Завдання 2

# def greet(name, age):
#     return f"Привіт, {name}! Твій вік — {age}"

# try:
#     name = input("Введіть ім'я: ")
#     age = int(input("Введіть вік: "))

#     if age < 0 or age > 130:
#         raise ValueError("Некоректний вік!")

#     print(greet(name, age))

# except ValueError as e:
#     print(f"Помилка: {e}")

# Завдання 3

# def get_positive_numbers():
#     numbers = []
#     while True:
#         num = int(input("Введіть додатне число (або 0 для завершення вводу): "))
#         if num == 0:
#             break
#         if num < 0:
#             raise ValueError("Від'ємне значення!")
#         numbers.append(num)
#     return numbers

# try:
#     numbers = get_positive_numbers()
#     total = sum(numbers)
#     print(f"Сума чисел: {total}")

# except ValueError as e:
#     print(f"Помилка: {e}")

# Завдання 4

# def sum_positive_numbers(numbers):
#     return sum(numbers)

# try:
#     numbers = []
#     while True:
#         num = int(input("Введіть додатне число (або 0 для завершення вводу): "))
#         if num == 0:
#             break
#         if num < 0:
#             raise ValueError("Від'ємне значення!")
#         numbers.append(num)

#     result = sum_positive_numbers(numbers)
#     print(f"Сума чисел: {result}")

# except ValueError as e:
#     print(f"Помилка: {e}")