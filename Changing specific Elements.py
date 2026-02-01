import numpy as np

a = np.array([
    [1,2,3,4,5,6,7],        
    [9,10,11,12,13,14,15]
])

print(a)

print(a[1,5]) # get specific element [r,c] output will be 14 because rows starts from 0 

print(a[0,:]) # Get a Specific row

print(a[:,2]) # Get a Specific Column

print(a[0,1:6:2]) # Get a little fancy [startindex:endindex:stepsize]

print(a[0,1:-2:2]) # Get a little fancy [startindex:endindex:stepsize]

a[1,5] = 20
print(a)

a[:,5] = 20
print(a)


