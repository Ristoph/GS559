# #seq = 'Class'
# #if seq.startswith('C'):
# #    print 'Starts with C'
#
# #import sys
#
# #argcount = len(sys.argv)-1
# #
# #if argcount == 2:
# #    print 'Yes'
# #elif argcount != 2:
# #    print 'Expected 2 values but found', argcount
#
# #import sys
#
# #base = sys.argv[1]
# #sequence = sys.argv[2]
#
# #if (sequence.find(base) != -1):
# #    print base, 'first occurs at position', sequence.find(base)+1
# #else:
# #    print 'A does not occur at all'
#
#
# #import sys
#
# #base = sys.argv[1]
# #sequence = sys.argv[2]
# #positions = list()
# #last_pos = 0
#
# # this won't work without a loop
# #if (sequence[last_pos:].find(base) != -1):
# #    positions = positions+sequence[last_pos:].find(base)
# #    last_pos = sequence[last_pos:].find(base)
# #    print base, 'first occurs at position', sequence.find(base)+1
# #else:
# #    print 'A does not occur at all'
#
# #1-24-18 for loops
#
# for name in ["Andrew", "Teboho", "Xian"]:
#     print "Hello", name
#
# for integer in [0, 1, 2]:
#     print integer
#     print integer * integer
#
# DNA = 'AGCTGA'
# for base in DNA:
#     print "base =", base
#
# DNA = 'AGCTGA'
# index = 0
# for base in DNA:
#     print "base", index, "is", base
#     index = index +1 # index += 1 does the same thing
# print "The sequence has", index, "bases"
#
# for index in xrange(0,4):
#     print index, "squared is", index * index
#
# for first in [1,2,3]:
#     for second in [4,5]:
#
#
#
#1-29-18

#loops
#for review:
#for <element> in <object>: ##creates the variable element as a variable of type the <object> is a list of
#while:
#does not creat the variable <element>

#import sys
# total = 0
# for i in range(1, len(sys.argv)):
#     total += int(sys.argv[i])
#     print total

#import sys
# total = 0
# i = 1
# while i < len(sys.argv):
#     total += int(sys.argv[i])
#     i += 1
#     print total

#import sys
# square = 0
# i = 0
# while square < int(sys.argv[1]):
#     square = i*i
#     if square < int(sys.argv[1]):
#         print square
#     i += 1

# import sys
#
# linecount = 0
# myfile = open(sys.argv[1], 'r')
# myline = myfile.readline()
#
# while myline != (''):
#     linecount += 1
#     myline = myfile.readline()
#
# print linecount

import sys

sequence_count = 0
myfile.readline()
while line != ('')
