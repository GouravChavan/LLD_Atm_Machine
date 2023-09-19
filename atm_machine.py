class Atm:
    def __init__(self):
        self.pin =''
        self.balance = 0
        self.menu()
        
        
    def menu(self):
        user_input = input("""
        How would you like to proceed?
        1.To crete pin
        2.Deposit
        3.Withdraw
        4.Balance
        5.Exit
""")
        
        if user_input == '1':
            self.create_pin()       #For Creating pin
            self.menu()             #For repetition
        elif user_input == '2':
            self.deposit()          #For Deposit
            self.menu()
        elif user_input == '3':     
            self.withdraw()         #For witdraw
            self.menu()
        elif user_input == '4':     
            self.check_balance()    #For checking balance
            self.menu()
        elif user_input == '5':
            print("Bye")            #For Exit
        else:
            print("Invalid")
            self.menu()
    
    def create_pin(self):
        self.pin = input("Enter your pin to create :")
        print("Pin set successfully")
    
    def deposit(self):
        temp = input("Enter your pin :")
        if temp == self.pin:
            amount = int(input("Enter amount to be deposited:"))
            self.balance += amount
            print("Deposited successfully")
        else:
            print("Invalid Pin")
    def withdraw(self):
        temp = input("Enter your pin :")
        if temp == self.pin:
            amount = int(input("Enter amount to be Withdrawan:"))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawan successfully")
            else:
                print("insufficiant amount")
        else:
            print("Invalid Pin")
    
    def check_balance(self):
        temp = input("Enter your pin :")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Inavalid pin")
        





