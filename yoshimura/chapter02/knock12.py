import sys

in_file = open(sys.argv[1])
out_file1 = open("col1.txt","w")
out_file2 = open("col2.txt","w")


for line in in_file:
    line = line.strip()
    line_list = line.split("\t")

    out_file1.write(line_list[0] + "\n")
    out_file2.write(line_list[1] + "\n")

in_file.close()
out_file1.close()
out_file2.close()

# cut -f 1 hightemp.txt
# cut -f 2 hightemp.txt

