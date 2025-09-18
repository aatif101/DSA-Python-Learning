import array

my_array = array.array('i', [1,2,3,4])

my_array.insert(2, 5) #array.insert(index, value)  

print(my_array) 


def traverse_array(arr):
    for i in arr:
        print(i)
        #easy

traverse_array(my_array)    