# insert rom version
import array
import random
import math
import sys

def hex2bin(x):
    tab = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111',]
##    tab = ['0000 ','0001 ','0010 ','0011 ','0100 ','0101 ','0110 ','0111 ','1000 ','1001 ','1010 ','1011 ','1100 ','1101 ','1110 ','1111 ']
    a0 = tab[(x>>28)&15]
    a1 = tab[(x>>24)&15]
    a2 = tab[(x>>20)&15]
    a3 = tab[(x>>16)&15]
    a4 = tab[(x>>12)&15]
    a5 = tab[(x>>8)&15]
    a6 = tab[(x>>4)&15]
    a7 = tab[(x>>0)&15]
    #print ("%08x") % x
    return a0+a1+a2+a3+a4+a5+a6+a7

## ---------- start -------------
versionid = '01'    # rev. in svn

infile = './debug/sdc_test_bin'
outfile = 'sdc_test.hex'
textfile = 'sdc_test.txt'

f1 = open(infile, 'rb')
f2 = open(outfile,'wb')
f3 = open(textfile,'w')

f1.seek(0,2)
size = f1.tell()
f1.seek(0,0)

d32 = array.array('I')
size_div = int(math.ceil(size/4))
d32.fromfile(f1,size_div)

d32[size_div-1] = int(versionid,16)
d32.tofile(f2)

for i in range(size_div):
    #print("%08x") % d32[i]
    line = hex2bin(d32[i])
    f3.write(line+"\n")
    
f1.close()
f2.close()
f3.close()

