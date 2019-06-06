# Creating global variables to be used within the code#

todo = "send"
check_balance = "balance"
bal = 5000
amount = 0
new_bal = bal-amount

# function to welcome users and also ask what they will like to todo#

def welcome():

    print("Welcome Stranger")
    username=input("what should i call you ? ")
    print(" Alright " + username +" it is ")
    print(username + " Your account Remaing is " + str(bal))
    action=input(" What can i do for you today ? ")
    if action == todo : # a conditional statemnet to help decide which action suite them the most
        to_do()
    elif action == check_balance:
        check_bal()
    else:
        print(" Invalid Entry")

#function to send money and details of the reciever

def to_do():
    Rname = input("What is the name of your Reciever ? ")
    acct = input("Account Number if your receiver? ")
    amount = input("Please enter amount to send? ")
    if int(amount) >= bal:
        print("Sorry, you are not allowed to empty your Account ")
    else:
        rnumber = input("Enter Reciever Phone number ")
        Snumber = input("Enter your Phonr numbre just incase ")
        print("If all the above details are correct, the reciever will be funded in Five minute, thanks ")
        print("Your new balance is " + str(bal - int(amount)))
        new_bal = bal - int(amount)
        

def check_bal():
    print(new_bal)


welcome() #running the code
