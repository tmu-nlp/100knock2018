sentence ="I am an NLPer"
chargram = [sentence[i:i+2] for i in range(len(sentence)-1)]
words = [word.strip(".,") for word in sentence.split()]
wordgram = ["-".join(words[i:i+2]) for i in range(len(words)-1)]

print(chargram)
print(wordgram)