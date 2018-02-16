## 3c. (10 points) Using the functions you implemented above, write a program that takes two files each containing
## a matrix of integers, adds them together (entry-wise) using a function, and then prints the result. Remember
## that matrix addition is only valid for matrices of the same size.

import sys
import Braden_PS6_abpackage

first_matrix = Braden_PS6_abpackage.get_matrix(sys.argv[1])
second_matrix = Braden_PS6_abpackage.get_matrix(sys.argv[2])

total_matrix = Braden_PS6_abpackage.matrix_add(first_matrix, second_matrix)
print(Braden_PS6_abpackage.printable_matrix(total_matrix))