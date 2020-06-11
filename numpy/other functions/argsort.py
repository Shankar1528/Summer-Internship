import numpy as np 
x = np.array([3, 1, 2]) 

print 'Our array is:' 
print x 
print '\n'  

print 'Applying argsort() to x:' 
y = np.argsort(x) 
print y 
print '\n'  

print 'Reconstruct original array in sorted order:' 
print x[y] 
print '\n'  

print 'Reconstruct the original array using loop:' 
for i in y: 
   print x[i],
