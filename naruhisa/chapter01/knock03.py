if __name__ == '__main__':
  text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
  text = text.replace(',', '').replace('.', '').split()
  answer = [len(line) for line in text]
  print(answer)
    
