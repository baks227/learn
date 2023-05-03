def sum(*nums):
    sum_ch = 0
    for num in nums:
        try:
            sum_ch +=sum(*num)
        except TypeError:
            sum_ch += num
    return sum_ch


#print('Ответ в консоли: ',sum([[1, 2, [3]], [1], 3]))