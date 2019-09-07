#!/usr/bin/python

###this script is used to calculate the rdf of PS-P2VP micelle
import sys,os,subprocess
import string, math
import random
import linecache

f_xyz = open("lc.xyz","r")
f_out = open("lc.dat","w")

np = 30000
nab = 3
nmol = np/3

p = []
for lines in f_xyz.readlines()[2:]:
    line = lines.split()
    for i in range(1,4):
        line[i] = float(line[i])
    p.append(line)
f_xyz.close()

dist = 0
num = 0
for i in range(nmol-1):
    idx1 = i*nab
    idx2 = idx1+2
    x12,y12,z12 = p[idx1][1]-p[idx2][1], p[idx1][2]-p[idx2][2], p[idx1][3]-p[idx2][3]
    d12 = math.sqrt(pow(x12,2) + pow(y12,2) +pow(z12,2))
    print >> f_out, i, d12
    if d12 < 100:
        dist +=d12
        num +=1
f_out.close()
print float(dist/num)
exit
