### Chris Braden PS6 question 3
##
## 3a. (10 points) Write a function that reads in a file containing a matrix of integers and returns it as a 2-
## dimensional list (a list of lists) of integers (not strings).

def get_matrix(matrix_filename_a):
    matrix_file = open(matrix_filename_a, 'r')
    matrix = []
    for row in matrix_file.readlines():
        row = list(row.strip().split())
        row = [int(x) for x in row]
        matrix.append(row)
    matrix_file.close()
    return matrix

## 3b. (10 points) Write a function that takes a 2-dimensional list of integers and prints it in a pretty format -  with
## entries separated by tabs, and rows on different lines.

def printable_matrix(matrix_a):
    p_m = ''
    for row in matrix_a:
        printable_row = ''
        for x in row:
            if x < 0:
                printable_x = str(x) + '\t'
                printable_row = printable_row + printable_x
            elif x >= 0:
                printable_x = ' ' + str(x) + '\t'
                printable_row = printable_row + printable_x
        p_m = p_m + (printable_row + '\n')
    return p_m

## 3c. (10 points) Using the functions you implemented above, write a program that takes two files each containing
## a matrix of integers, adds them together (entry-wise) using a function, and then prints the result. Remember
## that matrix addition is only valid for matrices of the same size.

def matrix_add(matrix1_a, matrix2_a):
    sum_matrix = []
    if len(matrix1_a) == len(matrix2_a):
        if len(matrix1_a[0]) == len(matrix2_a[0]):
            for row in range(len(matrix1_a)):
                sum_matrix_row = []
                for col in range(len(matrix1_a)):
                    sum_x = int()
                    sum_x = matrix1_a[row][col]+matrix2_a[row][col]
                    sum_matrix_row.append(sum_x)
                sum_matrix.append(sum_matrix_row)
        else:
            return -1000
    else:
        return -1000
    return sum_matrix

## 3d. (10 points) Write a program that takes two files each containing a matrix of integers, multiplies them using a
## function, and then prints the result. Remember that matrix multiplication is only valid for a matrix of size NxM (N
## rows, M columns) and one of size MxP (M rows, P columns), for any N, M, and P, and results in a matrix of size
## NxP.

# i is the index of rows
# j is the index of column
# m is the index of the shared dimension
# to build rows with .append, I have to keep i constant first

def matrix_product(matrix1_a, matrix2_a):
    if len(matrix1_a[0]) == len(matrix2_a):
        prod_matrix = []
        for i in range(len(matrix1_a)):
            prod_matrix_row = []
            for j in range(len(matrix2_a[0])):
                prod_matrix_row_el = 0
                for m in range(len(matrix1_a[0])):
                    prod_matrix_row_el += (matrix1_a[i][m] * matrix2_a[m][j])
                    #print prod_matrix_row_el
                prod_matrix_row.append(prod_matrix_row_el)
            prod_matrix.append(prod_matrix_row)
    else:
        return -1000
    return prod_matrix