def main():
  correct_counts = 0
  line_counts = 0
  with open("knock92.txt", "r") as fin:
    for line in fin:
      words = line.strip().split()
      if words[3] == words[4]:
        correct_counts += 1
      line_counts += 1
  accurency = correct_counts / line_counts
  print(correct_counts)
  print(line_counts)
  print(accurency)

if __name__ == '__main__':
  main()