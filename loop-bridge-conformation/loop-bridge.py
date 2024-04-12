#!/usr/bin/python
import math,sys,os,subprocess
import string

f = open('ab.xyz','r')

n = int(raw_input("the number of n: "))
m = int(raw_input("the number of m: "))
np = int(raw_input("the number of np: "))
nmol = int(np/(n+m))

Nloop=0
Nbrg=0

points = []
for lines in f.readlines()[2:]:
	  line = lines[12:53]
	  line = line.split()
	  points.append()
f.close()

for i in range(nmol):
    j=i*8+n
    k=j+m-1
    distance = math.sqrt(pow(abs(points[j][0]-points[k][0]),2) + pow(abs(points[j][1]-points[k][1]),2) +pow(abs(points[j][2]-points[k][2]),2))
    if d12 <= 2.15:
    	 Nloop=Nloop+1
    elif d12 < 20:
    	 Nbrg=Nbrg+1

print ("Nloop=", Nloop, "Nbrg=", Nbrg)

