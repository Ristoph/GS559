### Chris Braden PS5 question 5
##
## GIVEN: a plaintext file and a query letter-length minimum
## RETURN: the most common word in the file with at least the minimum letter-length, and the number of times it occurs

def find_words_of_len(doc, word_len): # takes an open file and a minimum letter-length, returns a dictionary with words and counts
    word_index_dict = {}
    # word_list = []
    # word_index = 0
    for doc_line in doc: # read each document line
        doc_line = doc_line.strip() # remove special(whitespace?) characters
        doc_line = doc_line.split(' ') # divide into a list of words

        for word in doc_line: # with each word in document line
            word = word.lower() # ignore case
            # word = word.split() # divide into character list
            for bad_char in ['.', ',', "'", '"', '?', ';', ':', '-', '(', ')', '!']:
                word = word.replace(bad_char, '')
            # word = word.replace((x for x in ['.', ',', "'", '"', '?', ';', ':', '-', '(', ')', '!']), '') # not done
            if word != '':
                if len(word) >= word_len:
                    if word in word_index_dict.keys():
                        word_index_dict[word] = word_index_dict[word] + 1
                    else:
                        word_index_dict[word] = 1
                # word_list.append(word)
            else:
                continue
    # for word in word_list:
    #     if len(word) >= word_len:
    #         if word in word_index_dict.keys():
    #             word_index_dict[word] = word_index_dict[word] + 1
    #         else:
    #             word_index_dict[word] = 1
    #     word_index += 1
    return(word_index_dict)

def dict_max_value(dict):
    # m = max(dict)
    # print m, dict[m]
    # maxes = []
    # for word in dict:
    #     if int(dict[word]) == int(dict[m]):
    #         maxes.append(word)
    # # print maxes
    # return maxes

    for word in dict.keys(): # copy library into list of two item lists
        output_list.append([dict[word], word])

    output_list.sort(reverse=True)

    max_list = [[output_list[0][1], output_list[0][0]]]
    for x in output_list[1:]:
        if x[0] == output_list[0][0]:
            max_list.append([x[1], x[0]])
    return max_list

####################### BODY

import sys

document = open(sys.argv[1], 'r')
output_list = []

my_dict = find_words_of_len(document, int(sys.argv[2]))
comm_words = dict_max_value(my_dict)
# print comm_words

for entry in comm_words:
    print entry[0], entry[1]


document.close()