import numpy as np


#list to array using np.array()
lst = [1,2,3,4]

arr = np.array(lst)

print("Print array values")
for x in arr:
    print(x)
    
# .shape shows the number of rows and columns
# prints in (row, column)
print(arr.shape)

# make multidimensional array
a = [1,2,3,4]
b = [4,5,6,5]
c = [7,8,9,6]

three = []
three = np.array([a,b,c])

print(".shape")
print(three.shape)
print(three)


#reshape the array - change rows and columns
# reshape = same data values with dimenions changed
print(".reshape()")
print(three.reshape(4,3))

#slicing the array output
# syntax - print(arr[start:end-1,start:end-1])

print("Sliced printing")
print(three[0:2,0:3])

#.arage(start, end, step) automatically creates an array for using

arr = []
print("using .arange()")
arr = np.arange(0,9,3)
print(arr)

# .linspace() - The numpy.linspace() function returns number spaces evenly w.r.t interval

print("using .linspace()")
arr = np.linspace(1,10)
print(arr)


# .copy() - arrays in python follows referencing
# copy() is used to make a copy of the array, and since it is referenced, the change in the new array
# will also be updated in the old array

arr = [1,2,3,4,5]
arr1 = arr.copy()
print("using .copy()")
print(arr1)


#arr1[2:] = 9 
# replace all values of arr1 from index 3 to the end with 999
print("after replacing the values if the copied array")

# coditional checking in data analysis

val = 2
#print(arr<val) => [true, false, false, false, false]

# ones(1, dtype = int) 
# make an array and put all values as 1
#        ones(num of times, datatype)   default is float 
arr = np.ones(4, dtype=int)
print("using ones function")
print(arr)


# random

# np.random.rand
arr = np.random.rand(1,5)
print("using random.rand")
print(arr)



#np.random.rand() => Return a sample (or samples) from the “standard normal” distribution. | mean =0 | s.d=1
arr = np.random.randn(4,4)
print("usind randn standard normal")
print(arr)

