#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 17:20:20 2020

@author: louise
"""




import matplotlib.pyplot as plt
import numpy as np
import math as math
import matplotlib.image as mpimg
import glob

depth=[]
data2=[]
data1=[]

avhole=[]
holes1=[]
holes2=[]
holelay=[]

n = 200
h=6.62607004*10**(-30) #cm^2 kg/s
c=2.99792458*10**(10) #cm/s
nphotons=800000000
#ri=1.38
P=1

zlength=0.1 #cm
xnumber=200
znumber=200
zvoxel_length=zlength/(znumber) #cm
vox_vol=(zvoxel_length)**3

L=P*(zlength**2)


#incIr420=((nphotons*h*c)/420*10**(-7))/(zlength**2)
#incIr630=((nphotons*h*c)/630*10**(-7))/(zlength**2)

file_list=glob.glob('jmean*.dat')


fd = open('jmean-420-epi.dat', 'rb')
datain1=np.fromfile(file=fd, dtype=np.double).reshape(n,n,n+1)
fd.close()
data1=np.flipud(datain1)


fd = open('jmean-420-full.dat', 'rb')
datain2=np.fromfile(file=fd, dtype=np.double).reshape(n,n,n+1)
fd.close()
data2=np.flipud(datain2)


# average all holes
for i in range(n):
	for j in range(n):
		holev=datain1[:400,i,j]
		holes1.append(holev)
	
#Do maths to calculate fluence rate from path data
holes1=np.asarray(holes1)
#j=(holes[20000]*L/(nphotons*vox_vol))
j1=holes1[1970]

for i in range(n):
	for j in range(n):
		holev=datain2[:400,i,j]
		holes2.append(holev)
	
#Do maths to calculate fluence rate from path data
holes2=np.asarray(holes2)
#j=(holes[20000]*L/(nphotons*vox_vol))
j2=holes2[1970]

print(j2)
#print(j.count(1))

#use data for voxel number axis and datain for axis produced in python like depth. 	
for i in range(znumber):
	idepth=(i*zvoxel_length) #mm
	depth.append(idepth)

depths=np.asarray(depth)

#depth_sc=np.arange(0.0001,0.0201,0.0001)

#depth_b=np.arange(0.02,0.100535,0.000535)

#depth_d=np.arange(0.1,0.50799286, 0.00799286)

depth1=np.arange(0.000052,0.010452,0.000052)

depth2=depths

index=min(range(len(depth2)), key=lambda i:abs(depth2[i]-0.0104))

j_fin=[]
depth_fin=[]

print(depth2[21])

for i in depth1:
    depth_fin.append(i)
    
for i in j1:
    j_fin.append(i)

for i in depth2[index:]:
    depth_fin.append(i)
    
for i in j2[index:]:
    j_fin.append(i)




#depth=[]

#for i in depth_sc:
   # depth.append(i)
    
#for i in depth_b:
    #depth.append(i)
    
#for i in depth_d:
    #depth.append(i)

plot_depth=depth_fin
plot_fluence=j_fin
#for i in range(n*n):
#	plt.plot(depths, holes250[i])	
#plt.plot(depths, avhole250s)	
plt.plot(plot_depth, plot_fluence, label=('500nm'))

	
plt.legend()
plt.title('Normalised Fluence rate vs depth')
#plt.xscale("log")
plt.xlabel('depth(mm)')
plt.ylabel('Normalised fluence rate')
plt.show()