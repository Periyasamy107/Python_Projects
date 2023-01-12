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

""" class Emp:
    name = 'sam'
    salary = 1500
    def tax(self):
        print(self.salary*0.10)
e1 = Emp()
print(e1.name)
print(e1.salary)
e1.tax() """

""" class Emp:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
e1 = Emp('god',1000)
print(e1.name)
print(e1.salary) """

""" class Emp:
    def __init__(self,salary):
        self.salary = salary
e1 = Emp(1000)
print(e1.salary)
e1.salary = 1500
print(e1.salary) """

""" class Animal():
    def __init__(self):
        self.eyes = 2
        self.name = 'Dog'
        self.color= 'Spotted'
        self.legs= 4
        self.age  = 10
        self.kids = 0
animal = Animal()
animal.tail = 1
temp = vars(animal)
for item in temp:
    print(item, ':', temp[item]) """


# class Vehicle:
#     def __init__(self):
#         self.trucks = []
#     def add_truck(self, truck):
#         self.trucks.append(truck)
# class Truck:
#     def __init__(self,color):
#         self.color = color
#     def __repr__(self):
#         return '{}'.format(self.color)
# def main():
#     v = Vehicle()
#     for t in 'Yellow Orange Pink Rose Gold'.split():
#         t = Truck(t)
#         v.add_truck(t)
#     print(v.trucks)
# if __name__ == "__main__":
#     main()


# class Employee:
#     pass 
# e1 = Employee()
# setattr(e1, 'salary', 5000)
# e2 = Employee()
# setattr(e2, 'age', 23)
# print(e1.salary)
# print(e2.age)


# class Employee:
#     def __init__(selfie,name,salary):
#         selfie.name = name 
#         selfie.salary = salary 
#     def show_details(final):
#         print('name : ',final.name)
#         print('salary : ',final.salary)
# e1 = Employee('god',5000)
# e1.show_details()

""" class Element:
    def __init__(self, name, city, population):
        self.name = name
        self.city = city
        self.population = population

    def show(self):
        return print(self.name,self.city,self.population)

ele = Element('canada', 'tokyo', 321345)
ele.show() """

""" class myclass:
    def __init__(self):
        self.cnt = 0
    def counter(self,function):
        def wrapper(**args):
            function(self,**args)
            self.cnt += 1
            print('counter inside wrapper : ',self.cnt)
        return wrapper 

global counter_object
counter_object = myclass()

@counter_object.counter
def sample(self):
    print('sample called')

sample()
sample()
sample()
sample()
sample() """

""" class Counter:
    def __init__(self,low,high):
        self.low = low 
        self.high = high 
    def __iter__(self):
        return self 
    def __next__(self):
        if self.low > self.high:
            raise StopIteration
        else:
            self.low+=1
            return self.low-1 

for i in Counter(2,4):
    print(i) """

""" class Reverse:
    def __init__(self,data):
        self.data = data 
        self.index = len(data)
    def __iter__(self):
        return self 
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1 
        return self.data[self.index]
test = Reverse('samy')
for i in test:
    print(i,end='') """

""" class Count:
    def __init__(self,low,high):
        self.low = low
        self.high = high 
    def __iter__(self):
        while self.low < self.high:
            yield self.low 
            self.low+=1
    def __next__(self):
        if self.low > self.high:
            raise StopIteration
        else:
            self.low+=1
            return self.low-1 
    def __reversed__(self):
        while self.high>=self.low:
            yield self.high
            self.high-=1
o1 = Count(0,5)
for i in o1:
    print(i)

o2 = reversed(o1)
for j in o2:
    print(j)  """

