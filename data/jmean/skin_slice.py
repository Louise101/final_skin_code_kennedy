import matplotlib.pyplot as plt
import numpy as np
import math as math
import matplotlib.image as mpimg
import csv



depth=[]
n = 201
fd = open('rhokap-400-final.dat', 'rb')
datain=np.fromfile(file=fd, dtype=np.double).reshape(n,n,n)
fd.close()
data=np.flipud(datain)

zlength=0.1 #cm
znumber=200
zvoxel_length=zlength/znumber #cm

dslice=data[0:n,0:n,10] #use data for voxel number axis and datain for axis produced in python like depth. 


for i in range(znumber):
	idepth=(i*zvoxel_length) #cm
	depth.append(idepth)
	

image=plt.imshow(dslice,extent=[min(depth),max(depth),min(depth),max(depth)])
plt.xlabel('x (cm)') 
plt.ylabel('z (cm)') 
plt.title('skin layers')
plt.colorbar()
plt.show()






