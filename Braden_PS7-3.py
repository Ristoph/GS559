# Write a function CalcDistance(point1, point2) that calculates the Euclidean distance between
# point1 and point2. Each point is given as a list of numbers that represent its coordinates in an ndimensional
# space. You can use the function math.pow(x,y) that returns x raised to the power y
# and the function math.sqrt(x) that returns the square root of x

import math
import sys

def CalcDistance(coord1, coord2):   #calculates the euclidean distance between two n-dimensional points
    squares_sum = 0
    for dim in range(len(coord1)):
        square_diff = math.pow((int(coord1[dim])-int(coord2[dim])), 2)
        squares_sum += square_diff
    return math.sqrt(squares_sum)


point1 = sys.argv[1]            # takes coordinate inputs as comma separated elements without whitespace
point1 = point1.split(',')

point2 = sys.argv[2]
point2 = point2.split(',')


euclid_dist = CalcDistance(point1, point2)

print point1, "and", point2, "are", euclid_dist, "apart"


