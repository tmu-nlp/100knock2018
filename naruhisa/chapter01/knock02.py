if __name__ == '__main__':
  pata = 'パトカー'
  taxi = 'タクシー'
  answer = ''
  for line1, line2 in zip(pata, taxi):
    answer += line1 + line2
  print(answer)
