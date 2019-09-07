#!/usr/bin/python

###this script is used to be generate martini-itp file for alternating copolymers
import sys,os,subprocess
import string

f1 = open("md.gro","r")
n = 2
m = 4
dp = 6
nmol = 1200
nab = (n+m)*dp

f2 = open('cg.gro','w')

print >> f2, 'alternating\n{0}'.format(nab*nmol)

all=[]
lines = f1.readlines()[2:]
for line in lines:
    line=line.strip('\n')
    all.append(line)
for i in range(nmol*dp):
    s = (i)*(n+m)
    all[s] = all[s].replace(' O', 'O1')
    all[s+1] = all[s+1].replace(' O', 'O2')
    all[s+2] = all[s+2].replace(' N', 'N3')
    all[s+3] = all[s+3].replace(' C', 'C4')
    all[s+4] = all[s+4].replace(' C', 'C5')
    all[s+5] = all[s+5].replace(' C', 'C6')
for i in range(nmol*nab):
    print >> f2, all[i]
print >> f2, lines[-1].strip('\n')
f1.close()
f2.close()
exit
