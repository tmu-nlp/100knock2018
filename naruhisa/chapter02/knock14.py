if __name__ == '__main__':
  num = input('input number:')
  for count, line in enumerate(open('hightemp.txt', 'r')):
    if count == int(num):
      break
    print(line.strip())
  #head -n [num] hightemp.txt
