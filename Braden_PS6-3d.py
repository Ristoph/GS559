## 3d. (10 points) Write a program that takes two files each containing a matrix of integers, multiplies them using a
## function, and then prints the result. Remember that matrix multiplication is only valid for a matrix of size NxM (N
## rows, M columns) and one of size MxP (M rows, P columns), for any N, M, and P, and results in a matrix of size
## NxP.

import sys
import Braden_PS6_abpackage

first_matrix = Braden_PS6_abpackage.get_matrix(sys.argv[1])
second_matrix = Braden_PS6_abpackage.get_matrix(sys.argv[2])

product_matrix = Braden_PS6_abpackage.matrix_product(first_matrix, second_matrix)

if product_matrix == -1000:
    print "Dimensional mismatch"
else:
    print(Braden_PS6_abpackage.printable_matrix(product_matrix))