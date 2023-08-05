
#import sys
#from operations import *
from operations import addition , substraction
#sys.path.append('/home/drtino/modules')

#import sayhi

#dir() show a list of functions
print(dir(addition))


def main():
    print(addition.addition(1,4))
    print(substraction.substraction(1,4))


if __name__ == '__main__':
    main()