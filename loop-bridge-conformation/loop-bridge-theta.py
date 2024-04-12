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

p = []
for lines in f.readlines()[2:]:
	  line = lines[12:53]
	  line = line.split()
	  for i in range(3):
	  	  line[0] = float(line[0])
	  	  line[1] = float(line[1])
	  	  line[2] = float(line[2])
	  p.append(line)
f.close()

for i in range(nmol):
    j=i*8+n-1
    k=j+int(m*0.5)
    l=i*8+n+m-1
    x1,y1,z1 = p[j][0]-p[k][0], p[j][1]-p[k][1], p[j][2]-p[k][2]
    x2,y2,z2 = p[l][0]-p[k][0], p[l][1]-p[k][1], p[l][2]-p[k][2]
    axb = x1*x2+y1*y2+z1*z2
    a = math.sqrt(pow(x1,2) + pow(y1,2) +pow(z1,2))
    b = math.sqrt(pow(x2,2) + pow(y2,2) +pow(z2,2))
    cosab = axb/(a*b)
    if cosab >= -0.500:
    	 Nloop=Nloop+1
    else:
    	 Nbrg=Nbrg+1

print ("Nloop=", Nloop, "Nbrg=", Nbrg)

