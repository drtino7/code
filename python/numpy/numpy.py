import numpy as np

my_array = np.array([1,2,3,4,5,6,7,8])
my_matriz = np.array([1,2,3],[4,5,6])
my_matrix = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
my_4d = mp.array([1,2,3,4,5],ndim=3)

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

arr=np.array([1,2,3])
arrc=arr.copy()#if we chang arr in the future arrc wont change
arrv=arr.view()#if we change arr in the futere arrv will show it

arr1=[1,2,3]
arr2=[1,2,3]
arradd= np.add(arr1,arr2)
arrsubstract = np.substract(arr1,arr2)
arrmyultyply = np.multyply(arr1,arr2)
arrdivide = np.divide(arr1,arr2)

arr=[0.5789,-7,-9]
print(np.absolute(arr))
print(np.trunc(arr))
print(np.around(arr))
print(np.floor(arr))
print(np.ceil(arr))

'''
log2(x): Returns the base-2 logarithm of x.
log10(x): Returns the base-10 logarithm of x.
log(x): Returns the natural logarithm of x.
cumsum(a, axis=None): Returns the cumulative sum of the elements along a given axis of array a.
prod(a, axis=None): Returns the product of the elements along a given axis of array a.
cumprod(a, axis=None): Returns the cumulative product of the elements along a given axis of array a.
diff(a, n=1, axis=-1): Returns the n-th discrete difference along a given axis of array a.
lcm(x, y): Returns the least common multiple of x and y.
gcd(x, y): Returns the greatest common divisor of x and y.
sin(x): Returns the sine of x, where x is in radians.
cos(x): Returns the cosine of x, where x is in radians.
tan(x): Returns the tangent of x, where x is in radians.
deg2rad(x): Converts x from degrees to radians.
rad2deg(x): Converts x from radians to degrees.
arcsin(x): Returns the inverse sine of x, in radians.
arccos(x): Returns the inverse cosine of x, in radians.
arctan(x): Returns the inverse tangent of x, in radians.
sinh(x): Returns the hyperbolic sine of x.
cosh(x): Returns the hyperbolic cosine of x.
tanh(x): Returns the hyperbolic tangent of x.
unique(a, return_index=False, return_inverse=False, return_counts=False, axis=None): Returns the sorted unique elements of array a, optionally along a specified axis, and optionally with additional information.
'''