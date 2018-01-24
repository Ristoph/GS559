### Chris Braden PS3 question 3
##
## GIVEN: A file containing DNA string 'sequence' composed of A, C, G, T, and '-'
## RETURN: Presence/Absence of missing bases, denoted with '-'
##    > python missing-bases.py seq1.txt
##    No missing bases detected.
##    > python missing-bases.py seq2.txt
##    2 missing bases detected.

import sys

seq_file = open(sys.argv[1], 'r')

missing = 0
for x in seq_file.readlines():
    missing = missing + x.count('-')

print missing, 'missing bases detected.'