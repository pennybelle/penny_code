# n = 11

# def divide_or_square(n):
#     if n % 5 == 0:
#         return f'square root: {n ** 0.5}'
#     else:
#         return f'remainder: {n % 5}'

# print(divide_or_square(n))



data = {'dairy': 'orange', 'fruit': 'apples', 'vegetable': 'peas'}

# def longest_value(data):
#     longest = ''
#     for food in data:
#         food = data.values()
#         if len(food) > len(longest):
#             longest = food
#     return max(food)

# print(data.values())

# print(longest_value(data))

# divide_or_square = lambda n: n%5 or n**.5

# print(divide_or_square(25))

def longest_value_2(data):
    return max(data.values(), key=len)

print(longest_value_2(data))