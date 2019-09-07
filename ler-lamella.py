#!/usr/bin/python
import math,sys,os,subprocess
import string               
import numpy as np
import multiprocessing

##calculate the line edge roughness of the lamellae in alt-bulk system
##CAUTION: lamellae must be parallel to the YOZ plane.
##LER is 3*sigema

##read files and definite varibles             
fout = open('ler.dat','w')

Cm = int(raw_input("the number of C: "))
f = open('LER.xyz','r')
lines = f.readlines()
N_tot = int(lines[0])
N_C = N_tot/Cm

## read all the points
points = []
for i in range(N_tot):
    point = []
    line = lines[i+2]
    point = line.split()
    point[1] = float(point[1])
    point[2] = float(point[2])
    point[3] = float(point[3])
    points.append(point)
f.close()

##calculate the center of mass of the membrane
sumx,sumy,sumz = 0, 0, 0
for p in points:
    sumx = sumx + p[1]
    sumy = sumy + p[2]
    sumz = sumz + p[3]
rcx, rcy, rcz = float(sumx/N_tot), float(sumy/N_tot), float(sumz/N_tot)

## divide these points into different interfaces.
lefts = []
rights = []
for i in range(N_C):
    m = (i-1)*Cm
    p = points[m][1]
    if p < rcx:
        lefts.append(p)
    elif p > rcx:
        rights.append(p)

## calculate the standard deviation (sigema) in the left and right
sigema_1 = np.std(lefts,ddof=1)
LER_1 = sigema_1*3

sigema_2 = np.std(rights,ddof=1)
LER_2 = sigema_2*3

## calculate the average LER
LER = float((sigema_1+sigema_2)/2)*3

print >> fout, LER_1, LER_2, LER
print LER_1, LER_2, LER
