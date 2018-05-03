from sys import argv

files = tuple(open(i) for i in argv[1:-1])
with open(argv[-1], 'w') as fw:
    for toks in zip(*files):
        fw.write("\t".join(t.rstrip() for t in toks))
        fw.write("\n")
for fr in files:
    fr.close()

# ls | paste - - # intersting -d "circular symbos", -s single_line
# sed = col1.txt | paste - -
# find / -name bin -type d | paste -s -d : - # auto make up PATH
# This command should be rename to rearrange
# paste col1.txt col2.txt > col_1_2.txt
