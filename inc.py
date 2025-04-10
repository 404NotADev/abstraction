'inkapsulyaciya princip OOP'
#1 eto sokrytie dannyh 
'==============================Encapsulation================================'
# Инкапсуляция - это принцип ООП

# сокрытие данных
# связь методов с аттрибутами (в одном классе мы закладываем одну логику)

# Виды сокрытия данных 
# 1. public(публичный) 
# 2. protected(защищенный) _
# 3. private(приватный) __

class A:
    attrs = 'public'
    _attrs = 'protected'
    __attrs = 'private'

    def __init__(self, login, email, password):
        self.login = login 
        self._email = email 
        self.__password = password

    def method(self):
        return 1

    def _method(self):
        return 2

    def __method(self):
        return 3

obj = A('katana', 'tlbkvs@gmail.com', '205221')

# print(obj.attrs)
# print(obj._attrs)
# print(obj._A__attrs)

# print(obj.method())
# print(obj._method())
# print(obj._A__method())

# print(A.__dict__)
# print(obj.__dict__)


'======================Getter, Setter===================='
# getter/setter - это функции при помощи которых мы можем доставать\изменять аттрибуты

# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self.__age = age 

#     def get_name(self):
#         return self._name 
    
#     def get_age(self):
#         return self.__age
    
#     def set_name(self, name):
#         self._name = name 

#     def set_age(self, age):
#         self.__age = age 

    
# obj = Person('katana', 21)
# print(obj.get_name())
# print(obj.get_age())

# obj.set_name('nick')
# obj.set_age(20)

# print(obj.get_name())
# print(obj.get_age())



class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age 

    # property - позволяет обращаться к методам как к аттрибутам (внтури проперти работает геттер)
    @property
    def age(self):
        return self.__age

    # getter - позволяет доставать значение аттрибута
    # @age.getter
    # def age(self):
    #     return self.__age 
    
    # setter - позволяет менять значение аттрибута
    @age.setter
    def age(self, age):
        self.__age = age

obj = Person('katana', 21)
print(obj.age)
obj.age = 23
print(obj.age)

