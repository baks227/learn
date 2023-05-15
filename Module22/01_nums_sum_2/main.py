import os

num_file = open('numbers.txt','r')
sum_num = 0
data = num_file.read()
for num in data:
    if num != ' ' and num != '\n':
        num = int(num)
        sum_num += num
print('Содержимое файла numbers.txt\n',data)
num_file.close()
new_file = open('answer.txt','w')
new_file.write(str(sum_num))
print('Содержимое файла answer.txt\n',sum_num)
new_file.close()
