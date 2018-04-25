import random
str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

word_list = str.split(" ")
for word in word_list:
    if len(word) > 4:
        chair_list = list(word[1:-1])
        random.shuffle(chair_list)
        word_list[word_list.index(word)] = word[0] + "".join(chair_list) + word[-1]

str = " ".join(word_list)
print(str)

    

    