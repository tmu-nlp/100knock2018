def cipher(s):
    enc = []
    for c in s:
        enc.append(__map_char(c))
    return ''.join(enc)

def __map_char(c):
    '''
    convert char with code between 97 to 122
    to 219 - charcode
    => map [a to z] to [z to a]
    '''
    # ord('a') # 97
    # ord('z') # 122
    offset = 219
    o = ord(c)
    if (97 <= o) and (o <= 122):
        return chr(offset - o)
    else:
        return c

if __name__ == '__main__':
    s = 'I am a NLPer'
    e = cipher(s)

    print(f'Encripted: {e}')
    print(f'Decripted: {cipher(e)}')