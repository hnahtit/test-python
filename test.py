import os
import numpy as np

# a = np.full((2,2),7)
# b = np.random.randint(low = 4,high = 6,size = (4,4))
# print(b)
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
a_row = a[:,1]
print(a_row)
ind_bool = a > 2
print(ind_bool)
