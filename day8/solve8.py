f = open('day8/input8', 'r')

unique_1 = 2
unique_4 = 4
unique_7 = 3
unique_8 = 7

outputs = []
for line in f.readlines():
    outputs.append(line.split('|')[1].strip().split(' '))

sum = 0


for output in outputs:
    for num in output:
        if len(num) == unique_1 or len(num) == unique_4 or len(num) == unique_7 or len(num) == unique_8:
            sum += 1

print(sum)