def gen_text(x, y, z):
  return '{}時の{}は{}'.format(x, y, z)

if __name__ == '__main__':
  print(gen_text(12, '気温', '22.4'))
