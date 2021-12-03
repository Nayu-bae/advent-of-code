f = open("day3/input3") 


saves = []
ones = [0,0,0,0,0,0,0,0,0,0,0,0]
zeros = [0,0,0,0,0,0,0,0,0,0,0,0]
result = 0


for lines in f.readlines():
    saves.append(lines.strip())
    
for round in range(12):
    losers = []
    for x in saves:
        bits = x
    
        if bits[round] == "1":
            ones[round] += 1
            
        if bits[round] == "0":
            zeros[round] += 1
        
    if ones[round] >= zeros[round]:
        result = 1
    else:
        result = 0
    
    for x in saves:
        if int(x[round]) != result:
            losers.append(x)
    
    for loser in losers:
        saves.remove(loser)
      

print(saves)


