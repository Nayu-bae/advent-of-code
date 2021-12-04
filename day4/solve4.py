import copy
f = open("day4/input4") 

saves = []
#puts input into saves
for lines in f.readlines():
    saves.append(lines.strip())

#splitting first row into single numbers + cutting out ","
drawNumbers = saves[0]
singleNumbers = drawNumbers.split(",")

#deleting first 2 rows from input, so we can continue with the bingo fields 
saves.pop(0)
saves.pop(0)

#deleting empty rows
saves[:] = [x for x in saves if x]

#splitting the bingo fields in each 5 rows 
chunked_saves = list()
chunk_size = 5
for n in range(0, len(saves), chunk_size):
    chunked_saves.append(saves[n:n+chunk_size])

#get all fields into a 2D array : "table"
number_grid = [[1],[2],[3],[4],[5]]
tables = []
for u in chunked_saves:
    inputNumber = u
    for x in range(5):
        number_grid[x] = inputNumber[x].split(" ")
        number_grid[x][:] = [int(x) for x in number_grid[x] if x]
    tables.append(number_grid.copy())
tableCopy = copy.deepcopy(tables)

#check function
def is_winner(table):
    for row in table:
        winnerCounter = 0
        for col in row:
            if col == -1:
                winnerCounter += 1
        if winnerCounter == 5:
            return 1
        
    for col in range(5):
        winnerCounter = 0
        for row in range(5):
            if table[row][col] == -1:
                winnerCounter += 1
        if winnerCounter == 5:
            return 1    
    return 0        

#checking the 2D array with the given numbers
gotWinner = 0
tableCounter = 0
winnerTable = 0
winnerNumber = 0
for check in singleNumbers:
    tableCounter = 0
    for table in tables:
        for row in range(5):
            for col in range(5):
                if int(check) == table[row][col]:
                    table[row][col] = -1
        if is_winner(table) == 1 and gotWinner == 0:            
            gotWinner = 1
            winnerTable = tableCounter
            winnerNumber = check
            break
        tableCounter +=1
    if gotWinner == 1:
        break
print(tables[winnerTable], winnerNumber)