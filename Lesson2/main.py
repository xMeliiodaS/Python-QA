# Error handling - try except finally

def div(num1: int, num2: int) -> int:
    """
    :param num1: First number
    :param num2: Second number
    :return: return the division between num1 and num2
    """
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: can't divide by zero")
    except TypeError:
        print("Error: all inputs should be numbers")
    # Valid - Works when valid
    else:
        print("Result is", result)
    # Does not matter if there is error or no error -> always do
    finally:
        print("Executing finally clause")


# Error - raise

def check_positive(value: int) -> None:
    """
    :param value: number
    print the value
    """
    if value < 0:
        raise ValueError(f"The value must be positive")
    print(value)


try:
    check_positive(-1)
except ValueError as e:
    print(f"We catch the error: {e}")
