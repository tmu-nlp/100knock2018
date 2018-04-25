def cipher(str):
    result = ""
    for c in str:
        if c.islower():
            result += chr(219 - ord(c))
        else:
            result += c
    return result 


if __name__ == "__main__":
    str = "I am a NLPer"
    print(cipher(str))
    print(cipher(cipher(str)))

