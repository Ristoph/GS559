### Chris Braden PS2 question 4
##
## GIVEN: a file with multiple lines
## RETURN: the lines of the file in reverse order

import sys

user_file = open(sys.argv[1], "r") # read user supplied file name and open file

lines = user_file.readlines() # obtain list  from user file
rev_lines = reversed(lines) # make a list of lines in reverse

print ''.join(rev_lines) # print out the lines as a string

user_file.close() # close open file
