if __name__ == '__main__':
    txt = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    id_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]

    ans_dict = dict()
    for id_, word in enumerate(txt.split()):
        if id_ + 1 in id_list:
            ans_dict[word[0]] = id_ + 1
        else:
            ans_dict[word[:2]] = id_ + 1

    print(ans_dict)
