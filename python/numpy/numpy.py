import numpy as np

my_array = np.array([1,2,3,4,5,6,7,8])
my_matriz = np.array([1,2,3],[4,5,6])
my_matrix = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(my_matrix.ndim)
print(my_array[0:2])

print(np.shape(my_array))
print(np.shape(my_matriz))

my_array_reshaped = my_array.reshape(4,2)
print(my_array_reshaped)

arr1 = np.array([1,2,3])
arr2 = np.array([1,2,3])

arr = np.concatenate((arr1,arr2))

print(arr)

arr1 = np.array([1,2],[3,4])
arr2 = np.array([5,6],[7,8])

arr = np.concatenate((arr1,arr2),axis=0)
arr_4item = np.concatenate((arr1,arr2),axis=1)

newarr = np.array_split(my_array,4)
print(newarr)

arr = np.array([1,2,7,5,7])
x=np.where(arr <= 7)

arr = np.array([3,0,2,1])
arr = np.sort(arr)
