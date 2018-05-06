import sys

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

with open(input_file_name,'r') as input_file:
    with open(output_file_name,'w') as output_file:
        for line in input_file:
            # output_file.write(line.expandtabs(1))
            output_file.write(line.replace("\t"," "))

# gsed -e 's/\t/ /g' hightemp.txt
# tr '\t' ' ' < hightemp.txt
# expand -t 1 hightemp.txt
