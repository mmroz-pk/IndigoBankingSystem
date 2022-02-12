import os
from os.path import isfile
from random import *
from pathlib import *


def register():
    # Randomize New Login
    register_username = randint(1000000000, 9999999999)
    register_password = randint(1000, 9999)

    # Save Username & Password
    try:
        os.mkdir(f"./database/{register_username}")
    except OSError:
        print("This user already exists")
    else:
        register_file = open(f"./database/{str(register_username)}/PIN", "w")
        register_file.write(str(register_password))
        register_file.close()
        print("--Your new login information--")
        print(f"Account Number: {register_username}")
        print(f"PIN Code: {register_password}")
        print("--\n")

        # Add 0 to Balance
        balance_file = open(f"./database/{str(register_username)}/Balance", "w")
        balance_file.write(str("0"))
        balance_file.close()


def verify(username):
    verify_username = isfile(f"./database/{username}/PIN")
    if verify_username is False:
        username_status = 0
    else:
        username_status = 1

    return username_status


def login(username, password):
    if verify(username) == 1:
        check_username = open(f"./database/{username}/PIN", "r").read()
        if check_username == str(password):
            # print("Correct Password")
            username_status = 1
        else:
            # print("Incorrect Password")
            username_status = 0
        return username_status
    else:
        # print("Incorrect Username")
        username_status = 3
    return username_status


def deposit(username):
    deposit_amount = input("How much would you like to deposit?\n> ")

    deposit_read = open(f"./database/{username}/Balance", "r").read()
    deposit_to = open(f"./database/{username}/Balance", "w")

    deposit_add = float(deposit_read) + float(deposit_amount)
    deposit_add = float("{:.2f}".format(deposit_add))

    deposit_to.write(str(float(deposit_add)))

    print(f"You have deposited: ${deposit_amount}")


def withdraw(username):
    current_balance = open(f"./database/{username}/Balance", "r").read()
    print(f"Available Balance: {current_balance}")

    withdraw_amount = input("How much would you like to withdraw?\n> ")

    deposit_subtract = float(current_balance) - float(withdraw_amount)
    deposit_subtract = float("{:.2f}".format(deposit_subtract))

    if deposit_subtract <= -1:
        print("You don't have enough funds to withdraw that sort of amount")
    else:

        update_balance = open(f"./database/{username}/Balance", "w")
        update_balance.write(str(float(deposit_subtract)))

        print(f"You have withdrawn: ${withdraw_amount}")


def transfer(username):
    current_balance = open(f"./database/{username}/Balance", "r").read()
    print(f"Available Balance: {current_balance}")

    transfer_amount = input("How much would you like to transfer?\n> ")

    deposit_subtract = float(current_balance) - float(transfer_amount)
    deposit_subtract = float("{:.2f}".format(deposit_subtract))

    if deposit_subtract <= -1:
        print("You don't have enough funds to execute the transfer")
    else:
        receiver = input("Enter the Reciever's 10 Digit Account Number:\n> ")
        check_receiver = verify(receiver)
        if check_receiver == 0:
            print("This account does not exist in our system")
        elif check_receiver == 1:
            receiver_balance = open(f"./database/{receiver}/Balance", "r").read()

            receiver_add = float(receiver_balance) + float(transfer_amount)
            receiver_add = float("{:.2f}".format(receiver_add))

            transfer_to_receiver = open(f"./database/{receiver}/Balance", "w")
            transfer_to_receiver.write(str(float(receiver_add)))

            update_balance = open(f"./database/{username}/Balance", "w")
            update_balance.write(str(float(deposit_subtract)))

            print(f"You have transfern: ${transfer_amount}")


def check_balance(username):
    current_balance = open(f"./database/{username}/Balance", "r").read()
    print(f"Your current balance is: {current_balance}")