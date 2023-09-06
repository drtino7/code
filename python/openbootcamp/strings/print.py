integ = 7
strin = "hello"
flo = 1.2


def not_good_way():
    '''
bad way to print(not modern)        #the .1 in %.1f mens that we usae only one decimal after the comma

    '''
    print("the number is %d and the strin is %s and the float %.1f"  %  (integ, strin, flo))


def format():
    '''
we use the format to replace
    '''

    print("the int is {integer} and the str is{strin} and the float {floa}"
          
          .format(integer=integ, strin = strin, floa= flo )
          
          )
    

def modern_way():
    '''
the modern way and we use (f''), also it's python code so you can call function or for ex the upper

    '''

    print(f'the number is {integ} and the str is {strin.upper()} and the float {flo}')
#------------------------------------------------------------------------------------------#

# __str__ human reperentation of a class
#__repr__ depuration code

#ex:

class toy:

    def __init__(self,name,price):
        self.name = name
        self.price = price
    
toy1 = toy("juan",1.50)
print(toy1)
print(repr(toy1))

class toyy:
   
    def __init__(self,name,price):
        self.name = name
        self.price = price


    def __str__(self):
        return f'the name is {self.name} and the price is {self.price}'



    def __repr__(self):
        return f'toy2 ({self.name},{self.price})'



toy2 = toyy("juan",1.50)
print(toy2)
print(repr(toy2))

string = "hello, my name Is vAlentino"

#capitalize()  firts letter mayus and all in min

print(string.capitalize())

#title()  al first letters mayus

print(string.title())

#count() how many is x in y

print(string.count('a'))

#lower() all in min

#upper() all in mayus

print(string.lower().count('a'))


#isdigit() 
print(string.isdigit())



