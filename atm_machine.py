class Atm:
    def __init__(self):
        self.__pin =''
        self.__balance = 0
        self.__menu()
        
        
    def menu(self):
        user_input = input("""
        How would you like to proceed?
        1. To create a pin
        2. Deposit
        3. Withdraw
        4. Balance
        5. Exit
""")
        
        if user_input == '1':
            self.create_pin()       #For Creating pin
            self.__menu()             #For repetition
        elif user_input == '2':
            self.deposit()          #For Deposit
            self.__menu()
        elif user_input == '3':     
            self.withdraw()         #For witdraw
            self.__menu()
        elif user_input == '4':     
            self.check_balance()    #For checking balance
            self.__menu()
        elif user_input == '5':
            print("Bye")            #For Exit
        else:
            print("Invalid")
            self.__menu()
    
    def create_pin(self):
        self.pin = input("Enter your pin to create :")
        print("Pin set successfully")
    
    def deposit(self):
        temp = input("Enter your pin :")
        if temp == self.__pin:
            amount = int(input("Enter amount to be deposited:"))
            self.__balance += amount
            print("Deposited successfully")
        else:
            print("Invalid Pin")
    def withdraw(self):
        temp = input("Enter your pin :")
        if temp == self.__pin:
            amount = int(input("Enter amount to be Withdrawan:"))
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal successfully")
            else:
                print("insufficient amount")
        else:
            print("Invalid Pin")
    
    def check_balance(self):
        temp = input("Enter your pin :")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Inavalid pin")
        
sbi = Atm()



