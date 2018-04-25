import itertools

str1 = "パトカー"
str2 = "タクシー"

result = ""
for (str1, str2) in itertools.zip_longest(str1, str2,fillvalue = ""):
    result += str1 + str2

print(result)



