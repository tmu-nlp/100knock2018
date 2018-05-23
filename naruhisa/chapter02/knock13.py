if __name__ == '__main__':
  with open('col1.txt', 'r') as f1, open('col2.txt', 'r') as f2, open('result13.txt', 'w') as o_f:
    for line1, line2 in zip(f1, f2):
      o_f.write(line1.strip() + '\t' + line2 )

