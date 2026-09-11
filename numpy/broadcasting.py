import numpy as np

arr_1d= np.array([10,20,30])
arr_2d=np.array([
[10,20,30],
[40,50,60],
[70,80,90],
])

print(arr_1d+arr_2d)
print(arr_1d.shape)
print(arr_2d.shape)

#broadcasting
#[10,20,30]
#[10,20,30]
#[10,20,30]
 