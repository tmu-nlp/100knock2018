from gensim.models import word2vec
from knock90 import analogy

def main():
  with open("knock91.txt", "r") as fin, open("knock92.txt", "w") as fout:
    for line in fin:
      line = line.strip()
      words = line.split()
      try:
        result_word = analogy(words[1], words[0], words[2], 1)[0]
      except KeyError:
        result_word = ["NULL", "NULL"]
      
      fout.write(f"{line} {result_word[0]} {result_word[1]}\n")

if __name__ == '__main__':
  main()