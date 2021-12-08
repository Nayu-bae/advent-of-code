
f = open("day7/input7")

positions = []
for line in f.readlines():
    positions.append(line.split(","))    
    position = positions[0]


    

pos = []
for x in position:
    pos.append(int(x))


ra = []
for i in range(max(pos)):
    fdif = 0
    for each in pos:
        dif = abs(i-each)
        xdif = dif * (dif + 1) / 2
        fdif = fdif + xdif

    ra.append(fdif)     



print(min(ra))