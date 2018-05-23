# -*- coding: utf-8 -*-
from matplotlib import pyplot 
from knock36 import get_ordered_words

pyplot.rcParams['font.family'] = 'AppleGothic'

ordered_words = get_ordered_words()
top_ten_words = ordered_words[0:100]

freq = []
for word in top_ten_words:
	freq.append(word[1])
    
pyplot.loglog(freq)
pyplot.show()