f = open("day1/input1") 

counter = 0
last_measurement = 1000000000000
measurements = []
for line in f.readlines():
    measurements.append(int(line))


#print(measurements)

#for line in f.readlines():
#    measurement = int(line)
#    if measurement > last_measurement:
#        counter += 1
#    last_measurement = measurement




for i in range(len(measurements) -2):
    measurement = measurements[i] + measurements[i + 1] + measurements[i + 2]
    if measurement > last_measurement:
        counter += 1

    last_measurement = measurement



print(counter)