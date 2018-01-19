### Chris Braden PS1 question 4
##
## GIVEN: three command line arguments
## Return: the three arguments as uppercase letters on a single line with spaces between

import sys # load sys package
arg1 = sys.argv[1] # read arguments
arg2 = sys.argv[2]
arg3 = sys.argv[3]

arg1 = arg1.upper() # convert arguments to upper case
arg2 = arg2.upper()
arg3 = arg3.upper()

print arg1, arg2, arg3 # print arguments: python 2.7 print command is hot garbage