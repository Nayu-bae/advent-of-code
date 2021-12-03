f = open("day3/input3") 
#first challenge.. gives out gamma.. epsilon is opposite.. binary to dezi.. multiply 
ones = [0,0,0,0,0,0,0,0,0,0,0,0]
zeros = [0,0,0,0,0,0,0,0,0,0,0,0]


for line in f.readlines():
    
    z = line.split(" ")
    bits = z[0]
    bits.split()
    for i in range(12):
        if bits[i] == "1":
            ones[i] = ones[i] + 1
    
        if bits[i] == "0": 
            zeros[i] = zeros[i] + 1   
    


for x in range(12):
    if ones[x] > zeros[x]:
        print(1)
    
    if ones[x] < zeros[x]:
        print(0)
        