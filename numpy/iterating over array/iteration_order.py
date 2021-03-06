
import numpy as np

a = np.arange(0,60,5)
a = a.reshape(3,4)
print 'Original array is:'
print a
print '\n'


print 'Transpose of the original array is:'
b = a.T
print b
print '\n'

print 'Sorted in C-style order:'
c = b.copy(order = 'C')
print c
for x in np.nditer(c):
   print x,

print '\n'

print 'Sorted in F-style order:'

c = b.copy(order = 'F')

print c
for x in np.nditer(c):
   print x,
   
   import numpy as np 
a = np.arange(0,60,5) 
a = a.reshape(3,4) 

print 'Original array is:' 
print a 
print '\n'  

print 'Sorted in C-style order:' 
for x in np.nditer(a, order = 'C'): 
   print x,  
print '\n' 

print 'Sorted in F-style order:' 
for x in np.nditer(a, order = 'F'): 
   print x,
