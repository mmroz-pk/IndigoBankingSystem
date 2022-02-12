from check import *

# Welcome
print("-- Welcome to IBS --\n")

# Login
while True:
    print("Select an Option:")
    print("1. Create a New Account")
    print("2. Login to Your Account")
    print("3. Exit")
    start = input("> ")

    if start == "1":
        register()
        continue
    if start == "2":
        pass
    if start == "3":
        exit()

    username = input("Enter your username: ")  # 10 digits
    password = input("Enter your password: ")  # 4 digit PIN

    connect = login(str(username), str(password))  # Send Login Request

    if connect == 1:  # Verify Login Request
        print("\n-- Connected --\n")
        break
    else:
        print("\nIncorrect Username or Password\n")

    # Main Menu
while True:
    print("Select an Option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Check Balance")
    print("5. Open a New Account")
    print("6. Logout")

    option = input("> ")

    if option == "1":
        deposit(username)
        while True:
            deposit_question = input("Would you like to do another deposit?\nY/N: ")
            if str(deposit_question).upper() == "Y":
                deposit(username)
            elif str(deposit_question).upper() == "N":
                break

    if option == "2":
        withdraw(username)
        while True:
            withdraw_question = input("Would you like to do another withdrawal?\nY/N: ")
            if str(withdraw_question).upper() == "Y":
                withdraw(username)
            elif str(withdraw_question).upper() == "N":
                break

    if option == "3":
        transfer(username)
        while True:
            transfer_question = input("Would you like to do another transfer?\nY/N: ")
            if str(transfer_question).upper() == "Y":
                transfer(username)
            elif str(transfer_question).upper() == "N":
                break

    if option == "4":
        check_balance(username)
        while True:
            check_balance_question = input("Would you like to check your balance again?\nY/N: ")
            if str(check_balance_question).upper() == "Y":
                check_balance(username)
            elif str(check_balance_question).upper() == "N":
                break

    if option == "5":
        register()

    if option == "6":
        print("-- You are now logged off! --\n\n-- Thank you for using IBS! --")
        break
        exit()