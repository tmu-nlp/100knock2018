import random



def create_sentiment(path_data_in_pos, path_data_in_neg):
    sentiment = []
    with open(path_data_in_pos, 'r', encoding='latin-1') as data_in_pos:
        for txt_pos in data_in_pos:
            sentiment.append('+1 ' + txt_pos.strip())

    with open(path_data_in_neg, 'r', encoding='latin-1') as data_in_neg:
        for txt_neg in data_in_neg:
            sentiment.append('-1 ' + txt_neg.strip())

    return random.sample(sentiment, len(sentiment))


if __name__ == '__main__':
    path_data_in_pos = '../data/rt-polaritydata/rt-polaritydata/rt-polarity.pos'
    path_data_in_neg = '../data/rt-polaritydata/rt-polaritydata/rt-polarity.neg'

    sentiment = create_sentiment(path_data_in_pos, path_data_in_neg)

    with open('result/sentiment.txt', 'w') as data_out:
        for line_random in sentiment:
            print(line_random, file=data_out)

# cut -d ' ' -f 1 result/sentiment.txt | sort | uniq -c | sort -nr
