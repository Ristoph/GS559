### Chris Braden PS3 question 6
##
## GIVEN: four files containing fluorophore "signal"
## RETURN: the 'hidden' DNA sequence

import sys

green_file = open(sys.argv[1], 'r') # A - file opened and read as a list
green = green_file.read() # read file data to variable
green = green.split(',') # split variable into string at commas

red_file = open(sys.argv[2], 'r') # T
red = red_file.read()
red = red.split(',')

blue_file = open(sys.argv[3], 'r') # C
blue = blue_file.read()
blue = blue.split(',')

yellow_file = open(sys.argv[4], 'r') # G
yellow = yellow_file.read()
yellow = yellow.split(',')

i = 0 # initialize index variable
base = str() # initialize variable to store current base id
sequence = list() # initialize list to store sequence

for x in green: # for each position in fluor trace
    fluor_value = 0 # initialize resetting maximum fluor value variable
    if int(green[i]) >= fluor_value: # if fluor value at position i is greater than currently stored max
        fluor_value = int(green[i]) # change the fluor value to new max
        base = 'A' # store new base
    if int(red[i]) >= fluor_value: # repeat
        fluor_value = int(red[i])
        base = 'T'
    if int(blue[i]) >= fluor_value: # repeat
        fluor_value = int(blue[i])
        base = 'C'
    if int(yellow[i]) >= fluor_value: # repeat
        fluor_value = int(yellow[i])
        base = 'G'
    ambig_check = [int(green[i]), int(red[i]), int(blue[i]), int(yellow[i])] # make list of all fluor values for position
    if ambig_check.count(fluor_value) > 1: # if the max fluor value appears more than once
        base = 'N' # Base call can't be made
    sequence.append(base) # store called base to sequence list
    i += 1 # increase index to next position
print "The DNA sequence is:" ''.join(sequence) # print result

green_file.close() # close files
red_file.close()
blue_file.close()
yellow_file.close()