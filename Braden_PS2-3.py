### Chris Braden PS2 question 3
##
## GIVEN: an input file to copy and a name for the copied file
## RETURN: the input file copied to a new file named with the filename

import sys

original_file = open(sys.argv[1], "r") #open the file named in the first arg
original_content = original_file.read() #read the file content to a variable

copy_file = open(sys.argv[2], "w") #create a file with a name supplied in the second arg
copy_file.write(original_content) #write the contents of original file to new file

original_file.close() #close opened files
copy_file.close()

print 'File copying is complete!'