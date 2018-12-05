import numpy as np
import time
import sys

l = range(1000)
print(sys.getsizeof(1)*len(l)) 
#finds size of any numerical value and multiplies lenght of the list l
# therefore the above line prints number of bytes of list
a = np.arange(1000) 
#this function is similar to range but gives numpy array
print(a.size*a.itemsize) 
#array.itemsize gives size of element and array.size gives size of list

#lists in python are essentially an array of pointers where each pointer points to a location where data is stored

#numpy array is contiguous list of values.

#numpy is fast and convenient

SIZE  = 100000
# delclare two lists
l1 = range(SIZE)
l2 = range(SIZE)
#declare two numpy arrays
a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

start = time.time() # stores starting time in start
#script for adding two lists in python
result = [(x+y) for x,y in zip(l1,l2)]
#subtact end time form start time
print "python list time",(time.time()-start)*1000

start = time.time() # stores starting time in start
#script for adding two numpy arraysn in python
result = a1+a2
#subtact end time form start time
print "python list time",(time.time()-start)*1000

#alternate declaration

a3 = np.array([3,5,6])
a4 = np.array([4,1,1])

#some simple term by term operations

print a3+a4

print a3-a4

print a3*a4

print a3//a4


