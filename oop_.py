'======================================================OOP================================================='
"""                       Object - Object-orientated programming                                        """

# class = это шаблоны
# Objectу(instance,экземпляр) -  это конечный продукт класса

class Person:
    #peremennye vnutri klassa "obekta - atributy"
    arms = 2
    legs = 2
    
    def __init__(self,name,age,prof):
        # __init__  - metod , kotoraya budet dobavlyat v obekt te otributy kotorye u vseh obektov raznye.
        # self. eto ssylka na obekt, kotoryi tolko chto sozdalsya
        self.name = name
        self.age = age
        self.prof = prof 


    #funkcii vnutri klassa 'obekty' metody
    def walk(self):
        print(f'{self.name} hodit')

    
    def swim(self):
        print(f'{self.name} plavaet')


obj1 = Person('Katana',21,'dev')
obj2 = Person('Nikita',21,'dev')
obj3 = Person('Laura',20,'senior dev')


obj1.walk()
obj1.swim()
obj2.swim()


print([obj1.name])
print([obj2.age])
print([obj3.name])


class calc:
    def add(self,a,b):
        return a+b
    def div(self, a,b):
        return a/b
    def mult(self,a,b):
        return a*b
    def minus(self,a,b):
        return a-b


Calc = calc()
print(Calc.add(4, 5))
print(Calc.div(10,5))
print(Calc.mult(4,5))
print(Calc.minus(10,5))