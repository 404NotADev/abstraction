'==============Polymorphism====================='
# polymorphism - is princip OOP where in same class method named similar but realisation different (one interface diferent functions )


class Dog:
    def voice(self):
        print('gav-gav')

class Cat:
    def voice(self):
        print('mew-mew')

class Duck:
    def voice(sel):
        print('crack-crack')

objects = [Dog(),Cat(),Duck(),Cat()]




for i in objects:
    i.voice()


#dict
#list
#10+5
#'hello'+'world'
#[1,2,3]+[5,6,7]
#str
#add
#pop