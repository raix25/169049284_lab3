import math
pi = 3.141592 #magic number of pi 

#asking for diameter 
d = float(input("Enter the length of the diameter for the circular end of the cylinder:"))
r = d/2 

#asking for the height
h= float(input("Enter the height of the cylinder:"))

v= pi * r **2 * h  #v is volume and putting the formula for volume of cylinger 

print (f'The volume of the cylinder is {v:.2f}')