import array

my_array = array.array('i')

print(my_array)

my_array1 = array.array('i', [1,2,3,4])

print(my_array1)


import numpy as np

np_array = np.array([], dtype = int)
#This creates an empty numpy array of integers

print(np_array)
'''
when we are creating an empty array by using numpy model, no memory is allocated for the array elements

because there is not any element in the array over here.

The only thing that is going to be created in the memory is going to be NP array object in which we

have the metadata for the array over here.

And this object over here does not store any reference to the any memory block

'''
np_array1 = np.array([1,2,3,4], dtype = int)
#This creates a numpy array of integers with 4 elements 
print(np_array1)

#Time Complexity of array creation when empty array is created is O(1)
#Time Complexity of array creation when array with n elements is created is O(n)