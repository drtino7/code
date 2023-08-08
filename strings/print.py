integ = 7
strin = "hello"
flo = 1.2


def not_good_way():
    '''
bad way to print(not modern)

    '''
    print("the number is %d and the strin is %s and the float %.2f"  %  (integ, strin, flo))


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
