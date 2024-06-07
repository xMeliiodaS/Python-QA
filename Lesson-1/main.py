# Basic
# id = "212207112"
# name = "Bahaa Abu zalaf"
# age = 23.75
# college = "Technion"
# isVisible = False
#
# print(f'My name is {name} and im {age} old. My id is {id}, also i \n'
#       f'studied practical engineer for 2 years in the {college}. Am I visible? {isVisible}')


# If statements
# if type(id) is str:
#     print(type(id))
# print(type(age))
# print(type(isVisible))
#
# name = input("Enter ur name: ")
# print(name)


# Loops - for
# for number in [1, 2, 3, 4]:
#     print(number, end="")

# while
# max = 10
# i = 0
# while True:
#     if i < max:
#         print(i)
#         i += 1
#     else:
#         break


# Functions

# def sum1(num1: int, num2: int) -> int:
#     """
#     :param num1: First number
#     :param num2: Second number
#     :return: Return the sum of the 2 numbers
#     """
#     return num1 + num2
#
#
# print(sum1(1, 3))

# Lambda
# sum_2 = lambda x, y: x + y
# print(sum_2(1, 2))


# Functional programming basics - map(), filter(), reduce()
# map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# filter() - return True or False
# While x is even, append to the list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# reduce()
from functools import reduce

product1 = reduce(lambda x, y: x * y, numbers)
print(product1)

product2 = reduce(lambda x, y: x + y, numbers)
print(product2)