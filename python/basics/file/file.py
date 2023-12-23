##open a file
import os


print(os.getcwd())## where am i

f=open('/root/code/class.py' , 'r')

data = f.read()  ## add a number of characters

print(data)


#   'r'   read

#   'w'   write

#   'a'   append

#   'x'  create





#   't'   text


#   'b'  binary




#    '+'  reading and writting








#readlines(number of line )

f = open('/root/code/class.py' ,'r')

data = f.readlines(7)


print(data)














