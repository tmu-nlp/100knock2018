import sys

file_name = sys.argv[1]
num_lines = sum(1 for line in open(file_name))
print(num_lines)

# wc -l hightemp.txt