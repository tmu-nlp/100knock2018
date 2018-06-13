from sys import argv

assert len(argv) == 4
m = int(argv[2])
fw = None
with open(argv[1]) as fr:
    for i, line in enumerate(fr):
        if i % m == 0:
            if fw:
                fw.close()
            fw = open(argv[3].strip() + "%d" % (i // m), "w")
        fw.write(line)
if fw:
    fw.close()

# -l by line; -b by size in byte/kb/mb
# default prefix is x in working dir
# split -l $1 "hightemp.txt" prefix_
