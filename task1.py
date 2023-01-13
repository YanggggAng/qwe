import numpy

f = open("/Users/yang/PycharmProjects/pythonProject4/filename.txt", "r")
print("Statistics Summary")

sum = 0
count = 0
data = []
for line in f:
    sum += int(line)
    count += 1
    data.append(int(line))

mean = float(sum) / float(count)
std = numpy.std(data)
min = min(data)
max= max(data)

print("mean: " + str(mean))
print("std: " + str(std))
print("min: " + str(min))
print("max: " + str(max))