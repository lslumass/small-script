#!/usr/bin/python

###this script is used to be generate martini-itp file for alternating copolymers
import sys,os,subprocess
import numpy as np
import string

f1 = open("md.gro","r")  ##input the original gro file
n = 3   ##number of polar bead
m = 5   ##number of apolar bead
dp = int(raw_input("the number of dp: "))   ##input the number of DP from keyboard
nab = (n+m)*dp   #bead number of one polymer chain

f2 = open('out.gro','w')  ##output file

lines = [] 
for line in f1.readlines():
    lines.append(line)
f1.close()

nmol = float(line[1])/(nab)
for i in range(nmol):
    idx1 = i*nab + 2
    idx2 = idx1 + (n+m)*(dp-1) + 2
    lines[idx1] = lines[idx1].replace('O','P')  #replace "O" as "p"
    lines[idx2] = lines[idx2].replace('N','B')  #replace "N" as "B"

for line in lines:
    print >> f2, line

f2.close()
exit
