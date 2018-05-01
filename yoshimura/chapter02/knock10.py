import sys

file_name = sys.argv[1]
with open(file_name) as file:
    count = sum(1 for line in file)
print(count)

# wc -l hightemp.txt
# 結果の空白

