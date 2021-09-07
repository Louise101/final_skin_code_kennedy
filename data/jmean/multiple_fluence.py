#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 12:39:28 2020

@author: louise
"""

import matplotlib.pyplot as plt
import numpy as np
import math as math
import matplotlib.image as mpimg
import glob

depth=[]
data=[]


holes222_full=[]
depth222_full=[]

holes222_half=[]
depth222_half=[]

holes222_no=[]
depth222_no=[]

holes254_full=[]
depth254_full=[]

holes254_half=[]
depth254_half=[]

holes254_no=[]
depth254_no=[]

holes300_full=[]
depth300_full=[]

holes300_half=[]
depth300_half=[]

holes300_no=[]
depth300_no=[]

holes350_full=[]
depth350_full=[]

holes350_half=[]
depth350_half=[]

holes350_no=[]
depth350_no=[]

holes400_full=[]
depth400_full=[]

holes400_half=[]
depth400_half=[]

holes400_no=[]
depth400_no=[]



n = 200
h=6.62607004*10**(-30) #cm^2 kg/s
c=2.99792458*10**(10) #cm/s
nphotons=80000000 
#ri=1.38
P=1.5

zlength=0.005 #cm
znumber=200
zvoxel_length=zlength/(znumber) #cm
vox_vol=(zvoxel_length)**3

L=P*(zlength**2)


#incIr420=((nphotons*h*c)/420*10**(-7))/(zlength**2)
#incIr630=((nphotons*h*c)/630*10**(-7))/(zlength**2)

file_list=glob.glob('jmean*.dat')
print(file_list)


for f in file_list:
	fd = open(f, 'rb')
	datain=np.fromfile(file=fd, dtype=np.double).reshape(n,n,n+1)
	fd.close()
	flipdata=np.flipud(datain)
	data.append(datain)
    
data222_full=data[0]
data222_half=data[6]
data222_no=data[9]
data254_full=data[5]
data254_half=data[1]
data254_no=data[2]
data300_full=data[4]
data300_half=data[11]
data300_no=data[3]
data350_full=data[12]
data350_half=data[10]
data350_no=data[8]
data400_full=data[14]
data400_half=data[7]
data400_no=data[13]


# sort data
for i in range(n):
	for j in range(n):
		holev=data222_full[0:n,i,j]
		holes222_full.append(holev)

for i in range(n):
	for j in range(n):
		holev=data222_half[0:n,i,j]
		holes222_half.append(holev)
        
for i in range(n):
	for j in range(n):
		holev=data222_no[0:n,i,j]
		holes222_no.append(holev)
        
for i in range(n):
	for j in range(n):
		holev=data254_full[0:n,i,j]
		holes254_full.append(holev)
        
for i in range(n):
	for j in range(n):
		holev=data254_half[0:n,i,j]
		holes254_half.append(holev)
        
for i in range(n):
	for j in range(n):
		holev=data254_no[0:n,i,j]
		holes254_no.append(holev)
        
for i in range(n):
	for j in range(n):
		holev=data300_full[0:n,i,j]
		holes300_full.append(holev)
        
for i in range(n):
	for j in range(n):
		holev=data300_half[0:n,i,j]
		holes300_half.append(holev)
        
for i in range(n):
	for j in range(n):
		holev=data300_no[0:n,i,j]
		holes300_no.append(holev)
        
for i in range(n):
	for j in range(n):
		holev=data350_full[0:n,i,j]
		holes350_full.append(holev)
        
for i in range(n):
	for j in range(n):
		holev=data350_half[0:n,i,j]
		holes350_half.append(holev)
        
for i in range(n):
	for j in range(n):
		holev=data350_no[0:n,i,j]
		holes350_no.append(holev)
        
for i in range(n):
	for j in range(n):
		holev=data400_full[0:n,i,j]
		holes400_full.append(holev)
        
for i in range(n):
	for j in range(n):
		holev=data400_half[0:n,i,j]
		holes400_half.append(holev)
        
for i in range(n):
	for j in range(n):
		holev=data400_no[0:n,i,j]
		holes400_no.append(holev)


	

#Do maths to calculate fluence rate from path data
hole222s_full=np.asarray(holes222_full)
j222_full=(holes222_full[7508])
          
hole222s_half=np.asarray(holes222_half)
j222_half=(holes222_half[7508])
         
hole222s_no=np.asarray(holes222_no)
j222_no=(holes222_no[7508])
         
hole254s_full=np.asarray(holes254_full)
j254_full=(holes254_full[7508])
          
hole254s_half=np.asarray(holes254_half)
j254_half=(holes254_half[7508])
         
hole254s_no=np.asarray(holes254_no)
j254_no=(holes254_no[7508])

hole300s_full=np.asarray(holes300_full)
j300_full=(holes300_full[7508])
          
hole300s_half=np.asarray(holes300_half)
j300_half=(holes300_half[7508])
         
hole300s_no=np.asarray(holes300_no)
j300_no=(holes300_no[7508])

hole350s_full=np.asarray(holes350_full)
j350_full=(holes350_full[7508])
          
hole350s_half=np.asarray(holes350_half)
j350_half=(holes350_half[7508])
         
hole350s_no=np.asarray(holes350_no)
j350_no=(holes350_no[7508])

hole400s_full=np.asarray(holes400_full)
j400_full=(holes400_full[7508])
          
hole400s_half=np.asarray(holes400_half)
j400_half=(holes400_half[7508])
         
hole400s_no=np.asarray(holes400_no)
j400_no=(holes400_no[7508])



#use data for voxel number axis and datain for axis produced in python like depth. 

full222_zlength=0.002/znumber
half222_zlength=0.002/znumber
no222_zlength=0.003/znumber

full254_zlength=0.005/znumber
half254_zlength=0.005/znumber
no254_zlength=0.004/znumber

full300_zlength=0.0084/znumber
half300_zlength=(0.0094-0.001)/znumber
no300_zlength=(0.0104-0.002)/znumber

full350_zlength=0.1/znumber
half350_zlength=(0.1-0.001)/znumber
no350_zlength=(0.1-0.002)/znumber

full400_zlength=0.1/znumber
half400_zlength=(0.1-0.001)/znumber
no400_zlength=(0.1-0.002)/znumber




	
for i in range(znumber):
	idepth=(i*full222_zlength)*10 #mm
	depth222_full.append(idepth)	

depths222_full=np.asarray(depth222_full)

for i in range(znumber):
	idepth=(i*half222_zlength)*10 #mm
	depth222_half.append(idepth)	

depths222_half=np.asarray(depth222_half)

for i in range(znumber):
	idepth=(i*no222_zlength)*10 #mm
	depth222_no.append(idepth)	

depths222_no=np.asarray(depth222_no)

for i in range(znumber):
	idepth=(i*no254_zlength)*10 #mm
	depth254_no.append(idepth)	

depths254_no=np.asarray(depth254_no)
	
for i in range(znumber):
	idepth=(i*full254_zlength)*10 #mm
	depth254_full.append(idepth)	

depths254_full=np.asarray(depth254_full)

for i in range(znumber):
	idepth=(i*half254_zlength)*10 #mm
	depth254_half.append(idepth)	

depths254_half=np.asarray(depth254_half)

for i in range(znumber):
	idepth=(i*no300_zlength)*10 #mm
	depth300_no.append(idepth)	

depths300_no=np.asarray(depth300_no)
	
for i in range(znumber):
	idepth=(i*full300_zlength)*10 #mm
	depth300_full.append(idepth)	

depths300_full=np.asarray(depth300_full)

for i in range(znumber):
	idepth=(i*half300_zlength)*10 #mm
	depth300_half.append(idepth)	

depths300_half=np.asarray(depth300_half)

for i in range(znumber):
	idepth=(i*no350_zlength)*10 #mm
	depth350_no.append(idepth)	

depths350_no=np.asarray(depth350_no)
	
for i in range(znumber):
	idepth=(i*full350_zlength)*10 #mm
	depth350_full.append(idepth)	

depths350_full=np.asarray(depth350_full)

for i in range(znumber):
	idepth=(i*half350_zlength)*10 #mm
	depth350_half.append(idepth)	

depths350_half=np.asarray(depth350_half)

for i in range(znumber):
	idepth=(i*no400_zlength)*10 #mm
	depth400_no.append(idepth)	

depths400_no=np.asarray(depth400_no)
	
for i in range(znumber):
	idepth=(i*full400_zlength)*10 #mm
	depth400_full.append(idepth)	

depths400_full=np.asarray(depth400_full)

for i in range(znumber):
	idepth=(i*half400_zlength)*10 #mm
	depth400_half.append(idepth)	

depths400_half=np.asarray(depth400_half)


	
#for i in range(znumber):
#	idepth=(i*zvoxel_length)*10 #mm
#	depth.append(idepth)

#depths=np.asarray(depth)


plt.plot(depths222_full, j222_full,'r-', label=('222nm full sc'))
plt.plot(depths254_full, j254_full,'r--', label=('254nm full'))
plt.plot(depths300_full, j300_full,'r-.', label=('300nm full sc'))
plt.plot(depths350_full[0:70], j350_full[0:70],'r:', label=('350nm full sc'))
plt.plot(depths400_full[0:70], j400_full[0:70],'r:.', label=('400nm full sc'))

plt.plot(depths222_half, j222_half,'g-', label=('222nm half sc'))
plt.plot(depths254_half, j254_half,'g--', label=('254nm half sc'))
plt.plot(depths300_half, j300_half,'g-.', label=('300nm half sc'))
plt.plot(depths350_half[0:70], j350_half[0:70],'g:', label=('350nm half sc'))
plt.plot(depths400_half[:70], j400_half[:70],'g:.', label=('400nm half sc'))

plt.plot(depths222_no, j222_no,'b-', label=('222nm no sc'))
plt.plot(depths254_no, j254_no,'b--', label=('254nm no sc'))
plt.plot(depths300_no, j300_no,'b-.', label=('300nm no sc'))
plt.plot(depths350_no[:70], j350_no[:70],'b:', label=('350nm no sc'))
plt.plot(depths400_no[:70], j400_no[:70],'b:.', label=('400nm no sc'))



	
plt.legend()
plt.title('Normalised Fluence Rate vs Depth into Skin')
plt.xlabel('depth(mm)')
#plt.xscale('log')
#plt.yscale('log')
plt.ylabel('Normalised fluence rate')
plt.show()



plt.plot(depths222_full, j222_full,'r-', label=('222nm full sc'))
plt.plot(depths254_full, j254_full,'r--', label=('254nm full sc'))
plt.plot(depths300_full, j300_full,'r-.', label=('300nm full sc'))
plt.plot(depths350_full[0:70], j350_full[0:70],'r:', label=('350nm full sc'))
plt.plot(depths400_full[0:70], j400_full[0:70],'r:.', label=('400nm full sc'))

plt.plot(depths222_half, j222_half,'g-', label=('222nm half sc'))
plt.plot(depths254_half, j254_half,'g--', label=('254nm half sc'))
plt.plot(depths300_half, j300_half,'g-.', label=('300nm half sc'))
plt.plot(depths350_half[0:70], j350_half[0:70],'g:', label=('350nm half sc'))
plt.plot(depths400_half[:70], j400_half[:70],'g:.', label=('400nm half sc'))

plt.plot(depths222_no, j222_no,'b-', label=('222nm no sc'))
plt.plot(depths254_no, j254_no,'b--', label=('254nm no sc'))
plt.plot(depths300_no, j300_no,'b-.', label=('300nm no sc'))
plt.plot(depths350_no[:70], j350_no[:70],'b:', label=('350nm no sc'))
plt.plot(depths400_no[:70], j400_no[:70],'b:.', label=('400nm no sc'))


plt.axvline(0.02,color='c',label='Stratum Corenum end')
plt.axvline(0.084,color='m',label='Epidermis end')
plt.axvline(0.094,color='y',label='Melanin Layer end')
plt.axvline(0.104,color='b',label='Basal Layer end')



	
plt.legend()
plt.title('Normalised Fluence rate vs depth into 5 layers')
plt.xlabel('depth(mm)')
#plt.xscale('log')
#plt.yscale('log')
plt.ylabel('Normalised fluence rate')
plt.show()