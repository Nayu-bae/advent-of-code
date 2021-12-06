states = [0, 0, 0, 0, 0, 0, 0, 0, 0]

inp = open('day6/input6', 'r')

for numstr in inp.read().split(','):
    num = int(numstr)
    
    states[num] += 1

print(states)


for round in range(256):
    temp = states.copy()
    states[0] = temp[1]
    states[1] = temp[2]
    states[2] = temp[3]
    states[3] = temp[4]
    states[4] = temp[5]
    states[5] = temp[6]
    states[6] = temp[7] + temp[0]
    states[7] = temp[8]
    states[8] = temp[0]

sum = 0
for i in range(len(states)):
    sum += states[i]

print(sum)