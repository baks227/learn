import re
def analysis_herc(data):
    result = {}
    print('Содержимое файла text.txt:\n',data,'\n')
    for line in data:
        for word in line.split():
            result[word.lower()] = result.get(word.lower(), 0) + 1
    result = [(v, k) for k, v in result.items() if k !='.']
    result = sorted(result, reverse=True)
    return result

file_analys = open('text.txt','r')
data_analys = file_analys.read()
herc = analysis_herc(data_analys)
file_analys.close()
new_file = open('analysis.txt', 'w')
print('Содержимое файла analysis.txt')
for score,char in herc:
    new_file.write(str(char)+' '+str(round(score/12,3))+'\n')
    print(str(char)+' '+str(round(score/12,3)))
new_file.close()

