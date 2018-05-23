if __name__ == '__main__':
  colum = set()
  for line in open('hightemp.txt'):
    colum.add(line.split()[0])
  print(len(colum))
