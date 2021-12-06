
from typing import ParamSpecArgs


f = open("day6/input6")


fish = []
for line in f.readlines():
    fish.append(line.split(","))    
    fishies = fish[0]

intfishies = []
for fishiesarray in fishies:
    intfishies.append(int(fishiesarray))



for round in range(80):
    for i in range (len (intfishies)):
        
        if  intfishies[i] > 0:
            intfishies[i] -= 1
        elif intfishies[i] == 0:
            intfishies[i] += 6
            intfishies.append(8)

print(len(intfishies))  