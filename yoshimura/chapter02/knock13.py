import sys

col1 = sys.argv[1]
col2 = sys.argv[2]

file1 = open(col1,"r") 
file2 = open(col2,"r") 
result = open("result.txt","w")


for line1,line2 in zip(file1,file2):
    result.write(line1.strip() + "\t" + line2)

file1.close()
file2.close()
result.close()

# paste col1.txt col2.txt