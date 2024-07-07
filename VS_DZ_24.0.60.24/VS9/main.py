# def print_quote():
#     print('"Don\'t compare yourself with anyone in this world....')
#     print('if you do so, you are insulting yourself."')
#     print('Bill Gates')
#--------------------------------------------------
# def print_even_numbers(a, b):
#     for i in range(a, b+1):
#         if i % 2 == 0:
#             print(i)
#--------------------------------------------------
# def print_square(size, symbol, filled):
#     if filled:
#         for i in range(size):
#             print(symbol * size)
#     else:
#         for i in range(size):
#             if i == 0 or i == size-1:
#                 print(symbol * size)
#             else:
#                 print(symbol + ' ' * (size-2) + symbol)
#--------------------------------------------------
# def find_min(a, b, c, d, e):
#     return min(a, b, c, d, e)
#--------------------------------------------------
# def multiply_numbers(a, b):
#     if a > b:
#         a, b = b, a
#     product = 1
#     for i in range(a, b+1):
#         product *= i
#     return product
#--------------------------------------------------
# def count_digits(n):
#     return len(str(n))
#--------------------------------------------------
# def is_palindrome(n):
#     str_n = str(n)
#     return str_n == str_n[::-1]