def main():
    pass

    def square(x):
        return x*x
    
    def add(x,y):
        return x+y

    def odd(x):
        if(x%2==0):
            return True
        else:
            return false

    from functools import reduce  # for reduce
    result = reduce(add, [1,2,3,4,5] )
    result = filter(odd, [1,2,3,4,5] )
    result = map(square, [1,2,3,4,5] )
    


    ls=["valen", "juan"]
    age = [15, 17]
    zip(ls,age)
    

    ls=[1 == 1, 2 == 7]
    result = any(ls)
    result = all(ls)


    a = 5.5
    b = 5.4
    c = 5.6

    round(a)
    round(b)
    round(c)

    ls = [4,7,1]
    min(ls)

    result = pow(2,7)


    ls = ["c", "a"]
    result = sorted(ls)



    from getpass import getpass

    pasword=getpass("type your password: ")


if(__name__==__main__):
    main()
