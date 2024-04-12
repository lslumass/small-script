#!/usr/bin/python
import math,sys,os,subprocess
import string

f = open('order.xyz','r')
fout = open('order-para.dat','w')

#键盘输入软段和硬段的长度（n和m）
#input the number of coil and rod length (n and m)
n = int(raw_input("the number of n: "))
m = int(raw_input("the number of m: "))
lines = f.readlines()
np = int(lines[0])               #the number of total beads 体系中粒子的总数目
nmol = int(np/(n+m))             #the number of total rods 体系中所以刚性链段的总数

f.close()
f = open('order.xyz','r')        #input file 输入坐标文件order.xyz
#read all of the points
p = []
for lines in f.readlines()[2:]:
    line = lines[10:53]
    line = line.split()
    for i in range(3):
        line[0] = float(line[0])
        line[1] = float(line[1])
        line[2] = float(line[2])
    p.append(line)
f.close()

#transform the points into rods and the com of the rod
rods = []
coms = []
Res = []
Rgs = []
for i in range(nmol):
    rod = [0,0,0]
    com = [0,0,0]
    Re,Rg,sumx,sumy,sumz = 0,0,0.00,0.00,0.00
    
    j = n+ i*(n+m)
    k = j+m-1
    rod[0], rod[1], rod[2] = p[k][0]-p[j][0], p[k][1]-p[j][1], p[k][2]-p[j][2]
    com[0], com[1], com[2] = (p[k][0]+p[j][0])*0.5, (p[k][1]+p[j][1])*0.5, (p[k][2]+p[j][2])*0.5
    rods.append(rod)
    coms.append(com)
    Re = math.sqrt(pow(rod[0],2) + pow(rod[1],2) + pow(rod[2],2))
    Res.append(Re)
    
    for l in range(j,j+m):
    	  sumx = sumx+p[l][0]
    	  sumy = sumy+p[l][1]
    	  sumz = sumz+p[l][2]
    rcx,rcy,rcz = float(sumx/m), float(sumy/m), float(sumz/m)
    dist = 0.00
    for l in range(j,j+m):
    	  dist = dist + pow((p[l][0]-rcx),2) + pow((p[l][1]-rcy),2) + pow((p[l][2]-rcz),2)
    Rg = float(dist/m)
    Rgs.append(Rg)

#calculate the order parameter,
sumS = 0.00
sumN = 0.00
Si = [0]*nmol
Ni = [0]*nmol
for i in range(nmol):
    for j in range(nmol):
        if i != j:
           for k in range(n+j*(n+m),n+j*(n+m)+m):
               vx,vy,vz = p[k][0]-coms[i][0], p[k][1]-coms[i][1], p[k][2]-coms[i][2]
    	       axb = vx*rods[i][0] + vy*rods[i][1] + vz*rods[i][2]
    	       a = math.sqrt(pow(vx,2) + pow(vy,2) +pow(vz,2))
    	       b = math.sqrt(pow(rods[i][0],2) + pow(rods[i][1],2) +pow(rods[i][2],2))
    	       cosab = axb/(a*b)
    	       ll = a*abs(cosab)                         #parallel direction
    	       T = math.sqrt(pow(a,2)-pow(ll,2))    #vertical direction
    	       
    	       if (ll <= Res[i]*0.5) and (T <= Rgs[i]):
    	      	  Ni[i] = Ni[i]+1
    	      	  x1,y1,z1 = rods[i][0], rods[i][1], rods[i][2]
    	      	  x2,y2,z2 = rods[j][0], rods[j][1], rods[j][2]
    	      	  axb = x1*x2+y1*y2+z1*z2
    	      	  a = math.sqrt(pow(x1,2) + pow(y1,2) +pow(z1,2))
    	      	  b = math.sqrt(pow(x2,2) + pow(y2,2) +pow(z2,2))
    	      	  cosab = axb/(a*b)
    	      	  Si[i] = Si[i] + (3*cosab*cosab-1)*0.5
    	     	  break

for i in range (nmol):
    sumS = sumS + Si[i]
    sumN = sumN + Ni[i]
	  
S = float(sumS/sumN)
print ('S=%f' % (S))
print >> fout, S

