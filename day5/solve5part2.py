class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toString(self):
        return 'Point(' + str(self.x) + ', ' + str(self.y) + ')'

table = []
for i in range(1000):
    row = []
    for j in range(1000):
        row.append(0)
    table.append(row)

inp = open('day5/input5', 'r')

def checkVerticalLine(p1, p2):
    if(p1.y > p2.y):
        for i in range(p1.y - p2.y + 1):
            table[p1.y - i][p1.x] += 1
    else:
        for i in range(p2.y - p1.y + 1):
            table[p1.y + i][p1.x] += 1

def checkHorizontalLine(p1, p2):
    if(p1.x > p2.x):
        for i in range(p1.x - p2.x + 1):
            table[p1.y][p1.x - i] += 1
    else:
        for i in range(p2.x - p1.x + 1):
            table[p1.y][p1.x + i] += 1

def checkDiagonalLine(p1, p2):
    diff = abs(p1.x - p2.x)

    if p1.x > p2.x and p1.y < p2.y: 
        for i in range(diff + 1):
            table[p1.y + i][p1.x - i] += 1
    elif p1.x > p2.x and p1.y > p2.y:
        for i in range(diff + 1):
            table[p1.y - i][p1.x - i] += 1
    elif p1.x < p2.x and p1.y < p2.y:
        for i in range(diff + 1):
            table[p1.y + i][p1.x + i] += 1
    elif p1.x < p2.x and p1.y > p2.y:
        for i in range(diff + 1):
            table[p1.y - i][p1.x + i] += 1

for line in inp.readlines():
    p1 = Point(int(line.split('->')[0].split(',')[0]), int(line.split('->')[0].split(',')[1]))
    p2 = Point(int(line.split('->')[1].split(',')[0]), int(line.split('->')[1].split(',')[1]))

    if p1.x == p2.x:
        checkVerticalLine(p1, p2)
    elif p1.y == p2.y:
        checkHorizontalLine(p1, p2)
    else:
        checkDiagonalLine(p1, p2)

counter = 0
for i in range(1000):
    for j in range(1000):
        if table[i][j] >= 2:
            counter += 1

print(counter)