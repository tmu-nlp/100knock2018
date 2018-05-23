from matplotlib import pyplot 
from knock36 import get_ordered_words

pyplot.rcParams['font.family'] = 'AppleGothic'

ordered_words = get_ordered_words()
top_ten_words = ordered_words[0:10]
x = []
y = []
for word in top_ten_words:
	x.append(word[0])
	y.append(word[1])
 
pyplot.bar(x, y)
pyplot.xlabel("単語")
pyplot.ylabel("頻度")
pyplot.show()