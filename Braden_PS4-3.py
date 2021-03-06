### Chris Braden PS4 question 3
##
## GIVEN: file containing a single sequence (either DNA or protein) and an integer (k)
## RETURN: all k-mers occuring at least once in the sequence, listed in alphabetical order with the count of how
##         many times they occur

import sys

seq_file = open(sys.argv[1], 'r')#I need to open the indicated file
kmer_len = int(sys.argv[2])#I need to store the length of the kmer

seq = list(str(seq_file.read())) # read in sequence file to list of bases and new line characters
seq = list(val for val in seq if val != '\n')

kmer_lib = {} # make a library to store kmers
seq_len = len(seq) # measure library length
rem_seq = len(seq) # create a measure of remaining bases for sliding window

while rem_seq >= kmer_len: # so long as there are enough bases to make a kmer
    start = seq_len - rem_seq # window start
    stop = start + kmer_len # window end
    kmer_now = (''.join(seq[start:stop])).upper() # make a string of current kmer in window
    # if 'N' in kmer_now: # include if removal of N containing kmers is desired
    #     rem_seq -= 1
    #     continue
    if kmer_now in kmer_lib.keys(): # if we've seen this kmer before
        kmer_lib[kmer_now] = kmer_lib[kmer_now] + 1 # increment the count
    else: # if we haven't seen it
        kmer_lib[kmer_now] = 1 # add current kmer to the library
    rem_seq -= 1 # reduce the count of remaining bases

output_list = [] # initialize list to return values

for val in kmer_lib.keys(): # copy library into list of two item lists
    output_list.append([val, kmer_lib[val]])

output_list.sort() # sort list alphabetically

for kmer_count in output_list: # print output list line by line in readable format
    kmer_count[1] = str(kmer_count[1])
    print ' '.join(kmer_count)

seq_file.close() # close opened file