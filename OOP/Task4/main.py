from Task4.generate_password import GeneratePassword


def main():
    generator = GeneratePassword()
    password = generator.generate_password(12)
    print(password)


if __name__ == '__main__':
    main()