def qsort(arr):
    if len(arr)<=1:
        return arr
    opora = arr[-1]
    left =[]
    mid = []
    right = []
    for e in arr:
        if e < opora:
            left.append(e)
        elif e == opora:
            mid.append(e)
        else:
            right.append(e)
    return qsort(left)+mid + qsort(right)

list_num =  [5, 8, 9, 4, 2, 9, 1, 8]
print(qsort(list_num))
