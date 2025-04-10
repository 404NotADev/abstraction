'=================================Association========================================'
#ассоциация это принцип ООП, в котором два класса связаны друг с другом

'композиция' #- это сильная связ
'агрегация' # - это слабая связ

class Battery:
    _power = 100

    def charge(self):
        if self._power < 100:
            self._power = 100

class Iphone:
    def __init__(self,color):
        self.color = color
        self.battery = Battery()



class Nokia:
    def __init__(self,color,battery):
        self.color = color
        self.battery = battery


#композиция
iphone = Iphone('black')
# del iphone

#агрегация
battery_for_nokia = Battery()
nokia = Nokia('red',battery_for_nokia)
# del nokia

iphone.battery._power = 50
iphone.battery.charge()
print(iphone.battery._power)


nokia.battery._power = 50
nokia.battery.charge()
print(nokia.battery._power)