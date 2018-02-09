### Chris Braden PS5 question 4
##
## GIVEN: a fasta file
## RETURN: a dictionary containing the information in the fasta file

def fasta_to_dict(file_name): # this function only makes dict's with fasta files that have '>' marked keys and values on separate lines

    seq_lib = {}
    my_fasta_file = open(file_name, 'r')
    line_list = list(x.strip() for x in my_fasta_file.readlines())
    my_fasta_file.close()
    seq_id_indexes = []
    index = 0

    for line in line_list:
        if '>' in line:
            seq_id_indexes.append(index)
        index += 1
    seq_id_indexes.append(len(line_list))

    for i in range(len(seq_id_indexes)-1):
        key_index = seq_id_indexes[i]
        next_key_index = seq_id_indexes[i+1]
        key = line_list[key_index]
        seq = ''.join(line_list[key_index+1:next_key_index])
        seq_lib[key[1:]] = seq

    return seq_lib

###################

import sys

fasta = sys.argv[1]

seqs_dict = fasta_to_dict(fasta)

print "There are", len(seqs_dict), "sequences in", fasta