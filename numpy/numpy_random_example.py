import numpy as np

print(np.random.rand(10))# all no. will be between 0 to 1

print(np.random.rand(3,4))      

print(np.random.randn(10)) 

print(np.random.randn(3,4)) 

print(np.random.randint(0,10))

print(np.random.randint(0,10,6)) #1D array

print(np.random.randint(2,10, size=(3,4))) #2D array

print(np.random.seed(43))
print(np.random.rand(2,3))

# shufle
arr = np.array([1,2,3,4])
np.random.shuffle(arr)
print(arr)

# without using shuffle function 
# 0= spam, 1- not spam
data= np.array([0,0,0,0,1,1,1,1])

# spit (first75% train, rest test
train = data[:6]
test =data[6:]

print("train:", train)
print("test:", test)

# using shuffle function 
import numpy as np

data= np.array([0,0,0,0,1,1,1,1])

np.random.shuffle(data)

train = data[:6]
test =data[6:]

print("train:", train)
print("test:", test)