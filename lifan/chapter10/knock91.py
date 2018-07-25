def main():
  start_flag = False
  with open("questions_words.txt", "r") as fin, open("knock91.txt", "w") as fout:
    for line in fin:
      if line == ": family\n":
        start_flag = True
        continue
      elif line[:2] == ": ":
        start_flag = False
      if start_flag:
        fout.write(line)

if __name__ == '__main__':
  main()