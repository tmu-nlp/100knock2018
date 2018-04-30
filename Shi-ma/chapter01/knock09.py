import random



def random_middle(word):
    middle = word[1:-1]
    random_middle = word[0] + ''.join(random.sample(middle, len(middle))) + word[-1]

    return random_middle


if __name__ == '__main__':
    txt = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    words = txt.strip().split()

    txt_ans_list = [word if len(word) <= 4 else random_middle(word) for word in words]
    txt_ans = ' '.join(txt_ans_list)

    print(txt_ans)
