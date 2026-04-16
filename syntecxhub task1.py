#Step 1: Import Libraries
import numpy as np
import time

#Step2: ArrayCreation
# 1D Array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# 2D Array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# Zeros and Ones
zeros = np.zeros((2,3))
ones = np.ones((2,3))

print("Zeros:\n", zeros)
print("Ones:\n", ones)

#Step 3: Indexing and Slicing
print("First element:", arr1[0])
print("Last element:", arr1[-1])

print("Slice:", arr1[1:4])

print("2D Indexing:", arr2[0,1])
print("2D Slice:\n", arr2[:,1])

#Step 4: Mathematical Operations
a = np.array([10,20,30])
b = np.array([1,2,3])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#Step 5: Statistical Operations
data = np.array([5,10,15,20,25])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Sum:", np.sum(data))

#Step 6: Reshaping Arrays
arr = np.arange(12)
reshaped = arr.reshape(3,4)

print("Original:", arr)
print("Reshaped:\n", reshaped)

#Step 7: Broadcasting
arr = np.array([1,2,3])
print("Broadcasting + 5:", arr + 5)

#Step 8: Save and Load NumPy Arrays
np.save("my_array.npy", arr)
loaded = np.load("my_array.npy")

print("Loaded Array:", loaded)

#Step 9: Performance Comparison (NumPy vs Python List)
size = 1000000

# Python List
list1 = list(range(size))
list2 = list(range(size))

start = time.time()
result = [x + y for x, y in zip(list1, list2)]
print("Python List Time:", time.time() - start)

# NumPy Array
arr1 = np.arange(size)
arr2 = np.arange(size)

start = time.time()
result = arr1 + arr2
print("NumPy Time:", time.time() - start)