if __name__ == '__main__':
    txt01 = 'パトカー'
    txt02 = 'タクシー'

    txt_ans = ''.join([txt01[i] + txt02[i] for i in range(len(txt01))])

    print(txt_ans)
