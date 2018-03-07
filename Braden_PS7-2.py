def super_sort(a, b):
    a_low = a.lower()
    b_low = b.lower()
    if a_low < b_low:
        return -1
    elif b_low > b_low:
        return 1
    elif a_low == b_low:
        sublist = [a,b]
        sublist.sort()
        if sublist == [a,b]:
            return -1
        elif sublist == [b,a]:
            return 1
    else:
        return 0

mylist = ['Jim', 'jim', 'Jimmy', 'jiM', 'elhanan', 'Elhanan']
mylist.sort(super_sort)
print mylist
