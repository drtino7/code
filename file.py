##open a file
import os


print(os.getcwd())

f=open('/root/code/class.py' , 'r')

data = f.read('''50''')  ## add a number of characters

print(data)


#   'r'   read

#   'w'   write

#   'a'   append

#   'x'  create





#   't'   text


#   'b'  binary




#    '+'  reading and writting




