#function to calc first n elements of fibonacci

# def fibber(a_n):
#     i=0
#     fib_list = []
#     for el in range(a_n):
#         if i == 0:
#             fib_list.append(0)
#         elif i == 1:
#             fib_list.append(1)
#         else:
#             new_num = fib_list[i-1] + fib_list[i-2]
#             fib_list.append(new_num)
#         i += 1
#     return fib_list
#
# import sys
#
# user_num = int(sys.argv[1])
# print fibber(user_num)

def fibber(a_n, first = 0, second = 1):
    fib_list = []
    i = 0
    for el in range(a_n):
        if el == 0: # this is the hard mode way to add user vals
            fib_list.append(first)
        elif el == 1:
            fib_list.append(second)
        else:
            new_num = fib_list[i-1] + fib_list[i-2]
            fib_list.append(new_num)
        i += 1
    return fib_list

import sys

user_num = int(sys.argv[1])
if len(sys.argv) == 2:
    print fibber(user_num)
elif len(sys.argv) == 3:
    user_first = int(sys.argv[2])
    print fibber(user_num, user_first)
elif len(sys.argv) == 4:
    user_first = int(sys.argv[2])
    user_second = int(sys.argv[3])
    print fibber(user_num, user_first, user_second)