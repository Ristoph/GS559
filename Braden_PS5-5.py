### Chris Braden PS5 question 5
##
## GIVEN: a plaintext file and a query letter-length minimum
## RETURN: the most common word in the file with at least the minimum letter-length, and the number of times it occurs

##################### Functions


def find_words_of_len(doc, word_len):   # takes an open file and a minimum letter-length, returns a dictionary with words and counts
    word_index_dict = {}

    for doc_line in doc:                # read each document line
        doc_line = doc_line.strip()     # remove special(whitespace?) characters
        doc_line = doc_line.split(' ')  # divide into a list of words

        for word in doc_line:           # with each word in document line
            word = word.lower()         # ignore case

            for bad_char in ['.', ',', "'", '"', '?', ';', ':', '-', '(', ')', '!']: # check string and remove listed chars
                word = word.replace(bad_char, '')

            if word != '':                                              # don't include empty lines
                if len(word) >= word_len:                               # include only words of sufficient length
                    if word in word_index_dict.keys():                  # if we've seen it before, increase the count
                        word_index_dict[word] = word_index_dict[word] + 1
                    else:                                               # if we haven't seen it, add it with a count of one
                        word_index_dict[word] = 1

            else:
                continue

    return(word_index_dict)             # return the dictionary of words and counts



def dict_max_value(dict):    # takes a dictionary of words and counts and returns list of entries with most counts/word

    for word in dict.keys():                            # copy library into list of two item lists with count first for easy sort
        output_list.append([dict[word], word])

    output_list.sort(reverse=True)                      # sort list of counts/word with largest count first

    max_list = [output_list[0][1]]                      # make a list of words starting with the top of sorted list

    for x in output_list[1:]:                           # check the rest of the list for equal counts/word
        if x[0] == output_list[0][0]:
            max_list.append(x[1])
        else:                                           # don't waste time on the rest of the list
            break
    return max_list                                     # return list of keys for top counts/word entries

####################### BODY

import sys

document = open(sys.argv[1], 'r')
output_list = []

my_dict = find_words_of_len(document, int(sys.argv[2]))
comm_words = dict_max_value(my_dict)

for entry in comm_words:
    print str(entry), my_dict[entry]

document.close()