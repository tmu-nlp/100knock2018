import sys
import math

file_name  = sys.argv[1]

n = int(sys.argv[2]) # 分割数N
num_line = math.ceil(sum(1 for line in open(file_name)) / n) # 1ファイルの行数

file = open(file_name,"r")

for i in range(n):
    f = open(f"result{i + 1}","w")
    for j in range(num_line):
        line = file.readline()
        f.write(line)
    f.close()

# split -l 6 hightemp.txt
# これは1ファイルの行数で分割数ではない