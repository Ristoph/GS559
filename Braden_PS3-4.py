### Chris Braden PS3 question 4
##
## GIVEN: an integer from 1 to 10
## RETURN: > python guess-number.py 5
##         The number I'm thinking of is less than 5.

import sys

from random import *
secret_number = randint(1,10) # The number I'm thinking of

guess_number = int(sys.argv[1]) # read user guess

if (guess_number == secret_number):
    print "You guessed right!"
elif (guess_number < secret_number):
    print "The number I'm thinking of is greater than", guess_number
elif (guess_number > secret_number):
    print "The number I'm thinking of is less than", guess_number
