import numpy as np

arr_1= np.array([1,2,3,4])

print(arr_1.shape)

arr_2= np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90],
    [55,44,85],
]) 

print(arr_2.shape) #gives shape of array

print(arr_1.ndim) #gives dimensions of array
print(arr_2.ndim)

print(arr_1.size)# gives no of elements
print(arr_2.size)

print(arr_1.dtype)
print(arr_2.dtype)