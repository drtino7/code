name=input("type your name;")

a=input("type a number: ")
b=input("type a number: ")

def function(name):
    print("your name is: "+name)    

function(name)

#------#



print("-------------------------")
def math_operations(a,b):
    def addidion(a,b):
        print(a+b)
    def substraction(a b):
        print(a-b)
    
    addition(a,b)
    substraction(a,b


                 )
math_operations(a,b)



#--------#





print("------------------------")
def global_variables():
 ##we can use global variables(like name) and change it
 global name
 name =input("type your friend's name:")
 print("your friend's name is: "+name)
global_variables() 






#--------#






##default parameters
print("-------------------------")
def addition(a,b=2,c=7):
    ##now if i call the function with only one parameter it will add 7 to the number which i type

    ##only the lastest arguments can be optionals
    print(a+b)
addition(a,c=5)







#-------#







# *args        /         **kwargs

print('-----------------------')


fruit = ('apple','banaba')

def my_list(*args):
    print(args)

    for i,j in zip(args,fruit):
        if i == j:
            print("is a fruit")

my_list('rice','apple')

#it create a list with unlimited parameters

def my_dictionary(**kwargs):
    print(kwargs)
    
    for key,value in kwargs.items():
        if key == 'car' and value == 'red':
            print("the car is red")

my_dictionary(car='red',juan='tall')




