from gensim.models import word2vec

model = word2vec.Word2Vec.load("tokens.model")

def word_vector(word):
  return model.wv[word]

def similarity(a, b):
  return model.similarity(a, b)

def similar_words(word):
  return model.similar_by_word(word)

def analogy(a, b, c, n=10):
  new_vector = model.wv[a] - model.wv[b] + model.wv[c]
  return model.similar_by_vector(new_vector, topn=n)

def main():
  print("------------単語ベクトル---------")
  print(word_vector("United_States"))
  print("------------単語類似度---------")
  print(similarity("United_States", "U.S"))
  print("------------類似度のTop10---------")
  print(similar_words("England"))
  print("------------加法構成性によるアナロジー---------")
  print(analogy("Spain", "Madrid", "Athens"))

if __name__ == '__main__':
  main()