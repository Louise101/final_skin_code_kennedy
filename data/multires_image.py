#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:49:46 2021

@author: lf58
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm



depth=[]
n = 100
fd = open('987skinslice_30umsc.dat', 'rb')
datain=np.fromfile(file=fd, dtype=np.double).reshape(900,n,n)
fd.close()
data=np.flipud(datain)

xmax=0.05
ymax=0.05
zmax=0.25

a=4
b=2

#for i in range(n): #to plot cut
 #   z = (i-1)*2.*xmax/n
  #  for j in range(n):
   #     y=(j-1)*2.*ymax/n
    #    for k in range(n):
     #       x=(k-1)*2.*zmax/n 
      #      if np.sqrt(a**2*(x-0.05)**2+b**2*(y-0.05)**2) < -(z-0.075): 
       #     datain[i,j,k]=0

             


zlength=0.5 #cm
znumber=800
zvoxel_length=zlength/znumber #cm

xlength=0.1 #cm
xnumber=100
xvoxel_length=(xlength/xnumber)*10 #mm

dslice=datain[0:800,:n,50] #use data for voxel number axis and datain for axis produced in python like depth. 

print(dslice)
xdepth=[]

for i in range(xnumber):
    idepth=(i*xvoxel_length) #cm
    xdepth.append(idepth)

    
zmax=0.25

sc_width=0.002 
e_width=0.0053
m_width=0.0032
b_width=0.0032
d_width=0.1970
h_width=0.3

            
sc_z_vox=200
e_z_vox=100
m_z_vox=100
b_z_vox=100
d_z_vox=150
h_z_vox=150

            
sc_nzg= (2.*zmax)/(sc_width/sc_z_vox)
e_nzg= (2.*zmax)/(e_width/e_z_vox)
m_nzg=(2.*zmax)/(m_width/m_z_vox)
b_nzg= (2.*zmax)/(b_width/b_z_vox)
d_nzg= (2.*zmax)/(d_width/d_z_vox)
h_nzg= (2.*zmax)/(h_width/h_z_vox)

            

dep=0

for i in range(0,300):
    dep=dep + ((2*zmax)/sc_nzg)*10 # 10 converts to mm
    depth.append(dep)

    
for i in range(300,400):
    dep=dep + ((2*zmax)/e_nzg)*10
    depth.append(dep)

    
for i in range(400,500):
    dep=dep + ((2*zmax)/m_nzg)*10
    depth.append(dep)

    
for i in range(500,600):
    dep=dep + ((2*zmax)/b_nzg)*10
    depth.append(dep)

    
for i in range(500,750):
    dep=dep + ((2*zmax)/d_nzg)*10
    depth.append(dep)

    
for i in range(750,901):
    dep=dep + ((2*zmax)/h_nzg)*10
    depth.append(dep)

    
print(np.count_nonzero(np.max(dslice)))

#fig, ax = plt.subplots(1,1)

#img = ax.imshow(dslice, aspect='auto')

#x_label_list = ['0','0.25', '0.5','0.75', '1']

#ax.set_xticks([0,25,50,75,100])

#ax.set_xticklabels(x_label_list)

#y_label_list = ['0', '0.02', '0.084', '0.104','2.1','5']

#ax.set_yticks([0,200,400,600,700,800])

#ax.set_yticklabels(y_label_list)



#image=plt.imshow(dslice,extent=[min(xdepth),max(xdepth),min(depth),max(depth)], norm=LogNorm())
#plt.imshow(dslice, aspect='auto')



cutimage=dslice[:600,:100]
plt.pcolormesh(xdepth[:100],depth[:600],cutimage)#, cmap='OrRd')
plt.xlabel('x (mm)') 
plt.ylabel('z (mm)') 
plt.gca().invert_yaxis()
plt.title('Fluence Image of Direct 601nm')
plt.colorbar()
plt.show()