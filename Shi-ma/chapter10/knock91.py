import re

if __name__ == '__main__':
    with open('../data/questions-words.txt', 'r') as data_in, open('result/knock91.txt', 'w') as data_out:
        print(re.search(r'(?<=: family\n).+?(?=\n^: )', data_in.read(), flags=(re.DOTALL | re.MULTILINE)).group(), file=data_out)