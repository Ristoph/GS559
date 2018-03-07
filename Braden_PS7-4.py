# 4A. (10 point) Write a function my_factorial(n) that calculates and returns the factorial of n
# (usually denoted by n!). Remember, n! is the product of all positive integers less than or equal to n.
# For example, 5! = 5 x 4 x 3 x 2 x 1 = 120. Note that according to the convention, the value of 0! is defined as 1.

import sys

def my_factorial(n):
    if n == 0:
        return 1
    i = 1
    n_factorial = n
    while n > i:
        n_factorial = n_factorial * (n-i)
        i += 1
    return n_factorial

# print my_factorial(int(sys.argv[1]))


# 4B. (10 point) Write a function my_choose(n,k) that calculates and returns the binomial coefficient (n),
# also known as "n choose k". Remember, the binomial coefficient can be calculated according to the following formula:
# Your solution should use the factorial function you wrote
# in part A of this question.

def my_choose(n,k):
    top = my_factorial(n)
    bottom = my_factorial(k)*(my_factorial(n-k))
    binomial = float(top/bottom)
    return binomial

my_n = int(sys.argv[1])
my_k = int(sys.argv[2])

print my_choose(my_n, my_k)