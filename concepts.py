'============================principy OOP====================='
#nasledovanie
#inkapculyaciya
#polimorfizm
#abstrakciya
#associaciya (agregaciya,kompoziciya)


"===========================nasledovanie======================="
#nasledovanie - princip OOP v kotorom my mojem unasledovat, pereopredelit i ispolzovat' dochernem klasse vse atributy i metody roditelskogo klassa



class A:
    var = 'a'

    def method(self):
        print('метод в классе A')


obj_a = A()
obj_a.method()  # метод в классе A


class B(A):
    var = 'b'
    pass


obj_b = B()  # Создаем объект B
obj_b.method()  # метод в классе A (наследуется от A)


class C(A):
    var = 'c'

    def method(self):
        return 'метод класса C'


obj_c = C()  # Создаем объект C
print(obj_c.method())  # метод класса C



class Animal():
    price = 100000

    def voice(self):
        return 'zvuki jivotnyh'

class Dog(Animal):
    def voice(self):
        return 'gav-gav'

class Cat(Animal):
    def voice(self):
        return 'mew-mew'

class Duck(Animal):
    def voice(sel):
        return 'crack-crack'

Animal.price = 2000000
Cat.price = 200001

Bobik = Dog()
Barsik = Cat()
Donald = Duck()


print(f'Bobik stroi {Bobik.price} som, on umeet {Bobik.voice()}')
print(f'Bobik stroi {Barsik.price} som, on umeet {Barsik.voice()}')
print(f'Bobik stroi {Donald.price} som, on umeet {Donald.voice()}')

#odinochnoe nasledovanie(1 rod - 1 doch)
class A:
    ...
class B(A):
    ...

'---------------------------------------------------------'
# ierhicheskaya nasledovaniya (1rod i mnogo doch)
class A:
        ...
class B(A):
        ...
class C(A):
        ...
class D(A):
        ...
'----------------------------------------------------------'
#mnojestvennoe nasledovanie (mnogo roditelei na docherni class)
class A:
        var = 'a'
        ...
class B():
        ...
class C(A,B):
        ...
class D(A,B):
        ...

obj = C()
print(obj.var)
'-------------------------------------------------------------'
#mnogourovnevaya kogda idet cepochkoi (doch-rod vniz po lestnice)
class A:
        ...
class B(A):
        ...
class C(B):
        ...
class D(C):
        ...
'----------------------------------------------------------------'
#gibridnoe nasledovanie(smes vidov)
class A:
        ...
class B(A):
        ...
class C(A):
        ...
class E:
      ...
class D(C,E):
      ...

class A:
    attr = 12

    
class B(A):
    def func(self):
        return super().attr ** 2
    

obj = B()
print(obj.func())


__dict__ 

object