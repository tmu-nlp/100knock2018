'''
81. 複合語からなる国名への対処
英語では，複数の語の連接が意味を成すことがある．例えば，アメリカ合衆国は"United States"，
イギリスは"United Kingdom"と表現されるが，"United"や"States"，"Kingdom"という単語だけでは，
指し示している概念・実体が曖昧である．そこで，コーパス中に含まれる複合語を認識し，複合語を1語として扱うことで，
複合語の意味を推定したい．しかしながら，複合語を正確に認定するのは大変むずかしいので，ここでは複合語からなる国名を認定したい．

インターネット上から国名リストを各自で入手し，80のコーパス中に出現する複合語の国名に関して，
スペースをアンダーバーに置換せよ．例えば，"United States"は"United_States"，"Isle of Man"は"Isle_of_Man"になるはずである．
'''
from tqdm import tqdm

countries = set()
for line in open('countries', 'r'):
    countries.add(line.split(' ')[0])

with open('corpus81', 'w') as f:
    for line in tqdm(open('corpus.txt', 'r')):
        words = set(line.rstrip().split(' '))
        if countries & words:
            for country in open('countries', 'r'):
                country = country.rstrip()
                line = line.replace(country, country.replace(' ', '_'))
        f.write(line)


        
