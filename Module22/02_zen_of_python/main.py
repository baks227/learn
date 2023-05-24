
def rec_zen(text):
    rec_file = []
    for stroka in text.split('\n'):
        rec_file.append(stroka)
    for image in reversed(rec_file):
        print(image)

this_file = open('zen.txt','r')
data = this_file.read()
this_file.close()
rec_zen(data)