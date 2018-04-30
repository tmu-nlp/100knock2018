if __name__ == '__main__':
    txt = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

    txt_ans_list = list(map(lambda x: len(x), txt.replace(',', '').replace('.', '').split()))
    print(txt_ans_list)
