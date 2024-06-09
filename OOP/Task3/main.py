from Task3.bank import BankAccount


def main():
    bank_acc = BankAccount("123", 100)

    while True:
        try:
            option = int(input("Enter 1 to deposit\nEnter 2 to withdraw\n"
                               "Enter 3 to get balance\nEnter 4 to exit\n"))

        except ValueError:
            print("Please enter a number")

        if isinstance(option, int):
            if option == 1:
                try:
                    money_to_deposit = int(input("Enter the amount of money u would like to add:"))
                    bank_acc.deposit(money_to_deposit)
                except ValueError:
                    print("Please a Enter a number!")

            elif option == 2:
                try:
                    money_to_withdraw = int(input("Enter the amount of money u would like to add:"))
                    bank_acc.withdraw(money_to_withdraw)
                except ValueError:
                    print("Please a Enter a number!")

            elif option == 3:
                print(f"\nUr account balance is {bank_acc.get_balance()}\n")

            elif option == 4:
                break

        else:
            print("Please enter a number")


if __name__ == '__main__':
    main()
