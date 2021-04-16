import random  # geneate account number for new user
import time  # show time to user upon login

localtime = time.asctime(time.localtime(time.time()))
print("Current local time is :", localtime)

# register
# - first name, last name , email 
# - generate user account

# login
# - account number and and password

# Generated acct numbers for test users to add for the dictionary
# Use same format from register function
#database = {4103041978: ["Queen", "B", "QB@aol.com", "Mom"]}
#database = {4563766566: ["Oakleigh", "B", "OB@aol.com", "Baby"]}
database = {7147200027: ["Papa", "P", "PP@aol.com", "Dad"]}

def init():
    isValidOptionSelected = False
    print("Welcome of Bank of QueenB!")

    while isValidOptionSelected == False:

        haveAccount = int(input("Do you have an account with us: 1 (yes) or 2 (no)? \n"))

        if (haveAccount == 1):
            isValidOptionSelected = True
            login()


        elif (haveAccount == 2):
            isValidOptionSelected = True
            register()
        else:
            print("You have entered an invalid selection")


def login():
    print("Please login to your account.")

    isLoginSuccessful = True

    while isLoginSuccessful == True:
        accountNumberFromUser = int(input("What is your account number? \n"))
        password = input("What is your password? \n")

        for accountNumber, userDetails in database.items():
            if (accountNumber == accountNumberFromUser):
                if (userDetails[3] == password):
                    isLoginSuccessful = False
        print("Invalid account or password, please try again!")

    bankOperation(userDetails)


def register():
    print("******** Register now! ********* ")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create your password? \n")

    accountNumber = generateAccountNumber()
    database[accountNumber] = [first_name, last_name, email, password]

    # return database; #for testing purposes, dont neeed to display output of user

    print("Your account has been created!! ")
    # below prints pulled in from p23
    print("== ==== ===== ==== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe!")
    print("== ==== ===== ==== ===")

    login()

    ###print("This is the register function")


def bankOperation(user):
    print("Welcome %s %s" % (user[0], user[1]))

    selectdOption = int(
        input("What would you like to do? (1) deposit (2) withdrawl (3) Logout (4) Report Issue (5) Exit).\n"))

    if (selectdOption == 1):
        depositOperation()
    elif (selectdOption == 2):
        withdrawawlOperation()
    elif (selectdOption == 3):
        login()
    elif (selectdOption == 4): #Added new selection for user from previous assignment
        reportComplaint()
    elif (selectdOption == 5):
        exit()  # to leave the program
    else:
        print("Invalid Option selected, please try again!")
        bankOperation(user)


##set up new functions from each operation: withdrawl, deposit and complaint
def withdrawawlOperation():
    withdrawal = input("How much would you like to withdraw? \n")
    print("Please take your $" + withdrawal + "!\n")
    pass

#Improvement
def depositOperation():
    deposit = (input("How much would you like to deposit? \n"))
    print("You have deposited $" + deposit + "! \n")
    pass
            
def generateAccountNumber():
    # print("Generating Account Number") ## dont need to show this to user
    return random.randrange(1111111111, 9999999999)

#Improvement
def reportComplaint():
    # print("You selected option %s" % selectedOption)
    complaint = input("What issue will you like to report? \n")
    print("Thank you for contacting us! \n")
    pass


###Actual Banking System ###
### print(generateAccountNumber())
init()
