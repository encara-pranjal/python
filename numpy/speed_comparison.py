import time 

import numpy as np

size= 10000000

list_1= list(range(size))
list_2= list(range(size))

start= time.time()

result=[]
for i in range(len(list_1)):
    result.append(list_1[i]+ list_2[i])


     
print(result) 
end= time.time()

print("list addition",end-start)

arr1 =np.array(list_1)
arr2 =np.array(list_2)

start= time.time()
result= arr1+ arr2
end=time.time()
print("array calculation:",end-start)

