def cipher(text):
  answer = ''
  for word in text:
    if word >= 'a' and word <= 'z':
      word = chr(219 - ord(word))
    answer += word
  return answer
if __name__ == '__main__':
  text = 'abcdefgABCDEFG'
  print('origin:', text)
  print('encode:', cipher(text))
  print('decode:', cipher(cipher(text)))
