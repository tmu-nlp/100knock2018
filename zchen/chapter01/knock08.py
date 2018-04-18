def cipher(s):
    return "".join(chr(219 - ord(i)) if ord("a") <= ord(i) <= ord("z") else i for i in s)

test1 = "Today is 18.April.2018."
print("Test '%s':" % test1, cipher(test1))
