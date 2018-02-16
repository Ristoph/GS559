### First package using a function that returns fibonacci sequence with optional user defined starts

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