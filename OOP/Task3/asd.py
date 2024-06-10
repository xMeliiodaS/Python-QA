import string
import secrets


def generate_password(length):
    temp = length
    password = ""
    while temp > 0:
        password += secrets.choice \
            (string.ascii_letters + string.digits + string.punctuation)
        temp -= 1
    return password


print(generate_password(5))
