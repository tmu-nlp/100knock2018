from sys import argv

fmt = "col%d.txt"
files = tuple(open(fmt%i, "w") for i in range(2))

with open(argv[1]) as fr:
    for line in fr:
        for t, fw in zip(line.split("\t"), files):
            fw.write(t + "\n")

for fw in files:
    fw.close()

# for i in {1..2}
# do
#     cut -d $'\t' -f $i < hightemp.txt > "col${i}.txt"
# done
