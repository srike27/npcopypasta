import numpy as np

#more array operations
# declaration of multi dim arrays similar to normal lists
a = np.array([[1,0,0],[0,1,0],[0,0,1]])
# to find dimensions of the array
print a.ndim
# to find itemsize of element in bytes
print a.itemsize


# normal declaration gives array as integer

# to declare as different data type we have to use dtype argument

f = np.array([1,3,4], dtype = np.float64)

print f.itemsize

#size of array gives total number of elements
A = np.array([[2,3,4],[4,5,6],[7,8,9]])

print A.shape
# shape gives the shape of array in number of elements per dimension

a = np.array([[1,0,0],[0,1,0],[0,0,1]], dtype= complex)
#initialized with complex numbers

np.zeros((3,3))
#initialized as an array of given shape and contains all zeroes
np.ones((3,3))
#initalized as an  array of given shape and contains all ones
np.arange(1,5)
#creates array with 1 to 5 elements(excluding the upper bound element)
np.arange(1,5,2)
#creates array with 1 to 5 with 2 gap between each element
np.linspace(1,5,10) 
#(lb,ub,number of numbers) creates arrayof numbers linearly spaced between lb and ub
# includes ub

print a.reshape(9,1)
#must be compatible args
print a.ravel()
#flattens multidim array into 1d array

#MATHS

print A.min() # gives minimum in entire array

print A.max() # gives maximum in entire array

print A.min(axis = 0) #returns minimum along columns as an array

print a.max(axis = 1) #returns maximum along rows as an array

print a.sum() #gives sum of all elements

print a.sum(axis=0) #returns an array of sums along that axis 0 for columns and 1 for columns

print np.sqrt(a) #returns array containing square root of all the elements

print np.std(a) #returns standard deviation of all elements in the array

print a.dot(A) #matrix multiplication of the two arrays

af = a.ravel()

aft = A.T #transposes and stores in same dimension !!!!!to be careful!!!!

# for vectors flatten and reshape to 1,n to obtain proper transpose

print af
print aft







