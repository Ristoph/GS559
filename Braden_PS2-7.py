### Chris Braden PS2 question 7
##
## GIVEN: two fasta files and a filename
## RETURN: a single file containing all the information in the two inputs

import sys

file1 = open(sys.argv[1], "r") # read user supplied file names and open files
file2 = open(sys.argv[2], "r")
file_name = sys.argv[3] # read user supplied name for combined file

combined_file = open(file_name, "w") # create a file with specified name

data_file1 = file1.readlines() # read lines of user supplied files
data_file2 = file2.readlines()

if (data_file1[len(data_file1)-2:len(data_file1)-1].count('\n') == 0): # adding carriage returns to first file if absent b/c ocd
    data_file1.append('\r\n')
    data_file1.append('\r\n')
elif (data_file1[len(data_file1)-2:len(data_file1)-1].count('\n') == 1):
    data_file1.append('\r\n')

data_file1 = ''.join(data_file1) # convert file lists to strings
data_file2 = ''.join(data_file2)

combined_data = (data_file1 + data_file2) # concatenate data strings from user supplied files
combined_file.write(combined_data) # write newly combined string to previously created new file

file1.close() # close files
file2.close()
combined_file.close()