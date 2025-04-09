'======================================1======================================='
class Document:
    def __init__(self,file):
        self.file = file 


    def print_info(self):
        print(self.file)

class PDFdocument(Document):
    def __init__(self, file):
        super().__init__(file)

    def print_info(self):
        return super().print_info()

class WordDocument(Document):
    def __init__(self, file):
        super().__init__(file)
    
    def print_info(self):
        return super().print_info()
    
pdf = PDFdocument("document1.pdf")
pdf.print_info()

word = WordDocument("document2.docx")
word.print_info() 
'======================================2======================================='
print('.\n.\n.\n')
'=============================================================================='
class Animal:
    def __init__(self,voice,animal):
        self.voice = voice
        self.animal = animal
 
    def make_sound(self):
        print(f'{self.animal} говорит {self.voice}')

class Dog(Animal):
    def __init__(self):
        super().__init__('Собака','гавгавгвквкв')
    
    def make_animal_talk(self):
        self.make_sound()

class Cat(Animal):
    def __init__(self):
        super().__init__('кошка', 'мяууауауауау')
    
    def make_animal_talk(self):
        self.make_sound()

class Cow(Animal):
    def __init__(self):
        super().__init__('корова', 'муууууууооооо')
    
    def make_animal_talk(self):
        self.make_sound()

dog = Dog()
dog.make_animal_talk()  

cat = Cat()
cat.make_animal_talk()

cow = Cow()
cow.make_animal_talk()
'======================================3======================================='
print('.\n.\n.\n')
'=============================================================================='
class Toy:
    def __init__(self, sounds):
        self.sounds = sounds  

    def play_sound(self):
        print(self.sounds) 


class Car(Toy):
    def __init__(self):
        super().__init__('Car: врумтратата-врумтратата')  

    def sound(self):
        self.play_sound()  

class Doll(Toy):
    def __init__(self):
        super().__init__('Doll: MOTHER')

    def sound(self):
        self.play_sound()

class Drum(Toy):
    def __init__(self):
        super().__init__('Drum: Ba-dum-tsssssss ')

    def sound(self):
        self.play_sound()

car = Car()
car.sound()  

doll = Doll()
doll.sound()

drum = Drum()
drum.sound()
'======================================4======================================='
print('.\n.\n.\n')
'=============================================================================='
import math

class Shape:
    '''Я не понимаю зачем здесь  area '''
    def area(self):
        ...

    def __str__(self):
        return f"Фигура с площадью {self.area():.2f}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Круг с радиусом {self.radius} и площадью {self.area():.2f}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Прямоугольник с шириной {self.width} и высотой {self.height} и площадью {self.area():.2f}"

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Треугольник с основанием {self.base} и высотой {self.height} и площадью {self.area():.2f}"

c1 = Circle(5)  
print(c1)

r1 = Rectangle(4, 6)  
print(r1)

t1 = Triangle(3, 4)    
print(t1)


'======================================5======================================='
print('.\n.\n.\n')
'=============================================================================='
class Card:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств")
        else:
            self.balance -= amount
            print(f"Снято {amount}. Остаток: {self.balance}")

class CreditCard(Card):
    def __init__(self, balance, credit_limit):
        super().__init__(balance)
        self.credit_limit = credit_limit

    def withdraw(self, amount):
        if amount > self.balance + self.credit_limit:
            print("Превышен лимит.")
        else:
            self.balance -= amount
            print(f"Снято {amount}. Остаток: {self.balance}")

class DebitCard(Card):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств")
        else:
            self.balance -= amount
            print(f"Снято {amount}. Остаток: {self.balance}")


credit_card = CreditCard(1000, 500)
debit_card = DebitCard(1000)

credit_card.withdraw(1200)
debit_card.withdraw(1200)
debit_card.withdraw(800)