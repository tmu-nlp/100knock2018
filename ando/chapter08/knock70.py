import random

concat = []
for line in open("/Users/one/Downloads/rt-polaritydata/rt-polaritydata/rt-polarity.neg"):
    concat.append("-1 " + line)
for line in open("/Users/one/Downloads/rt-polaritydata/rt-polaritydata/rt-polarity.pos"):
    concat.append("+1 " + line)
random.shuffle(concat)
concat = "".join(concat)
with open("sentiment.txt","w")as f:
    f.write(concat)