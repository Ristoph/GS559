#seq = 'Class'
#if seq.startswith('C'):
#    print 'Starts with C'

#import sys

#argcount = len(sys.argv)-1
#
#if argcount == 2:
#    print 'Yes'
#elif argcount != 2:
#    print 'Expected 2 values but found', argcount

#import sys

#base = sys.argv[1]
#sequence = sys.argv[2]

#if (sequence.find(base) != -1):
#    print base, 'first occurs at position', sequence.find(base)+1
#else:
#    print 'A does not occur at all'


import sys

base = sys.argv[1]
sequence = sys.argv[2]
positions = list()
last_pos = 0

# this won't work without a loop
if (sequence[last_pos:].find(base) != -1):
    positions = positions+sequence[last_pos:].find(base)
    last_pos = sequence[last_pos:].find(base)
    print base, 'first occurs at position', sequence.find(base)+1
else:
    print 'A does not occur at all'