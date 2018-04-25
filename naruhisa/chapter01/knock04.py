if __name__ == '__main__':
  text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
  number = [1, 5, 6, 7, 8, 9, 15, 16, 19]
  text = text.split()
  answer = dict()
  for count, line in enumerate(text):
   if count + 1 in number:
     answer[line[0]] = count + 1
   elif count + 1 == 12:
     answer[line[0] + line[2]] = count + 1
   else:
     answer[line[0:2]] = count + 1
  print(answer)
