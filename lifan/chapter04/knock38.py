from matplotlib import pyplot 
from knock36 import get_ordered_words

pyplot.rcParams['font.family'] = 'AppleGothic'

ordered_words = get_ordered_words()
top_ten_words = ordered_words[0:100]

x = []
for word in top_ten_words:
	x.append(word[1])

pyplot.hist(x, bins=100)
pyplot.show()