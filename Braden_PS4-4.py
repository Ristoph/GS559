### Chris Braden PS4 question 4
##
## GIVEN: a blastn output text like example_blastnout.txt
## RETURN: each alignment score and E-value, one per line

import sys

blastn_file = open(sys.argv[1], 'r')

for line in blastn_file:
    if 'Score' in line:
        goods = line.split()
        print 'Score', str(goods[2]), 'bits,', 'E-value', str(goods[7])

blastn_file.close()