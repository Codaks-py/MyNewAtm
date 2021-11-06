import time
import AccountStimulator
import random
import datetime


acclist=[]
Accounts = {"Bimpe": "12345678"}


def init():
    repeat = "Y"
    while repeat == "Y":
        print()
        # This is more like the prompt message
        # Ask if the user is an existing user or not

        print("Welcome dear User!\nHere are option to pick from in this program")
        prompt = input("Do you have an account(yes/no): ").capitalize()

        # Get user response, then utilizes
        # If existing user, Takes user to the login page
        # else, take user to registration format

        if prompt == "Yes":
            login()
        elif prompt == "No":
            register()
        else:
            print("Invalid option....")

        repeat = input("Like to Perform Operations(y/n).: ").capitalize()


def login():
    repeat = "Yes"
    # Collect user login details and utilizes
    # if valid continues, else stop operation
    # and return user back to the init()

    username = input("Enter your registered username: ")
    password = input("Enter password: ")
    initbal = 0.0
    total = 100000

    userSlash = username[:2]
    passSlash= password[:3]

    userFile = userSlash+passSlash


    with open(userFile + ".txt", "r") as f:
                with open(userFile+".txt", "a") as g:
                    print()
                    while repeat == "Yes":
                        print(f"\tWelcome Back {username}\n\tPress 1,To Deposit\n\tPress 2,To Withdraw\n\tPress 3,To Transfer\n\tPress 4,To Complain\n\tPress 5,To logout ")
                        prompt = input("Enter a valid Option: ")
                        if prompt == "1":
                            bal = deposit(initbal)

                        elif prompt == "2":
                            withdrawal(total)

                        elif prompt == "3":
                            Transfer(total)

                        elif prompt == "4":
                            complaint()

                        elif prompt == "5":
                            logout()
                        else:
                            print("Invalid option picked.")
                        print()
                        repeat = input("\tMore Operations To Perform On Your Account?(yes/no) : ").capitalize()




def AccountGenerate():
    with open("Accounts.txt", "a") as d:
        account = random.randrange(1111111111, 9999999999)
        na = str(account)
        d.write(str(account) + "\n")

    return account


def deposit(InitBal):
    total = 0.0
    DepositAmount = float(input("Enter Depositing Amount: "))

    print("Enter Account Details..")

    savings = AccountStimulator.BankAccount(InitBal)
    time.sleep(1)
    AccountName = input("Enter name of Receiving Account: ")
    AccountNumber = input("Enter Account Number: ")
    with open("Accounts.txt", "r") as f:
        try:
            for AccountNumber in f:
                    print("Depositing the funds into your Account....")
                    time.sleep(1)
                    print("Connecting to the server...")
                    time.sleep(3)
                    savings.deposit(DepositAmount)
                    print("Deposit Done.\nNew balance == ",format(savings.get_balance(), ".2f"),  sep="")
                    print("No Charges included..")
                    FinalBalance = format(savings.get_balance(), ".2f")
                    total += FinalBalance
                    # f_FloatBalance = float(FinalBalance)

        except:
            print("Invalid Account Number!")
    return total


def Transfer(total):
    TransferAmount = float(input("Enter Withdraw Amount:"))
    pin = input("Enter pin: ")
    if len(pin) == 4:
        savings = AccountStimulator.BankAccount(total)
        print("Might Take a few seconds...")
        time.sleep(2)
        print("\tConnecting servers..")
        time.sleep(3)
        print("\tTransferring funds")
        time.sleep(3)
        savings.withdraw(TransferAmount)
        print(f"Operation done.\nNew Balance == ", format(savings.get_balance(), ".2f"), sep="")
        Finalbal = format(savings.get_balance(), ".2f")
        y = float(Finalbal)
        x = float(total)
        x -= y
        return x


def withdrawal(total):
    WithdrawAmount = float(input("Enter Withdraw Amount:"))
    pin = input("Enter pin: ")
    if len(pin) == 4:

        savings = AccountStimulator.BankAccount(total)
        print("Might Take a few seconds...")
        time.sleep(2)
        print("\tConnecting servers..")
        time.sleep(3)
        print("\tWithdrawing funds")
        time.sleep(3)
        savings.withdraw(WithdrawAmount)
        print(f"Operation done.\nNew Balance == ",format(savings.get_balance(), ".2f"), sep="")
        Finalbal = format(savings.get_balance(), ".2f")
        y = float(Finalbal)
        x = float(total)
        x -= y
        return x

    else:
        print("Invalid pin input")


def complaint():
    userInput = input("Pour out your mind and let analysis the issue together: ")
    now = datetime.datetime.now()
    today = datetime.date.today()

    print("Complaint made was: {", userInput ,"}")
    print("\tAt exactly ", now)
    print("\tOn ", today)
    time.sleep(3)
    print("\tIssue being attended to...\n\tMight take a little while")
    time.sleep(5)
    print("\tBe rest assured we cherish our users\n\tComplaint has been attended to,...\n\tSorry for the inconveniences ")


def register():
    username = input("Enter a username of your choice: ")
    password = input("Enter a password: ")

    userslash = username[:2]
    passSlash = password[:3]
    UserFile = userslash+passSlash

    time.sleep(2)
    AccountGenerate()
    print("Your account number is ", AccountGenerate())
    print("Do well in Copying it..")
    with open(UserFile+".txt", "w") as w:

        time.sleep(1)
        print("Creating a Unique file for you\nAll Done...")
        init()
        return UserFile

def logout():
    print("Thanks for choosing us..")
    init()


# deposit(0)

# print(AccountGenerate())

init()
# withdrawal(1000)
# complaint()