f = open("day5/input5")

table = [[0 for y in range(1000)] for x in range(1000)]
for line in f.readlines():
    
    cords = line.split("->")
    cords1ew = cords[0].split(",")
    cords2ew = cords[1].split(",")
    cords1 = [int(cords1ew[0]), int(cords1ew[1])]
    cords2 = [int(cords2ew[0]), int(cords2ew[1].strip())]
    cordx1 = cords1[0]
    cordy1 = cords1[1]
    cordx2 = cords2[0]
    cordy2 = cords2[1]

    
    if cordx1 < cordx2 and cordy1 == cordy2:
        cordxminus = cordx2 - cordx1
        for counter in range(cordxminus +1):
            count = cordx1 + counter
            table[count][cordy1] +=1

    if cordx1 > cordx2 and cordy1 == cordy2:
        cordxminus = cordx1 - cordx2
        for counter in range(cordxminus +1):
            count =  cordx1 - counter
            table[count][cordy1] +=1 

    if cordy1 < cordy2 and cordx1 == cordx2:
        cordyminus = cordy2 - cordy1
        for counter in range(cordyminus +1):
            count = cordy1 + counter
            table[cordx1][count] +=1
    
    if cordy1 > cordy2 and cordx1 == cordx2:
        cordyminus = cordy1 - cordy2
        for counter in range(cordyminus +1):
            count = cordy1 - counter
            table[cordx1][count] +=1

result = 0
for row in table:
    for num in row:
        if num >= 2:
            result +=1
print(result)