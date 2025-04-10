import math
import re


class BankAccount:
    def __init__(self, som=0):
        self.__balance = som

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance


class User:
    def __init__(self, name, password):
        self.__name = name
        self.__password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def pw(self):
        return "*" * len(self.__password)

    @pw.setter
    def pw(self, password):
        if re.match(r"[A-Za-z\d]{7,}$", password):
            self.__password = password
        else:
            raise ValueError("Pw error")


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary >= 30_000:
            self.__salary = salary
        else:
            raise ValueError("Мало, очееень мало")


class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius error")
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius >= 0:
            self.__radius = radius
        else:
            raise ValueError("Radius error")

    @property
    def area(self):
        return math.pi * pow(self.__radius, 2)


class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        if height < 0:
            raise ValueError("Height error")
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height >= 0:
            self.__height = height
        else:
            raise ValueError("Height eroor")




account = BankAccount(1000)
print(account.get_balance())  
account.deposit(500)
print(account.get_balance())  
print(account.withdraw(2000))  
print(account.withdraw(1000))  
print(account.get_balance())  


user = User("Daniel", "password123")
print(user.name)  
user.name = "Danchik"
print(user.name)  
print(user.pw)  
try:
    user.pw = "12345"  
except ValueError as e:
    print(e)


employee = Employee("Daniel", 50000)
print(employee.name)  
print(employee.salary)  
try:
    employee.salary = 20000  
except ValueError as e:
    print(e)


circle = Circle(10)
print(circle.radius)  
print(circle.area)  
try:
    circle.radius = -5  
except ValueError as e:
    print(e)


cylinder = Cylinder(10, 20)
print(cylinder.radius)  
print(cylinder.height)  
try:
    cylinder.height = -10  
except ValueError as e:
    print(e)
