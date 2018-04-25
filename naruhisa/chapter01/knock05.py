def ngram(text, n):
  return list(zip(*[text[i:] for i in range(n)]))

if __name__ == '__main__':
  text = 'I am an NLPer'
  print(ngram(text.replace(' ', ''), 2))
  print(ngram(text.split(), 2))
