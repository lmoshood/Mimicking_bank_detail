database = ['admin', 'admin']
bal_database= []
from random import randint
import time


class SavingsAcct():

    def welcome(self, intialDeposit, amount_with):
        print('Welcome to the New New Horizon Bank App')
        ask = input('Do you have an account before?: Y(YES)/N(NO) or O to quit ').upper()
        if ask == 'Y':
            self.login(self, intialDeposit, amount_with)
        elif ask == 'N':
            self.reg(self,intialDeposit, amount_with)
        elif ask == 'O':
            print('Thanks for using this app, BYE')
            quit()
        else:
            self.welcome(self, intialDeposit, amount_with)

    def reg(self, intialDeposit, amount_with):
        print('Create your account below')
        reg_username = input('Enter your desire Username: ')
        database.append(reg_username)
        reg_pass1 = input('Enter password: ')
        database.append(reg_pass1)
        reg_pass2 = input('Confirm Password: ')
        if reg_pass1 != reg_pass2:
            print('Password dont Match')
            return self.reg(SavingsAcct,intialDeposit, amount_with)
        else:
            account = randint(1111111111, 9999999999)
            print('Your Account Has been succesfully Created ' + str(account))
            return self.login(SavingsAcct, intialDeposit, amount_with)

    def login(self, intialDeposit, amount_with):
        Username= input('please Enter youur Username ')
        if Username in database:
            password = input('please Enter Your Password here: ')
            if password in database:
                print('Welcome ' + Username+ ' How can i help You Today?')
                return self.action(SavingsAcct, Username, intialDeposit, amount_with)
            else:
                print('Password Note found, Enter Username Again')
                return self.login(SavingsAcct, intialDeposit, amount_with)
        else:
            print('Incorrect Username, Try login Again')
            return self.login(SavingsAcct, intialDeposit, amount_with)

    def deposit(self, Username, amount_with):
        intialDeposit =int(input('Enter amount You are saving into you account: '))
        bal_database.append(intialDeposit)
        print(str(intialDeposit) + ' Has been succesufully save to your account, Cheers')
        return SavingsAcct.action(SavingsAcct, Username, intialDeposit, amount_with)

    def withdraw(self, Username, intialDeposit):
        print('Cheers '+ Username )
        amount_with = int(input('Enter amount to Withdraw: '))
        while amount_with > intialDeposit:
            print('Insufficent Balance')
            amount_with = int(input('Enter amount to Withdraw: '))
        else:
            with_code = randint(1111, 9999)
            print('Thanks You, please see the Cashier for your cash and show them this Code ' +(str(with_code)))
            return SavingsAcct.action(SavingsAcct, Username, intialDeposit, amount_with)

    def check_bal(self, intialDeposit,amount_with ):
        new_depo = intialDeposit - amount_with
        if str(new_depo) < '0':
            print('Your Balance is Empty')
        else:
            print('Your Balnace is ' + str(new_depo))
            for i in range(1):
                print('''Taking your back to the main menu in...\n...3''')
                time.sleep(2)
                print('...2')
                time.sleep(2)
                print('...1')
                time.sleep(2)
                return SavingsAcct.welcome(SavingsAcct,intialDeposit,amount_with)

    def action(self, Username, intialDeposit, amount_with):
        print('''please Choose from this Option below to start
        Enter 1 to make deposit into your new account 
        Enter 2 to Withdraw from the Account 
        Enter 0 to Quite this program
        Enter 3 to Check your Balance ''')
        action = input('>>>>> ')
        if action == '0':
            SavingsAcct.welcome(self, intialDeposit, amount_with)
        elif action == '1':
            SavingsAcct.deposit(SavingsAcct, Username,amount_with)
        elif action == '2':
            self.withdraw(SavingsAcct,Username, intialDeposit)
        elif action == '3':
            SavingsAcct.check_bal(SavingsAcct,intialDeposit, amount_with)
        else:
            print('Invalid Command')
            return SavingsAcct.action(SavingsAcct, Username, intialDeposit, amount_with)

SavingsAcct.welcome(SavingsAcct,intialDeposit=0, amount_with=0)
