import numpy as np


#list to array using np.array()
lst = [1,2,3,4]

arr = np.array(lst)

for x in arr:
    print(x)
    
# .shape shows the number of rows and columns
# prints in (row, column)
print(arr.shape)
