'=======================================1========================================'
from abc import ABC, abstractmethod, abstractproperty
import math
class Transport(ABC):
    @property
    @abstractmethod
    def move(slef):
        ...
class Car(Transport):
    def move(self):
        return 'Car is moving on the road'

class Plane(Transport):
    def move(self):
        return 'Plane is flying in the sky'

car = Car()
print(car.move())

plane = Plane()
print(plane.move())
'=======================================2========================================'
print('\n')
'================================================================================'
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @property
    @abstractmethod
    def pay(self):
        pass

class CreditCard(PaymentMethod):
    def __init__(self, amount):
        self._amount = amount

    @property
    def pay(self):
        return f'Оплата {self._amount} через Credit Card'

class PayPal(PaymentMethod):
    def __init__(self, amount):
        self._amount = amount

    @property
    def pay(self):
        return f'Оплата {self._amount} через PayPal'

creditcard = CreditCard(1000)
print(creditcard.pay)

paypal = PayPal(500)
print(paypal.pay)
'=======================================3========================================'
print('\n')
'================================================================================'
class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 1)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
circle = Circle(5)
print(circle.area())

rectangle = Rectangle(10, 20)
print(rectangle.area())
'=======================================4========================================'
print('\n')
'================================================================================'
class OutputDevice(ABC):
    @abstractmethod
    def display(self, text):
        ...

class Monitor(OutputDevice):
    def display(self, text):
        print(f'[Monitor] : {text}')

class Printer(OutputDevice):
    def display(self, text):
        print(f'[Printer] : {text}')
        
monitor = Monitor()
monitor.display('Hello, world!')

printer = Printer()
printer.display('Hello, world!')

'=======================================5========================================'
print('\n')
'================================================================================'
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print('Гав!')

class Cat(Animal):
    def make_sound(self):
        print('Мяу!')

dog = Dog()
dog.make_sound()

cat = Cat()
cat.make_sound()
'=======================================6========================================'
print('\n')
'================================================================================'
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Developer(Employee):
    def calculate_salary(self):
        return 500000

class Manager(Employee):
    def calculate_salary(self):
        return 7000
developer = Developer()
print(f'Зарплата разработчика: {developer.calculate_salary()}')

manager = Manager()
print(f'Зарплата менеджера: {manager.calculate_salary()}')
'=======================================7========================================'
print('\n')
'================================================================================'
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print('Подключение к MySQL')

    def disconnect(self):
        print('Отключение от MySQL')

class PostgreSQLDatabase(Database):
    def connect(self):
        print('Подключение к PostgreSQL')

    def disconnect(self):
        print('Отключение от PostgreSQL')

mysql_db = MySQLDatabase()
mysql_db.connect()
mysql_db.disconnect()

postgres_db = PostgreSQLDatabase()
postgres_db.connect()
postgres_db.disconnect()

