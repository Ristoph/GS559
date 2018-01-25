### Chris Braden PS3 question 6 ALTERNATE SOLUTION
##
## GIVEN: four files containing fluorophore "signal"
## RETURN: the 'hidden' DNA sequence

import sys

rainbow_files = [open(sys.argv[1], 'r'), open(sys.argv[2], 'r'), open(sys.argv[3], 'r'), open(sys.argv[4], 'r')]
rainbow = [x.read() for x in rainbow_files]
rainbow = [x.split(',') for x in rainbow]

rainbow_bypos = [[] for pos in range(len(rainbow[0]))]

base_list = ['A', 'T', 'C', 'G']

sequence = []

for x in rainbow:
    i = 0
    for y in x:
        rainbow_bypos[i].append(y)
        i += 1

for pos in rainbow_bypos:
    ambigcheck_list = sorted(pos)
    if ambigcheck_list[3] == ambigcheck_list[2]:
        sequence.append('N')
        continue
    i = 0
    base = 0
    fluor_max = 0
    for basefluor in pos:
        if int(basefluor) > fluor_max:
            fluor_max = int(basefluor)
            base = i
            i += 1
    sequence.append(base_list[base])

print "The DNA sequence is:", ''.join(sequence) # print result

for i in range(4):
    rainbow_files[i].close()