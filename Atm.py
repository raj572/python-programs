class Atm:
    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()
    def menu(self):
        user_input=input('''
        1.Enter 1 to set pin
        2.Enter 2 to deposite balance
        3.Enter 3 to withdraw
        4.Enter 4 to check balance
        5.Enter 5 to exit
        
        ''')
        if user_input=='1':
            self.set_Pin()
        elif user_input=='2':
            self.Deposite()
        elif user_input=='3':
            self.withdraw()
        elif user_input=='4':
            self.checkBalance()
        else:
            print('Exit')
    def set_Pin(self):
        self.pin=input('Create a Pin : ')
        print('Pin Generated Successfully')
        self.menu()
    def Deposite(self):
        temp=input('Please Enter your pin : ')
        if temp==self.pin:
            amount=int(input('Enter amount :'))
            self.balance=self.balance+amount
            print('Amount deposited successfully')
        else:
            print('Please enter valid pin')
        self.menu()
    def withdraw(self):
        temp=input('Please Enter your pin : ')
        if temp==self.pin:
            amount=int(input('Enter amount you want to withdraw :'))
            if amount<self.balance:
                self.balance=self.balance-amount
                print('withdraw successfully')
            else:
                print('Insufficiant Balance in your account')
        else:
            print('Please provide valid pin')
        self.menu()
    def checkBalance(self):
        temp=input('Please Enter your pin : ')
        if temp==self.pin:
            print('Your current balance')
            print(self.balance)
        else:
            print('Please provide valid pin')
        self.menu()
sbi=Atm()


