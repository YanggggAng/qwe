import numpy
import sys

filenames = [x for x in sys.argv][1:]

files = []

for filename in filenames:
    f = open(filename, "r")
    files.append(f)
    

print("Statistics Summary")

count = 0

for f in files:
    Lines = f.readlines()
    #sum = 0
    data = []
    for line in Lines:
    #    sum += int(line)
    #    count += 1
        data.append(int(line))

    #mean = float(sum) / float(count)
    mean = sum(data)/len(data)
    std = numpy.std(data)
    mini = min(data)
    maxi = max(data)

    print(filenames[count])
    print(f"mean: {mean} std: {std} min: {mini} max {maxi} n: {len(Lines)}")
    count = count +1
    f.close()

