#import sys
#sum = 0
#for i in sys.argv[1:]:
#    i=int(i)
#    sum = sum + i
#    print sum


#import sys

#myfile = open(sys.argv[1],'r')
#mylist = list(myfile.readlines())
#i = 0
#for line in mylist:
#    words = line.split()
#    print len(words)

import sys

myfile = open(sys.argv[1],'r')

for x in myfile:
    words = x.split()
    lettercount = 0
    for y in words:
        lettercount = len(y)
        print lettercount


