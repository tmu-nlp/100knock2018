from knock90 import similarity

def main():
  with open("combined.csv", "r") as fin, open("knock94.txt", "w") as fout:
    for line in fin:
      line = line.strip()
      words = line.split(",")
      try:
        word_sim = round(similarity(words[0], words[1]) * 10, 2)
      except KeyError:
        word_sim = 0
      fout.write(f"{line},{word_sim}\n")

if __name__ == '__main__':
  main()