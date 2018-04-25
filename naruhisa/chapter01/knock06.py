from knock05 import ngram

if __name__ == '__main__':
  line1 = 'paraparaparadise'
  line2 = 'paragraph'
  X = set(ngram(line1, 2))
  Y = set(ngram(line2, 2))
  print(X | Y)
  print(X - Y)
  print(X & Y)
  text = ('s', 'e')
  print(text in X)
  print(text in Y) 
  
