def hightemp():
  with open('hightemp.txt', 'r') as f:
    for line in f:
      yield line

if __name__ == '__main__':
  o_f = open('hightemp11.txt', 'w')
  for line in hightemp():
    line = line.replace('\t', ' ')
    o_f.write(line)
  o_f.close()
  hightemp()
  #cat hightemp.txt | tr '\t' ' ' > hightemp12.txt
