### Chris Braden PS2 question 5
##
## GIVEN: a real number
## Return: integer part on one line, followed by its decimal part (i.e., the digits after the decimal point)
## on a second line. For the decimal part, print no more than 6 digits after the decimal, but do not print
## trailing zeroes.

import sys

my_number = float(sys.argv[1]) # read input number and make it a float
my_int = int(my_number) # store the integer portion of the number
my_dec = str(my_number-my_int) # store decimal portion of the number as a subset-able string

print my_int # print integer portion
print my_dec[0:8] # print 0, decimal point, and first 6 decimals