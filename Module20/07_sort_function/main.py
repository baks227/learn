def tpl_sort(nabor_num):
    for i_num in nabor_num:
        if i_num%1!=0:
            return nabor_num
    nabor_num = sorted(nabor_num)
    return nabor_num

#print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))