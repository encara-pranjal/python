import numpy as np
arr_2= np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90],
    [55,44,85],
]) 
print(np.sum(arr_2,axis=0)) #column wise
print(np.sum(arr_2,axis=1)) #row wise

print(np.mean(arr_2))
print(np.max(arr_2))
print(np.min(arr_2))