from knock90 import word_vector
from sklearn.externals import joblib

def main():
  country_name_dict = {}
  with open("country_names.txt", "r") as fin:
    for line in fin:
      line = line.strip()
      word = line.replace(" ", "_")
      try:
        country_name_dict[word] = word_vector(word)
      except:
        pass
  joblib.dump(country_name_dict, "country_name_dict.pkl")

if __name__ == '__main__':
  main()