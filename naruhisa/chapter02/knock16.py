def output_sentences(sentences, number):
  o_f = open('output{}.txt'.format(number), 'w')
  for line in sentences:
    o_f.write(line + '\n') 
  o_f.close()
  return 0

if __name__ == '__main__':
  num = int(input('input number:'))
  for count, line in enumerate(open('hightemp.txt')):
    pass
  sentences = list()
  number = 0
  for c, line in enumerate(open('hightemp.txt')):
    print(line, c, count, num)
    if c % int(count / num) == 0 and c != 0:
      output_sentences(sentences, number)
      sentences = [line]
      number += 1
    else:
      sentences.append(line)
      
    
