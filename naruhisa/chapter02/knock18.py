if __name__ == '__main__':
  colum = list()
  for line in open('hightemp.txt'):
    colum.append(line.split())
  for line in sorted(colum, key = lambda x:x[2]):
    print('\t'.join(line))
