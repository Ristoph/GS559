### Chris Braden PS1 question 7
##
## GIVEN: a string and two integers (representing a range of positions in the sequence)
## RETURN: the characters in the given range of the sequence

import sys # load sys package
seq_input = sys.argv[1] # read arguments
seq_sub_start = int(sys.argv[2])-1 # subtracts one to translate from human to programmer
seq_sub_end = int(sys.argv[3])

seq_sub = seq_input[seq_sub_start:seq_sub_end] # Get sub sequence

print seq_sub # print sub sequence