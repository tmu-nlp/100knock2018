import sys 
import linecache

file_name = sys.argv[1]
n = int(sys.argv[2])

with open(file_name,"r") as file:
    for i in range(n):
        print(file.readline().strip())



# head -3 hightemp.txt

