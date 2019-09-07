#!/usr/bin/python

###this script is used to be generate TraPPE-UA itp file for alternating copolymers
import sys,os,subprocess
import string

f1 = open("mapping.ndx","w")
f2 = open("bonded.ndx","w")
n = 8
m = 87
dp = 1
nmol = 50
np = 26

#mapping
for i in range(nmol):
    print >> f1, '[ C1 ]'
    print >> f1, '{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12}'.format(i*np+1,i*np+2,i*np+3,i*np+4,i*np+5,i*np+6,i*np+7,i*np+8,i*np+9,i*np+10,i*np+11,i*np+12,i*np+13)
    print >> f1, '[ C2 ]'
    print >> f1, '{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12}'.format(i*np+14,i*np+15,i*np+16,i*np+17,i*np+18,i*np+19,i*np+20,i*np+21,i*np+22,i*np+23,i*np+24,i*np+25,i*np+26)
f1.close()

#bond
f2.write('[ C-C ]\n')	
for j in range(nmol):
    print >> f2, '{0} {1}'.format(j*np+1,j*np+2)	  
f2.close()
exit
