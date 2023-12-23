
from operations import addition , substraction


def comments():
    #import sys
    #sys.path.append('/home/drtino/modules')
   
   #from operations import *

    #dir() show a list of functions
    #print(dir(addition))

    #print(globals())info of file   (clasees and functions)
    #a=5
    #globals()['a'] = 7

    #locals() show info of the local function or class
    #def hi():
    #   print("hi")
    #   print(locals())
    pass

def main():
    print(addition.addition(1,4))
    print(substraction.substraction(1,4))
    

if __name__ == '__main__':
    main()