import numpy as np

a = np.array([
    [[1,2], [3,4]],
    [[5,6], [7,8]]
])

print(a)

print("Dimensions:", a.ndim)

print("Shape:", a.shape)

print(a[0,1,1]) #get specific element (work outside in)

a[:,1,:] = [[9,9],[8,8]] #replace
print(a)