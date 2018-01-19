### Chris Braden PS1 question 6
##
## GIVEN: a DNA string 'sequence'
## RETURN: a count of the number of bases in the DNA string

import sys # load sys package
DNA = sys.argv[1] # read arguments

DNA_len = len(DNA)

print "The sequence is", DNA_len, "bases long."