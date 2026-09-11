import numpy as np

arr_a= np.array([1,2,3])
arr_b=np.array([
[10],[20],[30],])

print(arr_a.shape)
print(arr_b.shape) 

print(arr_b+arr_a)


# python method (vectorising method will not be used)
arr_a= np.array([1,2,3])
arr_b=np.array([
[10],[20],[30],])

result = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(arr_b[i][0]+ arr_a[j])
        result.append(row)