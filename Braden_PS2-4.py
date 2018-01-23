### Chris Braden PS2 question 4
##
## GIVEN: a file with multiple lines
## RETURN: the lines of the file in reverse order

import sys

user_file = open(sys.argv[1], "r")


#lines = list(user_file.readlines())
#rev_lines = list(reversed(lines))

lines = user_file.readlines()
rev_lines = reversed(lines)


print 'lines: ', ''.join(lines)
print 'rev_lines: ', ''.join(rev_lines)

user_file.close()




