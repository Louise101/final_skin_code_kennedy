#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 12:35:37 2020

@author: louise
"""

import matplotlib.pyplot as plt
import numpy as np
import math as math
import matplotlib.image as mpimg
import glob

xholes397=[]
xdepth=[]
zdepth=[]
srzdepth=[]
j397=[]

n=200
nphotons=800000000
P=1

xlength=1 #cm
zlength=0.004 #cm
A=(zlength/n)**2
vox_vol=zlength**3
L=P*A


fd = open('jmean-254-no_sc.dat', 'rb')
datain=np.fromfile(file=fd, dtype=np.double).reshape(n,n,n+1)
fd.close()
data=np.flipud(datain)

for i in range(200):	
    holev=datain[i,86,0:n]	
    xholes397.append(holev)
    
#Do maths to calculate fluence rate from path data
xhole397s=np.asarray(xholes397)

#produces the third 'z' value for the intesity contour
for i in range(len(xhole397s)):
    #j397v=(xholes397[i]*L/(nphotons*vox_vol))
    v=xholes397[i]
    j397.append(v)

#use data for voxel number axis and datain for axis produced in python like depth. 
#produce x and z axis 
for i in range(n):
	idepth=(i*(xlength/n))*10 #mm
	xdepth.append(idepth)
    
for i in range(n):
	idepth=(i*(zlength/400))*10 #mm
	zdepth.append(idepth)    

plotx=xdepth
plotz=zdepth



#produces contour plot
X, Y = np.meshgrid(plotx, plotz)
Z=j397

cp = plt.contourf(X, Y, Z, cmap=('pink'))
plt.colorbar(cp)

	
plt.gca().invert_yaxis()
#plt.yscale("log")
plt.title('Fluence at 254nm')
plt.xlabel('x(mm)')
plt.ylabel('z (mm)')
plt.show()