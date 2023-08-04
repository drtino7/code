class car:
    def __init__(self):
        self.off=True
    doors = 4
#if the funtion is called with _ we dont have to change it outside the class
    def on(self):
        self.off = False
    #the self. is for referer to the functionon the class

lambo = car()
lambo.on()  

print(lambo.doors)

class static:
    number = 1

    def addition():
        static.number +=1

static.addition()
print(static.number)

del(static)
#inheritance
class truck(car):
    def __init__(self):
        super().__init__() ##call the constructor from the base class
    trunk = 24 #CM

truck1 = truck()

print(truck1.off)

#print(dir(truck1)) #show metods and properties



class constructor:

    #constructor
    def __init__(self,name):
        pass

    def func(self):
        a = 5
 #desconstructor
    def __del__(self):
        pass
       #func del() to use when you want 
cons = constructor("juan")
del(cons)

#abstarct

from abc import ABC,abstractmethod

class animal:
    @abstractmethod
    def sound(self):
        print("sound")


class dog(animal):
   def __init__(self):
        def sound(self):
            print("guau")
        sound()

caniche = dog()