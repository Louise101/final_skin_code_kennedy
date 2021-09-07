#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 10:35:12 2021

@author: lf58
"""

import matplotlib.pyplot as plt
import numpy as np
import math as math
import matplotlib.image as mpimg
import glob

depth=[]
data=[]

avhole=[]
holes=[]
holelay=[]

n = 100
h=6.62607004*10**(-30) #cm^2 kg/s
c=2.99792458*10**(10) #cm/s
nphotons=8000000 
#ri=1.38
P=1

zlength=0.5 #cm
znumber=801
zvoxel_length=zlength/(znumber) #cm
vox_vol=(zvoxel_length)**3

L=P*(zlength**2)


#incIr420=((nphotons*h*c)/420*10**(-7))/(zlength**2)
#incIr630=((nphotons*h*c)/630*10**(-7))/(zlength**2)

file_list=glob.glob('jmean*.dat')


fd = open('350jmean_direct.dat', 'rb')
datain=np.fromfile(file=fd, dtype=np.double).reshape(800,n,n)
fd.close()
data=np.flipud(datain)

# average all holes
for i in range(n):
    for j in range(n):
        holev=datain[:801,i,j]
        holes.append(holev)


#Do maths to calculate fluence rate from path data
#holes=np.asarray(holes)
#j=(holes[20000]*L/(nphotons*vox_vol))
j=holes[1400]

a = np.array(j)
unique, counts = np.unique(a, return_counts=True)
dict(zip(unique, counts))

print(j)

#print(unique, counts)



#print(j.count(1))

#use data for voxel number axis and datain for axis produced in python like depth. 
#for i in range(znumber):
# idepth=(i*zvoxel_length)*10 #mm
# depth.append(idepth)

#depths=np.asarray(depth)

#set axis values for varying res

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

for i in range(0,200):
    dep=dep + ((2*zmax)/sc_nzg)*10 # 10 converts to mm
    depth.append(dep)

    
for i in range(200,300):
    dep=dep + ((2*zmax)/e_nzg)*10
    depth.append(dep)

    
for i in range(300,400):
    dep=dep + ((2*zmax)/m_nzg)*10
    depth.append(dep)

    
for i in range(400,500):
    dep=dep + ((2*zmax)/b_nzg)*10
    depth.append(dep)

    
for i in range(500,650):
    dep=dep + ((2*zmax)/d_nzg)*10
    depth.append(dep)

    
for i in range(650,801):
    dep=dep + ((2*zmax)/h_nzg)*10
    depth.append(dep)

#depth_sc=np.arange(0.0001,0.0201,0.0001)

#depth_b=np.arange(0.02,0.100535,0.000535)

#depth_d=np.arange(0.1,0.50799286, 0.00799286)






#depth=[]

#for i in depth_sc:
   # depth.append(i)

    
#for i in depth_b:
    #depth.append(i)

    
#for i in depth_d:
    #depth.append(i)

plot_depth=depth[:500]
plot_fluence=j[:500]
#for i in range(n*n):
# plt.plot(depths, holes250[i])
#plt.plot(depths, avhole250s)
plt.plot(plot_depth, plot_fluence)


plt.legend()
plt.title('Fluence at 650nm')
#plt.yscale("log")
plt.xlabel('depth(mm)')
plt.ylabel('Normalised fluence rate')
plt.show()
