from knock11 import hightemp

if __name__ == '__main__':
  col1 = open('col1.txt', 'w')
  col2 = open('col2.txt', 'w')
  for line in hightemp():
    line = line.split()
    col1.write(line[0] + '\n')
    col2.write(line[1] + '\n')
  col1.close()
  col2.close()
  hightemp()
  #cut -f[num] hightemp.txt > file.txt
