def cipher(txt):
    txt_cip = ''
    for char in txt:
        txt_cip += chr(219 - ord(char)) if char.isalpha() and char.islower() else char

    return txt_cip

if __name__ == '__main__':
    txt = 'Hello World!! ハローワールド！！'
    print(cipher(txt))
