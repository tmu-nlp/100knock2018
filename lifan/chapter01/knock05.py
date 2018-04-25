def get_word_bigram(sentence):
	word_result = []
	words = sentence.split(' ')
	for i in range(len(words)-1):
		word_result.append(words[i]+words[i+1])
	return word_result

def get_string_bigram(sentence):
	string_result = []
	words = sentence.split(' ')
	for i in range(len(sentence)-1):
		string_result.append(sentence[i]+sentence[i+1])
	return string_result

get_word_bigram("I am an NLPer")
get_string_bigram("I am an NLPer")