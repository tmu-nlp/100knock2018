import re

def cipher(text):
    result = re.match('[a-z]',text)
    if not isinstance(result,type(None)):
        text = 219-ord(text)
    return text
phrase = "IWasSoHappy"
phrase = list(phrase)
for i in phrase:
    print(cipher(i))