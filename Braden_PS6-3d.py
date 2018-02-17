## 3d. (10 points) Write a program that takes two files each containing a matrix of integers, multiplies them using a
## function, and then prints the result. Remember that matrix multiplication is only valid for a matrix of size NxM (N
## rows, M columns) and one of size MxP (M rows, P columns), for any N, M, and P, and results in a matrix of size
## NxP.

import sys
import Braden_PS6_abpackage

def matrix_multiply(matrix1_a, matrix2_a):
    product_matrix = []
    if len(matrix1_a[0]) == len(matrix2_a):
        print "it works"
        for dim_n in range(len(matrix1_a)):
            dot_product = 0
            for dim_m in range(len(matrix1_a[0])):
                for dim_p in range(len(matrix2_a))
                    dot_product = dot_product + (matrix1_a[dim_n][dim_m]) x matrix2_a[dim_m][dim_p]
                



    else:
        print "mismatch"
        print len(matrix1_a[0]), len(matrix2_a)

first_matrix = Braden_PS6_abpackage.get_matrix(sys.argv[1])
second_matrix = Braden_PS6_abpackage.get_matrix(sys.argv[2])

matrix_multiply(first_matrix, second_matrix)