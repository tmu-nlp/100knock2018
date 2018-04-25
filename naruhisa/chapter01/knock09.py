import random

def text_shuffle(text):
  ans = ''
  for line in text.split():
    print(line)
    if len(line) < 4:
      ans += line
      continue
    first = line[0]
    last = line[-1]
    line = line[1:-1]
    line = sorted(line, key = lambda k: random.random()) 
    ans += first + ''.join(line) + last
  return ans
    
    

if __name__ == '__main__': 
  text = 'I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
  print(text_shuffle(text))
