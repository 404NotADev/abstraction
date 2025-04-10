# Концепции ООП: Инкапсуляция, Наследование, Полиморфизм, Абстракция

# 1. Абстракция — мы создаём общую модель/шаблон (например, "Животное"),
# не вдаваясь в детали конкретной реализации.
class Animal:
    def __init__(self, name):
        self.name = name  # Инкапсуляция: данные (name) "спрятаны" внутри объекта

    def speak(self):
        # Это абстрактный метод — в базовом классе он не реализован
        raise NotImplementedError("Этот метод должен быть переопределён в подклассе")

# 2. Наследование — создаём конкретные классы, которые наследуют свойства и методы от общего (Animal)
class Dog(Animal):
    def speak(self):
        return f"{self.name} говорит: Гав!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} говорит: Мяу!"

# 3. Полиморфизм — используем один и тот же метод speak, но каждый класс реализует его по-своему
def animal_talk(animal):
    # Эта функция работает с любым животным
    print(animal.speak())

# Создаём объекты
dog = Dog("Шарик")
cat = Cat("Мурка")

# Вызываем полиморфную функцию
animal_talk(dog)  # Шарик говорит: Гав!
animal_talk(cat)  # Мурка говорит: Мяу!

# Также можно продемонстрировать инкапсуляцию с "приватными" переменными:
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Двойное подчеркивание делает переменную "приватной"

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостаточно средств")

    def get_balance(self):
        return self.__balance

# Используем BankAccount
account = BankAccount("Алиса", 1000)
account.deposit(500)
account.withdraw(300)
print(account.get_balance())  # 1200
# print(account.__balance)  # Ошибка! Приватная переменная
'------------------------------------------------------------------------------------------------------'
# Класс — это как чертёж. Объект — это конкретный экземпляр по этому чертежу.

class Car:
    # Атрибут класса — общий для всех машин
    wheels = 4

    def __init__(self, brand, color):
        # Атрибуты объекта — уникальны для каждой машины
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"{self.color} {self.brand} поехала!")

# Создаём объекты (экземпляры) класса Car
car1 = Car("Toyota", "Красная")
car2 = Car("BMW", "Синяя")

# Обращаемся к атрибутам объекта
print(car1.brand)   # Toyota
print(car2.color)   # Синяя

# Обращаемся к методу
car1.drive()        # Красная Toyota поехала!

# Обращаемся к атрибуту класса через объект и через класс
print(car1.wheels)       # 4
print(Car.wheels)        # 4

# Меняем wheels только у класса — это отразится на всех объектах, если они не переопределяли wheels
Car.wheels = 6

print(car1.wheels)  # 6
print(car2.wheels)  # 6

# Можно создать уникальный атрибут wheels у конкретного объекта
car1.wheels = 8     # Это создаёт атрибут только у car1

print(car1.wheels)  # 8 (уникальное значение для car1)
print(car2.wheels)  # 6 (осталось как у класса)

# Проверим внутренности
print(car1.__dict__)  # {'brand': 'Toyota', 'color': 'Красная', 'wheels': 8}
print(Car.__dict__)   # покажет wheels как атрибут класса (в числе других служебных вещей)

'-------------------------------------------------------------------------------------------------------------'
class Person:
    def __init__(self, name, age):
        # self — это ссылка на конкретный объект, который мы создаём
        # через self мы сохраняем данные в объекте
        self.name = name
        self.age = age

    # Метод класса — обычная функция внутри класса, всегда получает self первым аргументом
    def greet(self):
        # Используем self, чтобы обратиться к данным объекта
        print(f"Привет! Меня зовут {self.name}, мне {self.age} лет.")

    def have_birthday(self):
        # Изменим возраст объекта через self
        self.age += 1
        print(f"{self.name} теперь {self.age} лет!")

# Создаём объект
person1 = Person("Аня", 25)

# Вызов методов
person1.greet()         # Привет! Меня зовут Аня, мне 25 лет.
person1.have_birthday() # Аня теперь 26 лет!

# Создаём ещё одного человека
person2 = Person("Игорь", 30)
person2.greet()         # Привет! Меня зовут Игорь, мне 30 лет.

# Важно! self передаётся автоматически при вызове метода:
# Вот это:
person1.greet()

# То же самое, что:
Person.greet(person1)  # Мы вручную передали self (редко делается так)

'--------------------------------------------------------------------------------------------------'
class Book:
    def __init__(self, title, author):
        # Инициализатор __init__ вызывается сразу при создании объекта
        # Здесь мы задаём начальные значения (атрибуты объекта)
        self.title = title
        self.author = author
        print(f"Книга \"{self.title}\" автора {self.author} добавлена в систему.")

    def read(self):
        print(f"Вы читаете \"{self.title}\".")

    def __del__(self):
        # Финализатор __del__ вызывается при удалении объекта
        # Обычно используется для освобождения ресурсов (файлы, соединения и т.д.)
        print(f"Книга \"{self.title}\" удалена из системы.")

# Создаём объект
book1 = Book("1984", "Джордж Оруэлл")
book1.read()

# Удаляем объект вручную (обычно это происходит автоматически, когда объект "умирает")
del book1

# После del book1 сработает __del__ — "Книга ... удалена из системы."
'------------------------------------------------------------------------------------------------------'
class Singleton:
    _instance = None  # переменная класса для хранения единственного экземпляра

    def __new__(cls, *args, **kwargs):
        # метод __new__ вызывается до __init__ и отвечает за создание объекта
        if cls._instance is None:
            # если экземпляр ещё не создан, создаём его
            cls._instance = super().__new__(cls)
            print("Создан новый Singleton-объект")
        else:
            # если экземпляр уже существует, возвращаем его
            print("Возвращён существующий Singleton-объект")
        return cls._instance  # возвращаем экземпляр (новый или уже существующий)

    def __init__(self, value):
        # __init__ инициализирует объект (но вызывается каждый раз при создании)
        self.value = value  # сохраняем значение в атрибуте объекта

# создаём первый объект
s1 = Singleton("Первый")
print("s1.value =", s1.value)

# создаём второй объект
s2 = Singleton("Второй")
print("s2.value =", s2.value)

# проверим, указывают ли s1 и s2 на один и тот же объект
print("s1 is s2:", s1 is s2)  # True — оба переменные указывают на один и тот же экземпляр
'-------------------------------------------------------------------------------------------------------'
class MathHelper:
    pi = 3.14159  # атрибут класса

    def __init__(self, radius):
        self.radius = radius  # атрибут объекта

    def area(self):
        # обычный метод: работает с конкретным объектом, доступ к self
        return MathHelper.pi * self.radius ** 2

    @classmethod
    def change_pi(cls, new_value):
        # метод класса: работает с самим классом, доступ к cls
        cls.pi = new_value  # меняем значение pi для всех объектов

    @staticmethod
    def add(a, b):
        # статический метод: не зависит ни от объекта, ни от класса
        return a + b  # просто выполняет функцию

# создаём объект
circle = MathHelper(5)

# вызываем обычный метод
print("Площадь круга:", circle.area())  # использует self и pi

# меняем значение pi с помощью classmethod
MathHelper.change_pi(3.14)
print("Новая площадь круга:", circle.area())  # пересчитает с новым pi

# вызываем staticmethod
print("Сумма 2 + 3:", MathHelper.add(2, 3))  # работает как обычная функция
'---------------------------------------------------------------------------------------------------------------'
class Person:
    def __init__(self, name, age):
        self.name = name             # public — можно обращаться напрямую (person.name)
        self._age = age              # protected — по соглашению: не трогать напрямую вне класса или подкласса
        self.__salary = 50000        # private — имя "переписывается", нельзя обратиться напрямую (person.__salary)

    # геттер для чтения приватного атрибута __salary
    def get_salary(self):
        return self.__salary

    # сеттер для изменения приватного атрибута __salary
    def set_salary(self, new_salary):
        if new_salary >= 0:
            self.__salary = new_salary
        else:
            print("Ошибка: зарплата не может быть отрицательной")

# создаём объект
person = Person("Алиса", 30)

# доступ к public
print("Имя:", person.name)  # можно напрямую

# доступ к protected (всё ещё можно, но не рекомендуется напрямую)
print("Возраст:", person._age)  # по соглашению — только внутри класса или подкласса

# доступ к private напрямую невозможен:
# print(person.__salary)  # вызовет ошибку

# доступ к private через геттер
print("Зарплата:", person.get_salary())

# изменение зарплаты через сеттер
person.set_salary(60000)
print("Новая зарплата:", person.get_salary())

# попытка установить неправильную зарплату
person.set_salary(-1000)  # покажет ошибку

# при желании всё же можно "взломать" private (не рекомендуется)
print("Хакерский доступ:", person._Person__salary)  # доступ через имя_класса__имя_атрибута
'--------------------------------------------------------------------------------------------------'
22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
class Magic:
    def __init__(self):
        # обычное присваивание через setattr (вызовет __setattr__)
        self.x = 10

    def __setattr__(self, name, value):
        # вызывается при любом присваивании атрибута
        print(f"Устанавливаем {name} = {value}")
        super().__setattr__(name, value)  # важно: используем super(), чтобы избежать бесконечной рекурсии

    def __getattribute__(self, name):
        # вызывается при любом доступе к атрибуту
        print(f"Получаем значение {name}")
        return super().__getattribute__(name)  # обращаемся к настоящему значению

    def __getattr__(self, name):
        # вызывается, если атрибут НЕ найден (после __getattribute__)
        print(f"Атрибут {name} не найден, возвращаем значение по умолчанию")
        return "Нет такого свойства"

    def __delattr__(self, name):
        # вызывается при удалении атрибута
        print(f"Удаляем атрибут {name}")
        super().__delattr__(name)  # удаляем с помощью родительского метода

# создаём объект
obj = Magic()

# присваиваем новый атрибут
obj.y = 20  # вызовет __setattr__

# получаем существующий атрибут
print(obj.x)  # вызовет __getattribute__

# обращаемся к несуществующему атрибуту
print(obj.z)  # вызовет __getattribute__, затем __getattr__

# удаляем атрибут
del obj.x  # вызовет __delattr__

# снова пробуем получить удалённый атрибут
print(obj.x)  # снова вызовет __getattribute__ и __getattr__
'---------------------------------------------------------------------------------------------------'
class MonoState:
    # Вся информация хранится в одном атрибуте класса
    _state = {}

    def __new__(cls, *args, **kwargs):
        # при создании нового объекта, возвращаем тот же самый объект, что и для всех остальных
        obj = super().__new__(cls)
        obj.__dict__ = cls._state  # указываем, что все объекты будут использовать один и тот же словарь для хранения атрибутов
        return obj

    def __setattr__(self, name, value):
        # устанавливаем атрибуты, которые будут общими для всех объектов
        self.__dict__[name] = value

    def __getattr__(self, name):
        # возвращаем атрибут, если он существует
        try:
            return self.__dict__[name]
        except KeyError:
            return None

# создаём несколько объектов
obj1 = MonoState()
obj2 = MonoState()

# присваиваем значения через один объект
obj1.name = "Объект 1"
obj1.value = 100

# значения становятся общими для всех объектов, т.к. состояние одно на всех
print(obj1.name)  # Объект 1
print(obj2.name)  # Объект 1 (MonoState паттерн — все объекты имеют одинаковые атрибуты)
print(obj2.value)  # 100

# присваиваем значения через второй объект
obj2.name = "Объект 2"

# изменения снова видны для всех объектов
print(obj1.name)  # Объект 2
print(obj2.name)  # Объект 2
'-----------------------------------------------------------------------------------------------------'
class Person:
    def __init__(self, name, age):
        self._name = name  # внутренний атрибут
        self._age = age    # внутренний атрибут

    @property
    def name(self):
        # геттер: возвращает значение атрибута _name
        return self._name

    @name.setter
    def name(self, value):
        # сеттер: позволяет изменить атрибут _name
        if len(value) > 2:  # просто проверка длины имени
            self._name = value
        else:
            print("Имя слишком короткое!")

    @property
    def age(self):
        # геттер для возраста
        return self._age

    @age.setter
    def age(self, value):
        # сеттер для возраста
        if value > 0:
            self._age = value
        else:
            print("Возраст должен быть положительным числом!")

# создаём объект
person = Person("Алиса", 30)

# доступ к свойствам через @property
print(person.name)  # Алиса
print(person.age)   # 30

# изменение значений через сеттеры
person.name = "Боб"  # имя будет изменено
print(person.name)  # Боб

person.name = "A"    # имя слишком короткое, не изменится
print(person.name)  # Боб

person.age = -5      # ошибка: возраст не может быть отрицательным
print(person.age)   # 30

person.age = 35      # возраст изменится
print(person.age)   # 35
'---------------------------------------------------------------------------------------------------'
class Rectangle:
    def __init__(self, width, height):
        self._width = width  # внутренний атрибут
        self._height = height  # внутренний атрибут

    # свойство для ширины
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            print("Ширина должна быть положительным числом!")

    # свойство для высоты
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            print("Высота должна быть положительным числом!")

    # свойство для площади
    @property
    def area(self):
        return self._width * self._height

# создаём объект
rect = Rectangle(5, 10)

# доступ к свойствам
print("Ширина:", rect.width)      # 5
print("Высота:", rect.height)     # 10
print("Площадь:", rect.area)      # 50

# изменение значений через сеттеры
rect.width = 7                    # изменяем ширину
rect.height = 12                  # изменяем высоту
print("Новая площадь:", rect.area)  # 84

# попытка установить некорректные значения
rect.width = -3                   # ошибка: ширина должна быть положительным числом
rect.height = -5                  # ошибка: высота должна быть положительным числом
'-------------------------------------------------------------------------------------------------'
class DataDescriptor:
    # дескриптор с методами __get__, __set__ и __delete__
    def __get__(self, instance, owner):
        print(f"Вызван __get__ для {instance}")
        return self._value

    def __set__(self, instance, value):
        print(f"Вызван __set__ для {instance} с значением {value}")
        self._value = value

    def __delete__(self, instance):
        print(f"Вызван __delete__ для {instance}")
        del self._value

class NonDataDescriptor:
    # дескриптор с только методом __get__
    def __get__(self, instance, owner):
        print(f"Вызван __get__ для {instance}")
        return "Значение из NonDataDescriptor"

class MyClass:
    data_descriptor = DataDescriptor()  # это data descriptor
    non_data_descriptor = NonDataDescriptor()  # это non-data descriptor

    def __init__(self, name):
        self.name = name

# создаём объект
obj = MyClass("Пример")

# доступ к data descriptor
obj.data_descriptor = 42  # вызовет __set__
print(obj.data_descriptor)  # вызовет __get__

# доступ к non-data descriptor
print(obj.non_data_descriptor)  # вызовет только __get__

# удаление data descriptor
del obj.data_descriptor  # вызовет __delete__
'---------------------------------------------------------------------------------------------------'
class Adder:
    def __init__(self, increment):
        self.increment = increment  # задаём значение для увеличения

    def __call__(self, value):
        # каждый раз при вызове объекта мы увеличиваем значение
        return value + self.increment

add_five = Adder(5)

result = add_five(10)  # добавляем 5 к 10
print(result)  # 15

def decorator(func):
    def wrapper(*args, **kwargs):
        print("До вызова функции")
        result = func(*args, **kwargs)
        print("После вызова функции")
        return result
    return wrapper

@decorator
def say_hello(name):
    print(f"Привет, {name}!")

say_hello("Аня")
'---------------------------------------------------------------------------------------------------'
class MyClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    # Магический метод __str__ для красивого строкового представления объекта
    def __str__(self):
        return f"Объект: {self.name}, Значение: {self.value}"

    # Магический метод __repr__ для подробного представления объекта (для разработчиков)
    def __repr__(self):
        return f"MyClass(name={self.name!r}, value={self.value!r})"

    # Магический метод __len__ для получения длины объекта
    def __len__(self):
        return len(self.name)

    # Магический метод __abs__ для получения абсолютного значения
    def __abs__(self):
        return abs(self.value)

# создаём объект
obj = MyClass("Пример", -42)

# выводим строковое представление с помощью __str__
print(str(obj))  # Объект: Пример, Значение: -42

# выводим подробное представление с помощью __repr__
print(repr(obj))  # MyClass(name='Пример', value=-42)

# получаем длину объекта с помощью __len__
print(len(obj))  # 6 (длина строки "Пример")

# получаем абсолютное значение с помощью __abs__
print(abs(obj))  # 42 (абсолютное значение -42)
'---------------------------------------------------------------------------------------------------'
333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
class MyNumber:
    def __init__(self, value):
        self.value = value

    # Магический метод __add__ для сложения
    def __add__(self, other):
        return MyNumber(self.value + other.value)

    # Магический метод __sub__ для вычитания
    def __sub__(self, other):
        return MyNumber(self.value - other.value)

    # Магический метод __mul__ для умножения
    def __mul__(self, other):
        return MyNumber(self.value * other.value)

    # Магический метод __truediv__ для деления
    def __truediv__(self, other):
        if other.value != 0:
            return MyNumber(self.value / other.value)
        else:
            raise ValueError("Невозможно делить на ноль!")

    # Для красивого вывода
    def __str__(self):
        return str(self.value)

# создаём два объекта
num1 = MyNumber(10)
num2 = MyNumber(5)

# сложение
result_add = num1 + num2
print(result_add)  # 15

# вычитание
result_sub = num1 - num2
print(result_sub)  # 5

# умножение
result_mul = num1 * num2
print(result_mul)  # 50

# деление
result_div = num1 / num2
print(result_div)  # 2.0

# деление на ноль
try:
    result_div_zero = num1 / MyNumber(0)
except ValueError as e:
    print(e)  # Невозможно делить на ноль!
'--------------------------------------------------------------------------------------------------'
class MyNumber:
    def __init__(self, value):
        self.value = value

    # Магический метод __eq__ для проверки равенства
    def __eq__(self, other):
        return self.value == other.value

    # Магический метод __ne__ для проверки неравенства
    def __ne__(self, other):
        return self.value != other.value

    # Магический метод __lt__ для проверки "меньше чем"
    def __lt__(self, other):
        return self.value < other.value

    # Магический метод __gt__ для проверки "больше чем"
    def __gt__(self, other):
        return self.value > other.value

    # Магический метод __le__ для проверки "меньше или равно"
    def __le__(self, other):
        return self.value <= other.value

    # Магический метод __ge__ для проверки "больше или равно"
    def __ge__(self, other):
        return self.value >= other.value

    # Для красивого вывода
    def __str__(self):
        return str(self.value)

# создаём два объекта
num1 = MyNumber(10)
num2 = MyNumber(5)

# проверка равенства
print(num1 == num2)  # False

# проверка неравенства
print(num1 != num2)  # True

# проверка "меньше чем"
print(num1 < num2)  # False

# проверка "больше чем"
print(num1 > num2)  # True

# проверка "меньше или равно"
print(num1 <= num2)  # False

# проверка "больше или равно"
print(num1 >= num2)  # True
'------------------------------------------------------------------------------------------------'
class MyClass:
    def __init__(self, value):
        self.value = value  # инициализируем объект с атрибутом value

    def __eq__(self, other):
        # Магический метод __eq__ сравнивает два объекта на равенство
        # Сравниваем значение атрибутов value объектов
        if isinstance(other, MyClass):  # проверяем, что другой объект тоже MyClass
            return self.value == other.value
        return False  # если другой объект не MyClass, возвращаем False

    def __hash__(self):
        # Магический метод __hash__ возвращает хеш-значение объекта
        # Используем хеширование на основе атрибута value
        return hash(self.value)  # hash — стандартная функция Python для хеширования

# создаём два объекта с одинаковым значением
obj1 = MyClass(42)
obj2 = MyClass(42)

# проверка на равенство
print(obj1 == obj2)  # True, потому что значения атрибутов у объектов одинаковые

# проверка хеш-значений
print(hash(obj1))  # Хеш-значение для obj1
print(hash(obj2))  # Хеш-значение для obj2

# создаём словарь, используя объекты с одинаковыми значениями
my_dict = {obj1: "Первый объект", obj2: "Второй объект"}
print(my_dict)  # словарь, где ключи obj1 и obj2 будут иметь одинаковое значение, потому что их хеши одинаковы
'--------------------------------------------------------------------------------------------------------------'
class MyClass:
    def __init__(self, value):
        self.value = value  # инициализируем объект с атрибутом value

    def __bool__(self):
        # Магический метод __bool__ определяет правдивость объекта
        # Если value больше 0, объект считается правдивым
        return self.value > 0

# создаём объекты с разными значениями
obj1 = MyClass(10)   # правдивый объект (10 > 0)
obj2 = MyClass(0)    # ложный объект (0 == 0)
obj3 = MyClass(-5)   # ложный объект (-5 < 0)

# проверка правдивости объектов
print(bool(obj1))  # True, так как 10 > 0
print(bool(obj2))  # False, так как 0 == 0
print(bool(obj3))  # False, так как -5 < 0
'-------------------------------------------------------------------------------------------'
class MyList:
    def __init__(self):
        self.items = []  # инициализация пустого списка

    def __getitem__(self, index):
        # Магический метод __getitem__ для получения элемента по индексу
        # Этот метод вызывается, когда пытаемся получить элемент с помощью obj[index]
        return self.items[index]  # возвращаем элемент по индексу

    def __setitem__(self, index, value):
        # Магический метод __setitem__ для изменения элемента по индексу
        # Этот метод вызывается, когда пытаемся присвоить значение с помощью obj[index] = value
        self.items[index] = value  # изменяем элемент по индексу

    def __delitem__(self, index):
        # Магический метод __delitem__ для удаления элемента по индексу
        # Этот метод вызывается, когда пытаемся удалить элемент с помощью del obj[index]
        del self.items[index]  # удаляем элемент по индексу

# создаём объект MyList
my_list = MyList()

# добавляем элементы
my_list.items = [10, 20, 30, 40]

# получаем элемент по индексу
print(my_list[2])  # 30, так как это элемент с индексом 2

# изменяем элемент по индексу
my_list[2] = 99  # меняем элемент с индексом 2 на 99
print(my_list[2])  # 99

# удаляем элемент по индексу
del my_list[2]  # удаляем элемент с индексом 2
print(my_list.items)  # [10, 20, 40], элемент 99 был удалён
'----------------------------------------------------------------------------------------------'
class MyRange:
    def __init__(self, start, end):
        self.start = start  # начальное значение диапазона
        self.end = end      # конечное значение диапазона
        self.current = start  # текущее значение, с которого начнём итерацию

    def __iter__(self):
        # Магический метод __iter__ возвращает итератор объекта
        # В данном случае объект сам себя является итератором, поэтому возвращаем self
        return self

    def __next__(self):
        # Магический метод __next__ возвращает следующий элемент в итерации
        if self.current < self.end:
            current_value = self.current  # сохраняем текущее значение
            self.current += 1  # увеличиваем на 1 для следующей итерации
            return current_value  # возвращаем текущее значение
        else:
            # Если достигнут конец диапазона, возбуждаем исключение StopIteration
            raise StopIteration

# создаём объект MyRange для диапазона от 1 до 5
my_range = MyRange(1, 5)

# используем объект как итератор в цикле for
for num in my_range:
    print(num)  # выведет 1, 2, 3, 4

'--------------------------------------------------------------------------------------------------'
# Базовый класс Animal
class Animal:
    def __init__(self, name):
        self.name = name  # атрибут name для хранения имени животного

    def speak(self):
        # метод speak, который будет переопределён в подклассах
        raise NotImplementedError("Этот метод должен быть переопределён в подклассе")

# Подкласс Dog, наследует от Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # вызываем конструктор родительского класса для инициализации name
        self.breed = breed  # добавляем атрибут breed для породы собаки

    def speak(self):
        # переопределяем метод speak для собаки
        return f"{self.name} говорит: Гав!"  # поведение для собаки

# Подкласс Cat, наследует от Animal
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # вызываем конструктор родительского класса для инициализации name
        self.color = color  # добавляем атрибут color для цвета кошки

    def speak(self):
        # переопределяем метод speak для кошки
        return f"{self.name} говорит: Мяу!"  # поведение для кошки

# создаём объекты подклассов
dog = Dog("Шерлок", "Бульдог")  # создаём объект класса Dog
cat = Cat("Мурка", "Чёрный")  # создаём объект класса Cat

# вызываем метод speak у объектов
print(dog.speak())  # Шерлок говорит: Гав!
print(cat.speak())  # Мурка говорит: Мяу!
'-------------------------------------------------------------------------------------------'
4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
# Пример использования функции issubclass() и наследования от встроенных типов и от object

# Базовый класс Animal
class Animal:
    def __init__(self, name):
        self.name = name  # атрибут name для хранения имени животного

    def speak(self):
        # метод speak, который будет переопределён в подклассах
        raise NotImplementedError("Этот метод должен быть переопределён в подклассе")

# Подкласс Dog, наследует от Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # вызываем конструктор родительского класса для инициализации name
        self.breed = breed  # добавляем атрибут breed для породы собаки

    def speak(self):
        return f"{self.name} говорит: Гав!"  # поведение для собаки

# Подкласс Cat, наследует от Animal
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # вызываем конструктор родительского класса для инициализации name
        self.color = color  # добавляем атрибут color для цвета кошки

    def speak(self):
        return f"{self.name} говорит: Мяу!"  # поведение для кошки

# Пример наследования от встроенных типов
class MyList(list):
    # Наследуем от встроенного типа list и добавляем новый метод
    def first_element(self):
        return self[0] if self else None  # возвращаем первый элемент списка или None

# Используем функцию issubclass()
print(issubclass(Dog, Animal))  # True, Dog является подклассом Animal
print(issubclass(Cat, Animal))  # True, Cat является подклассом Animal
print(issubclass(MyList, list))  # True, MyList является подклассом list
print(issubclass(Dog, object))  # True, Dog является подклассом object (по умолчанию)

# Создаём объекты
dog = Dog("Шерлок", "Бульдог")
cat = Cat("Мурка", "Чёрный")
my_list = MyList([1, 2, 3])

# Проверка типа объектов
print(isinstance(dog, Dog))  # True, dog является экземпляром Dog
print(isinstance(dog, Animal))  # True, dog также является экземпляром Animal
print(isinstance(my_list, list))  # True, my_list является экземпляром list
print(isinstance(my_list, MyList))  # True, my_list является экземпляром MyList
'---------------------------------------------------------------------------------------------------'
# Базовый класс Animal
class Animal:
    def __init__(self, name):
        self.name = name  # атрибут name для хранения имени животного

    def speak(self):
        # метод speak, который будет переопределён в подклассах
        return f"{self.name} издает звук!"

# Подкласс Dog, наследует от Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # вызываем конструктор родительского класса для инициализации name
        self.breed = breed  # добавляем атрибут breed для породы собаки

    def speak(self):
        # переопределяем метод speak для собаки
        return f"{self.name} говорит: Гав!"

# Подкласс GuardDog, наследует от Dog
class GuardDog(Dog):
    def __init__(self, name, breed, guard_level):
        super().__init__(name, breed)  # вызываем конструктор родительского класса Dog
        self.guard_level = guard_level  # добавляем атрибут guard_level для уровня охраны

    def speak(self):
        # переопределяем метод speak для охранной собаки
        base_speak = super().speak()  # вызываем speak() родительского класса Dog
        return f"{base_speak} (но он защищает!)"  # добавляем дополнительное поведение

# Создаём объект GuardDog
guard_dog = GuardDog("Шерлок", "Бульдог", 5)

# Вызываем метод speak
print(guard_dog.speak())  # Шерлок говорит: Гав! (но он защищает!)

# Пример делегирования через super() в другом контексте
class Person:
    def __init__(self, name):
        self.name = name  # атрибут name для хранения имени человека

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)  # вызываем конструктор родительского класса Person
        self.salary = salary  # добавляем атрибут salary для зарплаты

    def details(self):
        # Метод для вывода информации о сотруднике
        return f"{self.name} работает за {self.salary} в месяц."

# Создаём объект Employee
employee = Employee("Иван", 50000)

# Вызываем метод details
print(employee.details())  # Иван работает за 50000 в месяц.
'-------------------------------------------------------------------------------------------------'
# Базовый класс Animal
class Animal:
    def __init__(self, name):
        self.__name = name  # private атрибут __name, доступный только внутри класса
        self._type = "Животное"  # protected атрибут _type, доступный внутри класса и подклассов

    def get_name(self):
        # Геттер для доступа к private атрибуту __name
        return self.__name

    def speak(self):
        return f"{self.__name} издает звук!"  # метод, который будет переопределен в подклассах

# Подкласс Dog, наследует от Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # вызов конструктора родительского класса для инициализации __name
        self.breed = breed  # атрибут для породы собаки

    def speak(self):
        return f"{self.get_name()} говорит: Гав!"  # используем геттер для доступа к private атрибуту __name

    def get_type(self):
        return self._type  # доступ к protected атрибуту _type

# Создание объекта Dog
dog = Dog("Шерлок", "Бульдог")

# Доступ к атрибутам
# print(dog.__name)  # Ошибка! Невозможно получить доступ к __name, так как это private атрибут
print(dog.get_name())  # "Шерлок", доступ через геттер
print(dog.get_type())  # "Животное", доступ к protected атрибуту
'-----------------------------------------------------------------------------------------------------'
from abc import ABC, abstractmethod  # Импортируем модуль для абстрактных классов

# Абстрактный класс Animal
class Animal(ABC):
    def __init__(self, name):
        self.name = name  # атрибут name для хранения имени животного

    @abstractmethod
    def speak(self):
        # Абстрактный метод, который будет переопределён в подклассах
        pass

# Подкласс Dog, наследует от Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # вызываем конструктор родительского класса для инициализации name
        self.breed = breed  # добавляем атрибут breed для породы собаки

    def speak(self):
        # Переопределяем метод speak для собаки
        return f"{self.name} говорит: Гав!"

# Подкласс Cat, наследует от Animal
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # вызываем конструктор родительского класса для инициализации name
        self.color = color  # добавляем атрибут color для цвета кошки

    def speak(self):
        # Переопределяем метод speak для кошки
        return f"{self.name} говорит: Мяу!"

# Создаем объекты подклассов
dog = Dog("Шерлок", "Бульдог")
cat = Cat("Мурка", "Чёрный")

# Пример полиморфизма: один и тот же метод 'speak' ведет себя по-разному для разных объектов
animals = [dog, cat]
for animal in animals:
    print(animal.speak())  # Разные выводы в зависимости от типа объекта
'--------------------------------------------------------------------------------------------------'
# Базовый класс Animal
class Animal:
    def __init__(self, name):
        self.name = name  # атрибут name для хранения имени животного

    def speak(self):
        # Метод speak, который будет переопределён в подклассах
        return f"{self.name} издает звук!"

# Базовый класс Pet
class Pet:
    def __init__(self, owner):
        self.owner = owner  # атрибут owner для хранения владельца животного

    def play(self):
        # Метод play, который будет использоваться для всех питомцев
        return f"{self.owner} играет с {self.name}"

# Подкласс Dog, наследует от Animal и Pet
class Dog(Animal, Pet):
    def __init__(self, name, breed, owner):
        Animal.__init__(self, name)  # Инициализация через конструктор класса Animal
        Pet.__init__(self, owner)    # Инициализация через конструктор класса Pet
        self.breed = breed  # атрибут breed для породы собаки

    def speak(self):
        return f"{self.name} говорит: Гав!"  # Переопределяем метод speak для собаки

# Создаем объект Dog
dog = Dog("Шерлок", "Бульдог", "Иван")

# Вызов методов из разных классов
print(dog.speak())  # Шерлок говорит: Гав!
print(dog.play())   # Иван играет с Шерлоком
'------------------------------------------------------------------------------------------------------------'
# Пример использования __slots__

class Animal:
    # Используем __slots__, чтобы ограничить набор атрибутов
    __slots__ = ['name', 'age']  # Ограничиваем доступ к этим атрибутам

    def __init__(self, name, age):
        self.name = name  # атрибут name
        self.age = age    # атрибут age

# Создаём объект Animal
animal = Animal("Шерлок", 5)

# Доступ к атрибутам, которые указаны в __slots__
print(animal.name)  # Шерлок
print(animal.age)   # 5

# Попытка добавить новый атрибут, который не указан в __slots__
# animal.color = "Черный"  # Ошибка! Атрибут 'color' не существует, так как он не включён в __slots__
'-----------------------------------------------------------------------------------------------------------'
# Пример использования __slots__ с property и наследованием

class Animal:
    __slots__ = ['name', 'age']  # Определяем __slots__ для атрибутов

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def description(self):
        # Свойство, которое возвращает описание животного
        return f"{self.name} - {self.age} лет"

# Наследуем класс Dog от Animal
class Dog(Animal):
    __slots__ = ['breed']  # Дополняем __slots__ для класса Dog

    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Инициализируем родительский класс
        self.breed = breed  # Атрибут породы собаки

    @property
    def description(self):
        # Переопределяем описание для собаки
        return f"{self.name}, порода {self.breed}, {self.age} лет"

# Создаём объект Dog
dog = Dog("Шерлок", 5, "Бульдог")

# Используем свойство description
print(dog.description)  # Шерлок, порода Бульдог, 5 лет

# Проверяем доступ к атрибутам, ограниченным __slots__
print(dog.name)  # Шерлок
print(dog.age)   # 5
print(dog.breed)  # Бульдог

# Попытка добавить новый атрибут, который не определен в __slots__
# dog.color = "Черный"  # Ошибка! Этот атрибут не существует.
'-----------------------------------------------------------------------------------------------'
55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
# Пример обработки исключений в ООП с использованием блоков try / except

class DivisionError(Exception):
    # Создаем пользовательское исключение для деления на ноль
    pass

class Calculator:
    def divide(self, a, b):
        try:
            # Попытка деления
            if b == 0:
                raise DivisionError("На ноль делить нельзя!")  # Генерация исключения при делении на ноль
            return a / b
        except DivisionError as e:
            # Обработка исключения деления на ноль
            print(f"Ошибка: {e}")
        except Exception as e:
            # Обработка других ошибок
            print(f"Произошла ошибка: {e}")
        else:
            # Если ошибок не было
            print("Деление успешно!")
        finally:
            # Этот блок выполнится в любом случае
            print("Завершение операции деления.")

# Создаем объект калькулятора
calc = Calculator()

# Пример успешного деления
result = calc.divide(10, 2)  # 10 / 2
print("Результат деления:", result)

# Пример деления на ноль
result = calc.divide(10, 0)  # Ошибка деления на ноль
'-------------------------------------------------------------------------------------------------------'
# Пример использования блоков finally и else в ООП для обработки исключений

class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        try:
            # Открытие файла для чтения
            with open(self.filename, 'r') as file:
                content = file.read()  # Чтение содержимого файла
                print("Содержимое файла:")
                print(content)
        except FileNotFoundError as e:
            # Обработка исключения, если файл не найден
            print(f"Ошибка: Файл {self.filename} не найден!")
        except IOError as e:
            # Обработка других ошибок ввода-вывода
            print(f"Ошибка ввода/вывода: {e}")
        else:
            # Если исключений не произошло, выполняется этот блок
            print("Файл успешно прочитан.")
        finally:
            # Этот блок выполнится в любом случае
            print(f"Попытка прочтения файла {self.filename} завершена.")

# Создаём объект для работы с файлом
file_handler = FileHandler("sample.txt")

# Пример успешного чтения файла
file_handler.read_file()

# Пример с файлом, которого не существует
file_handler = FileHandler("non_existing_file.txt")
file_handler.read_file()
'---------------------------------------------------------------------------------------------------------------'
# Пример распространения исключений (propagation exceptions) в ООП

class InvalidAgeError(Exception):
    # Пользовательское исключение для некорректного возраста
    pass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, age):
        try:
            if age < 0:
                raise InvalidAgeError("Возраст не может быть отрицательным!")
            self.age = age
        except InvalidAgeError as e:
            # Исключение обрабатывается здесь, но мы решаем его распространить дальше
            print(f"Ошибка: {e}")
            raise  # Повторно генерируем исключение для его дальнейшей обработки

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # Инициализируем родительский класс
        self.grade = grade

    def set_age(self, age):
        # Переопределяем метод, но оставляем обработку исключений
        try:
            super().set_age(age)  # Вызов метода родительского класса
        except InvalidAgeError:
            # Исключение будет обработано на этом уровне, но можно сделать дополнительные действия
            print(f"{self.name} не может установить отрицательный возраст.")

# Создание объектов
person = Person("Иван", 30)
student = Student("Петя", 18, "A")

# Попытка установить некорректный возраст
try:
    person.set_age(-5)  # Генерация исключения InvalidAgeError
except InvalidAgeError as e:
    print(f"Произошла ошибка в классе Person: {e}")

# Попытка установить некорректный возраст для студента
try:
    student.set_age(-2)  # Исключение будет передано и обработано в классе Person
except InvalidAgeError as e:
    print(f"Произошла ошибка в классе Student: {e}")
'-------------------------------------------------------------------------------------------------------'
# Пример использования инструкции raise и пользовательских исключений

# Определяем пользовательское исключение
class NegativeNumberError(Exception):
    pass

class Calculator:
    def add(self, a, b):
        # Проверяем на наличие отрицательных чисел
        if a < 0 or b < 0:
            raise NegativeNumberError("Нельзя использовать отрицательные числа для сложения!")
        return a + b

    def divide(self, a, b):
        if b == 0:
            # Генерация исключения при делении на ноль
            raise ValueError("Деление на ноль невозможно!")
        return a / b

# Создаём объект калькулятора
calc = Calculator()

# Пример работы с инструкцией raise
try:
    result = calc.add(-5, 10)  # Попытка сложить отрицательное число
except NegativeNumberError as e:
    print(f"Ошибка: {e}")

try:
    result = calc.divide(10, 0)  # Попытка деления на ноль
except ValueError as e:
    print(f"Ошибка: {e}")
'------------------------------------------------------------------------------------------'
# Пример использования менеджеров контекстов и оператора with

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        # Открываем файл при входе в контекст
        self.file = open(self.filename, 'r')
        return self.file  # Возвращаем объект файла

    def __exit__(self, exc_type, exc_value, traceback):
        # Закрываем файл при выходе из контекста, независимо от того, произошла ли ошибка
        if self.file:
            self.file.close()
        # Возвращаем True, если исключение было обработано, иначе False
        return False

# Использование менеджера контекста
with FileHandler("sample.txt") as file:
    # Работа с файлом внутри блока with
    content = file.read()
    print(content)
    # Если файл не существует, возникнет ошибка, но менеджер все равно закроет файл

# В случае ошибки файл будет закрыт корректно
try:
    with FileHandler("non_existing_file.txt") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Ошибка: {e}")
'-------------------------------------------------------------------------------------------'
# Пример использования вложенных классов в Python

class OuterClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Привет, {self.name}!")

    # Вложенный класс
    class InnerClass:
        def __init__(self, value):
            self.value = value

        def display(self):
            print(f"Значение: {self.value}")

# Создаём объект внешнего класса
outer = OuterClass("Иван")

# Взаимодействие с внешним классом
outer.greet()  # Привет, Иван!

# Создаём объект вложенного класса
inner = outer.InnerClass(10)  # Вложенный класс можно создать только через внешний класс
inner.display()  # Значение: 10
'--------------------------------------------------------------------------------------------------'
# Пример использования метаклассов в Python

# Определим метакласс, который будет изменять поведение классов
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # Добавляем новый метод в класс, создаваемый метаклассом
        dct['greet'] = lambda self: f"Привет, я класс {self.__class__.__name__}!"
        return super().__new__(cls, name, bases, dct)

# Создаем класс с использованием нашего метакласса
class MyClass(metaclass=MyMeta):
    pass

# Создаем объект класса MyClass
obj = MyClass()

# Вызов метода, добавленного метаклассом
print(obj.greet())  # Привет, я класс MyClass!

# Проверяем, что MyClass использует MyMeta в качестве метакласса
print(isinstance(MyClass, type))  # True, MyClass - это тип, созданный MyMeta
print(isinstance(MyClass, MyMeta))  # True, MyClass использует MyMeta как метакласс
'----------------------------------------------------------------------------------------------------'
# Пример использования пользовательских метаклассов с параметром metaclass

# Определим пользовательский метакласс, который будет проверять наличие метода 'say_hello'
class HelloMeta(type):
    def __new__(cls, name, bases, dct):
        # Проверка, есть ли в классе метод 'say_hello'
        if 'say_hello' not in dct:
            raise TypeError(f"Класс {name} должен содержать метод 'say_hello'.")
        return super().__new__(cls, name, bases, dct)

# Класс с метаклассом HelloMeta
class MyClassWithHello(metaclass=HelloMeta):
    def say_hello(self):
        return "Привет, мир!"

# Класс без метода say_hello, который вызовет исключение
class MyClassWithoutHello(metaclass=HelloMeta):
    pass  # Здесь нет метода 'say_hello'

# Создание объекта первого класса
obj1 = MyClassWithHello()
print(obj1.say_hello())  # Привет, мир!

# Попытка создать объект второго класса вызовет исключение
try:
    obj2 = MyClassWithoutHello()  # Это вызовет ошибку TypeError
except TypeError as e:
    print(f"Ошибка: {e}")
'---------------------------------------------------------------------------------------------------'
from django.db import models

# Пример пользовательского метакласса
class CustomMeta(type):
    def __new__(cls, name, bases, dct):
        # Добавление дополнительного атрибута "custom_attribute" во все модели
        dct['custom_attribute'] = "This is a custom attribute"
        return super().__new__(cls, name, bases, dct)

# Создание модели с пользовательским метаклассом
class MyModel(models.Model, metaclass=CustomMeta):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name}, {self.age}"

# Проверка работы метакласса
# Модель будет содержать "custom_attribute"
print(MyModel.custom_attribute)  # This is a custom attribute
'--------------------------------------------------------------------------------------------------'
# Введение в Python Data Classes (часть 1)

# Импортируем декоратор для создания Data Class
from dataclasses import dataclass

# Определяем простой Data Class
@dataclass
class Person:
    name: str  # Атрибут name, строка
    age: int   # Атрибут age, целое число

# Создаем объект класса
person1 = Person("Alice", 30)

# Выводим объект, используя автоматически сгенерированное строковое представление __repr__
print(person1)  # Person(name='Alice', age=30)

# Введение в Python Data Classes (часть 2)

# Дополнительные параметры для @dataclass
from dataclasses import dataclass

# Data Class с параметром order=True, который позволяет использовать операторы сравнения
@dataclass(order=True)
class Product:
    name: str  # Атрибут name, строка
    price: float  # Атрибут price, число с плавающей запятой

# Создаем два объекта класса Product
product1 = Product("Laptop", 1000.0)
product2 = Product("Phone", 500.0)

# Сравниваем объекты с использованием оператора >
print(product1 > product2)  # True, так как цена у ноутбука больше

# Используем параметр frozen=True, чтобы сделать объекты неизменяемыми
@dataclass(frozen=True)
class ImmutableProduct:
    name: str
    price: float

# Создаем объект и пытаемся изменить атрибут (это вызовет ошибку)
immutable_product = ImmutableProduct("Tablet", 300.0)
try:
    immutable_product.price = 350.0  # Ошибка: нельзя изменить значение атрибута
except AttributeError as e:
    print(f"Ошибка: {e}")  # Ошибка: can't set attribute
'---------------------------------------------------------------------------------------------------'
# Python Data Classes при наследовании

# Импортируем декоратор для создания Data Class
from dataclasses import dataclass

# Базовый класс Data Class
@dataclass
class Animal:
    name: str  # Атрибут name, строка
    age: int   # Атрибут age, целое число

# Наследуем от базового класса Animal
@dataclass
class Dog(Animal):
    breed: str  # Атрибут breed, строка, для породы собаки

# Создаем объект класса Dog
dog = Dog("Buddy", 5, "Golden Retriever")

# Строковое представление объекта (сгенерированное автоматически)
print(dog)  # Dog(name='Buddy', age=5, breed='Golden Retriever')

# Python Data Classes при наследовании с параметром init=False

# Базовый класс Data Class
@dataclass
class Animal:
    name: str
    age: int

# Наследуем от Animal и отключаем создание __init__ для потомка
@dataclass
class Cat(Animal):
    breed: str
    age: int = 0  # Переопределяем атрибут age, делаем его по умолчанию равным 0

    # __init__ автоматически не создается, так как init=False

# Создаем объект класса Cat, передавая только имя и породу
cat = Cat("Whiskers", "Siamese")

# Строковое представление объекта
print(cat)  # Cat(name='Whiskers', age=0, breed='Siamese')