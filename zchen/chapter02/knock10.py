from sys import argv

with open(argv[1]) as fr:
    print(sum(1 for l in fr))

# echo number of lines:
# cat hightemp.txt | wc -l
