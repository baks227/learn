import os
def customs_sort(data):
    return data[2]
def sort_tour(tour):
    tournament = {}
    for line in tour.split('\n'):
        try:
            score = line.split()[2]
            if int(score) > k and score in line:
                tournament[score]= (line.split()[1][0]+'. '+line.split()[0])
        except IndexError:
            k = int(line)
    return sorted(tournament.items(),reverse=True)

file_tour = open('first_tour.txt','r')
data_tour = file_tour.read()
data_sort = dict(sort_tour(data_tour))
file_tour.close()
file_tour_new = open('second_tour.txt','w')
file_tour_new.write(str(len(data_sort)))
i=0
for score,name in data_sort.items():
    i +=1
    file_tour_new.write('\n'+str(i)+') '+name+' '+str(score))
file_tour_new.close()
