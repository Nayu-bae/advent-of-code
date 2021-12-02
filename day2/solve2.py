f = open("day2/input2")

cords = []
depth = 0
hori = 0
aim = 0
result = 0
for line in f.readlines():
    z = line.split(" ")
    commando = z[0]
    number = int(z[1])
    
    if commando == "forward":
        hori = hori + number
        depth = depth + aim * number
    if commando == "down":
       # depth = depth + number
        aim = aim + number

    if commando == "up":
       # depth = depth - number
        aim = aim - number

print("Horizontal is ", hori)
print("Depth is ", depth)
result = hori * depth
print("Result is ", result)