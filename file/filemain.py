def main():
    file = '/root/code/class.py'
    list(file)




def list(file):
    f=open(file, 'r')
    line = f.readlines()
    y = 0
    x = len(line)
    print('----------------------')
    
    while(y <= x ):
        line = f.readlines(y)
        print(line)
        y = y + 1




if __name__ == '__main__':
    main()




