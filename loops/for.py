my_list = [1,2,3,4,5]
for a in my_list:
    print(a)
    if a==5:
        print("the list ended")

##for dicionary is needed 2 values for ex:
dictionary ={'valentino':15,'juan':27}
for b in dictionary:
    print(dictionary[b])

for c, v in dictionary.items():
    print('Clave:', c, ', Valor:', v)


##in range()

##Inicio: es el valor inicial de la secuencia (0 si no se especifica).

##Fin: es el valor final de la secuencia, el cual no se incluye en el resultado

##Paso: indica el incremento entre elementos de la secuencia (1 si no se especifica).


for i in range(1,10,2):
    print(i)


##break

for j in range(1,10,1):
    if j==7:
        break
    print(j)

##continue

for k in range(1,10,1):
    if k % 2 == 0:
        continue
    print(k)














