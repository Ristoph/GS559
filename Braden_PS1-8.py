### Chris Braden PS1 question 7
##
## GIVEN: two strings
## RETURN: how many times the second argument appears inside the first

import sys # load sys package
seq_input = sys.argv[1] # read arguments
seq_find = sys.argv[2]

seq_count = seq_input.count(seq_find) # count instances of second string in first

print seq_count