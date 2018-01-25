### Chris Braden PS3 question 6
##
## GIVEN: four files containing fluorophore "signal"
## RETURN: the 'hidden' DNA sequence

import sys

green_file = open(sys.argv[1], 'r') # A - file opened and read as a list
green = green_file.read()
green = green.split(',')

red_file = open(sys.argv[2], 'r') # T
red = red_file.read()
red = red.split(',')

blue_file = open(sys.argv[3], 'r') # C
blue = blue_file.read()
blue = blue.split(',')

yellow_file = open(sys.argv[4], 'r') # G
yellow = yellow_file.read()
yellow = yellow.split(',')

i = 0
base = str()
sequence = list()

for x in green:
    fluor_value = 0
    if int(green[i]) >= fluor_value:
        fluor_value = int(green[i])
        base = 'A'
    if int(red[i]) >= fluor_value:
        fluor_value = int(red[i])
        base = 'T'
    if int(blue[i]) >= fluor_value:
        fluor_value = int(blue[i])
        base = 'C'
    if int(yellow[i]) >= fluor_value:
        fluor_value = int(yellow[i])
        base = 'G'
    #if
     #   base = 'N'
    sequence.append(base)
    print green[i], red[i], blue[i], yellow[i]
    print sequence
    i += 1

# boolcheck = int(green[0]) < int(red[0])
# print boolcheck

# i = 1
# for x in green_file:
#     green = green_file.readline()
#     # red = red_file.read(i)
#     # blue = blue_file.read(i)
#     # yellow = yellow_file.read(i)
#     print green#, red, blue, yellow
#     i += 1


green_file.close()
red_file.close()
blue_file.close()
yellow_file.close()