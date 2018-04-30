import sys
import math

file_name  = sys.argv[1]

n = int(sys.argv[2])
num_line = math.ceil(sum(1 for line in open(file_name)) / n)

file = open(file_name,"r")

for i in range(n):
    f = open(f"result{i + 1}","w")
    for j in range(num_line):
        line = file.readline()
        f.write(line)
    f.close()

# split -l 6 hightemp.txt
