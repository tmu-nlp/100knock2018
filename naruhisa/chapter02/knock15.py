if __name__ == '__main__':
  num = int(input('input number:'))
  tmp = list()
  for line in open('hightemp.txt'):
    tmp.append(line.strip())
  for i in range(len(tmp)):
    if i == num:
      break
    print(tmp[i-num])
  # tail -n [num] hightemp.txt
