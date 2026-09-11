a =[1,2,3,4]
b = [5,6,7,8,9]
c=a+b
print(c)

result = []

for i in range(len(a)):
    result.append(a[i]+b[i])

    print("list")
    print()

import numpy as np

arr1 =np.array([1,2,3,4])
arr2 =np.array([5,6,7,8,])

arr3 = arr1 + arr2
print(arr3)