### Chris Braden PS5 question 3
##
## GIVEN: a file containing organisms and sequences (as above), and a query species
## RETURN: the corresponding sequence for the query species, or a message if the query species isn't in the file

################# PACKAGES

import sys

################# FUNCTIONS

def file_to_dict(file_name): # this function only makes dict's with files that have keys and values on alternating lines
    file = open(file_name, 'r')
    file_elements = list(x.strip() for x in file.readlines())
    file.close()
    new_dict = {}
    key_line = 0
    val_line = 1
    for el in range(len(file_elements)/2):
        new_dict[file_elements[key_line]] = file_elements[val_line]
        key_line += 2
        val_line += 2
    return new_dict

def get_dict_entry(dict, key): # this function takes a dictionary and a key entry and returns the value or an error
    if key in dict:
        val = dict[key]
        return val
    else:
        return -1

#################### BODY

seq_dict = file_to_dict(sys.argv[1]) # make a dict using user-supplied file name
query = sys.argv[2] # store the user-supplied query species
result = get_dict_entry(seq_dict, query) # retrieve sequence matching the query or an error value (-1)

if result != -1:
    print query
    print result
elif result == -1:
    print "sequence", query, "not found"

