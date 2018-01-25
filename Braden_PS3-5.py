### Chris Braden PS3 question 5
##
## GIVEN: a query barcode sequence, a file with sequencing reads of interest, and a file with barcode sequences
## RETURN: sequences from the reads file that have the corresponding barcode sequences

import sys

barcode_user = str(sys.argv[1]) # read user supplied barcode
barcode_file = open(sys.argv[2], 'r') # open user supplied barcode file
sequence_file = open(sys.argv[3], 'r') # open user supplied sequence file

for x in barcode_file: # for each line in barcode file
    sequence = sequence_file.readline() # retrieve the next line of sequence file
    if (x.strip() == barcode_user): # if user barcode matches supplied barcode stripped of leading/trailing characters
        print sequence # print the current line of sequence file
