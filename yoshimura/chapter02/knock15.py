import sys 

file_name = sys.argv[1]
n = int(sys.argv[2])

with open(file_name,"r") as file:
    line_list = file.readlines()
    for line in line_list[-n:]:
        print(line.strip())

# tail -3 hightemp.txt