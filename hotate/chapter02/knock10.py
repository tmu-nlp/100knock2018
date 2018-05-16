file = open('hightemp.txt')
print(len(file.readlines()))
file.close()

# wc -l hightemp.txt