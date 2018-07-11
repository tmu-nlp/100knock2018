import numpy as np

POS_PATH = "rt-polarity.pos"
NEG_PATH = "rt-polarity.neg"
TXT_PATH = "sentiment.txt"

def add_polarity_label(pos_path=POS_PATH, neg_path=NEG_PATH, txt_path=TXT_PATH):
	pos_array = []
	neg_array = []
	with open(POS_PATH, 'r', encoding='cp1252') as pos_file, open(NEG_PATH, 'r', encoding='cp1252') as neg_file, open(txt_path, 'w') as txt_file:
		for pos_line in pos_file:
			pos_array.append("+1\t" + pos_line)
		for neg_line in neg_file:
			neg_array.append("-1\t" + neg_line)
		both_array = pos_array + neg_array
		np.random.shuffle(both_array)
		txt_file.write("".join(both_array))
		print(f'positive: {len(pos_array)} \t negative: {len(neg_array)}')

if __name__ == '__main__':
	add_polarity_label()