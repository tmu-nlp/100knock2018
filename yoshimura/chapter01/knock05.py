def ngram(seq, n):
    ngram = []
    for i in range(len(seq)):
        if len(seq[i : i + n]) == n:
            ngram.append(seq[i : i + n])

    return ngram


if __name__ == "__main__":
    str = "I am an NLRer"
    word_ngram = str.split(" ")
    character_ngram = str
    n = 2

    print(f"単語{n}gram : {ngram(word_ngram, n)}")
    print(f"文字{n}gram : {ngram(character_ngram, n)}")