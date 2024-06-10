import random
import string


class GeneratePassword:

    def __init__(self):
        pass

    def generate_password(self, psw_length):
        """
        Generate random characters to form password
        :param psw_length: THe length of the password
        :return: Return the generated password
        """
        characters = string.ascii_letters + string.digits + string.punctuation

        random_password = ''.join(random.choice(characters) for _ in range(psw_length))

        return random_password
