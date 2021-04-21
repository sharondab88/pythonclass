import random  # generate account number for new user
import time  # show time to user upon login
import validation
import database
from getpass import getpass

localtime = time.asctime(time.localtime(time.time()))
print("Current local time is :", localtime)

# register
# - first name, last name , email 
# - generate user account

# login
# - account number and and password


def init():
    #isValidOptionSelected = False
    print("Welcome of Bank of QueenB!")

    #while isValidOptionSelected == False:

    haveAccount = int(input("Do you have an account with us: 1 (yes) or 2 (no)? \n"))

    if (haveAccount == 1):
        isValidOptionSelected = True
        login()

    elif (haveAccount == 2):
        isValidOptionSelected = True
        register()
    else:
        print("You have entered an invalid selection!")


def login():
    print("Please login to your account.")


    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:
        password = getpass("What is your password \n")
        user = database.authenticated_user(account_number_from_user, password)

        if user:
            bank_operation(user)

        print("Invalid account or password, please try again!")  # didnt check for validation
        login()
    else:
        print("Account number is invalid: check that you have up to 10 digits and only integers")
        init()


def register():
    print("******** Register now! ********* ")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password for yourself \n")

    account_number = generation_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawl (3) Logout (4) Report Issue (5) Exit).\n"))

    if (selected_option == 1):
        deposit_operation(user)
    elif (selected_option == 2):
        withdrawal_operation(user)
    elif (selected_option == 3):
        login()
    elif (selected_option == 4):#Added new selection for user from previous assignment
        report_complaint()
    elif (selected_option == 5):
        exit()  # to leave the program
    else:
        print("Invalid Option selected, please try again!")
        bank_operation(user)

##set up new functions from each operation: withdrawl, deposit and complaint

def withdrawal_operation(user):
    withdrawal_amount = int(input("How much would you like to withdraw? \n"))
    print("You withdrew $%s" % withdrawal_amount + "!\n")
    balance = int((user[4]))
    new_balance = str(balance - int(withdrawal_amount))
    print("Your current balance is $ %s!" % new_balance)
    database.withdrawal(user, withdrawal_amount)
    init()
    pass

#Improvement
def deposit_operation(user):
    deposit_amount = int(input("How much would you like to deposit? \n"))
    print("You have deposited $ %s"% deposit_amount + "! \n")
    current_balance = int((user[4]))
    updated_balance = str(current_balance + int(deposit_amount))
    print("Your current balance is now $ %s" % updated_balance)
    database.deposit(user, deposit_amount)
    init()
    pass

def generation_account_number():
    # print("Generating Account Number") ## dont need to show this to user
    return random.randrange(1111111111, 9999999999)

#Improvement
def report_complaint():
    # print("You selected option %s" % selectedOption)
    complaint = input("What issue will you like to report? \n")
    print("Thank you for contacting us! \n")
    pass

#4/16 Improvement
def set_current_balance(user_details, balance):
    user_details[4] = balance

#4/16 Improvement
def get_current_balance(user_details):
    return user_details[4] # 4 is the position of balance

def logout():
    login()

###Actual Banking System ###
### print(generateAccountNumber())
init()