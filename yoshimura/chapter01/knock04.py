str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
list = str.split(" ")
dict = {} 

for i in range(len(list)):
    if i + 1 in [1,5,6,7,8,9,15,16,19]:
        dict[list[i][0]] = i + 1
    else:
        dict[list[i][:2]] = i + 1

print(dict)


