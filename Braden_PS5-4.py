### Chris Braden PS5 question 4
##
## GIVEN: a fasta file
## RETURN: a dictionary containing the information in the fasta file

def fasta_to_dict(file_name): # this function only makes dict's with files that have keys and values on alternating lines
    file = open(file_name, 'r')
    line_list = list(x[:-1] for x in file.readlines())
    # print line_list[0:20]
    seq_id_indexes = []
    for line in line_list
    # line_index = 0
    # while line_index < len(file)

###################

import sys

fasta = sys.argv[1]

fasta_to_dict(fasta)