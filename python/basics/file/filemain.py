def main():
    file = '/root/code/class.py'
    list(file)
    fileadd()



def list(file):
    f=open(file, 'r')
    data = f.readlines()
    print('----------------------')
    
    
    for lines in data:
        if not(lines[0] == '#'):
          print(lines)  


def fileadd():
    f = open('test.py', 'w')
    f.write('a = 5 \nb = 7\nc = a+ b \nprint(c)')












if __name__ == '__main__':
    main()




