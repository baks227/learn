import random

first_team = [round(random.uniform(5,10),2) for _ in range(20)]
second_team = [round(random.uniform(5,10),2) for _ in range(20)]
winners = [(first_team[x] if first_team[x] > second_team[x] else second_team[x])
           for x in range(len(first_team))]

print('Первая команда: ',first_team,'\nВторая команда: ',
      second_team,'\nПобедители тура:',winners)