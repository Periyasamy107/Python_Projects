""" class Vehicle:
    def __init__(self,speed,mileage):
        self.speed=speed
        self.mileage=mileage 
car = Vehicle(150,18)
bus = Vehicle(100,28)
bike = Vehicle(300,10)

print(f'car speed : {car.speed}, car mile : {car.mileage}')
print(bus.speed,bus.mileage)
print(bike.speed,bike.mileage) """

""" class Vehicle:
    def __init__(self,speed,mileage):
        self.speed=speed
        self.mileage=mileage 

    def car(Vehicle):
        pass 

car = Vehicle(150,18,)
print('car speed :',car.speed,'car mile :',car.mileage) """

""" class S:
    pass 
class M:
    pass 
s1=S()
m1=M()
print(isinstance(s1,S))
print(isinstance(m1,S))
print(isinstance(m1,M))
print(isinstance(s1,M)) """

""" class Bank_account:
    def __init__(self,acctnum,name,balance) :
        self.acctnum = acctnum
        self.name = name 
        self.balance = balance 
    def Deposit(self,d):
        self.balance = self.balance + d
    def Withdraw(self,w):
        if (self.balance < w):
            print('Insufficient balance')
        else:
            self.balance = self.balance - w 
    def Fees(self):
        self.balance = (98/100)*self.balance 
    def Display(self):
        print('Acct number : ', self.acctnum)
        print('Name : ', self.name)
        print('Balance : ', self.balance)
c1 = Bank_account(12345546,'Hena',10000)
c1.Deposit(5000)
c1.Withdraw(1000)
c1.Fees()
c1.Display() """

""" class Book:
    def __init__(self,author,price):
        self.author = author
        self.price = price
    def View(self):
        print('Author : ',self.author)
        print('Price : ',self.price)
book1 = Book('william james',1000)
book1.View()
book2 = Book('Biggod',10000)
book2.View() """

""" class Bank_account:
    def __init__(self):
        self.balance = 0
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance 
a = Bank_account()
print(a.balance)
print(a.deposit(100))
print(a.withdraw(40)) """

""" class Employee:
    pass
e1 = Employee()
print(e1)
e1.name = 'sam'
print(e1.name)
e1.age = 34
print(e1.age) """

