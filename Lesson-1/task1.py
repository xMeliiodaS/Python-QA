# Ex-1
# day = input("What's the day today ?")
# actual_day = "Wednesday"
#
# print(f"Today is {actual_day}" if day != actual_day else f'Correct! Today is {actual_day}')
from functools import reduce

# Ex-2 Casting
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# res = 7

# type(x + y) == int and
# if num1 + num2 == res:
#     print(f'Great!, the result of {num1}+{num2} is', num1 + num2)
# else:
#     print(f'X  The result is not correct')

# Ex-3 Loops

# List of numbers
# numbers = [1, 5, 7, -4, 6, 3]
#
# # Keep tracking if a negative number found or not
# negative_found = False
#
# # Iterate through the list
# for num in numbers:
#     if num < 0:
#         print(num)
#         negative_found = True
#         break
#
# # If no negative number was found
# if negative_found is False:
#     print("No negative number is found")


# Ex-4 Map
my_list = [1, 2, 3, 4, 5, 6]
my_list_add_three = list(map(lambda x: x + 3, my_list))
print(my_list_add_three)


# celsius_list = [20, 22, 25, 27, 30, 33]
# fahrenhit_list = list(map(lambda celsius: (celsius * (9 / 5)) + 32, celsius_list))
# filtered = list(filter(lambda fahrenhit: fahrenhit > 75, fahrenhit_list))
# print(filtered)

# Ex-5 Celsius and fahrenheit

def celsius_to_fahrenheit(celsius_list):
    return list(map(lambda celsius: (celsius * (9 / 5)) + 32, celsius_list))


def filter_fahrenheit_above_75(fahrenheit_list):
    return list(filter(lambda fahrenheit: fahrenheit > 75, fahrenheit_list))


def list_avg(filtered_list):
    return reduce(lambda x, y: x + y, filtered_list) / len(filtered_list) if filtered_list else 0


celsius_list = [20, 22, 25, 27, 30, 33]
fahrenheit_list = celsius_to_fahrenheit(celsius_list)
filtered_fahrenheit_list = filter_fahrenheit_above_75(fahrenheit_list)
avg_filtered = list_avg(filtered_fahrenheit_list)
print(fahrenheit_list)
print(filtered_fahrenheit_list)
print(avg_filtered)
