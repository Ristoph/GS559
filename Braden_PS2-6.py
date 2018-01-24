### Chris Braden PS2 question 6
##
## GIVEN: a number and a format, where the format is either integer, real, or scientific
## Return: the given number in the requested format, AND print an error if an invalid format
## string is provided

import sys

input_number = float(sys.argv[1]) # get number
target_format = sys.argv[2] # get format

int_number = '%d' %input_number # convert number to various formats pre-emptively
real_number = '%f' %input_number
sci_number = '%e' %input_number

if (target_format == 'integer'): # return requested format or error
    print int_number
elif (target_format == 'real'):
    print real_number
elif (target_format == 'scientific'):
    print sci_number
else:
    print 'unrecognized format'