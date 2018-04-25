def cipher(my_string):
	str_list = list(my_string)
	for i in range(len(str_list)):
		if str_list[i].islower():
			str_list[i] = chr(219 - ord(str_list[i]))
	return "".join(str_list)

print("原文:", "helloADFhasdf")
print("暗号文:", cipher("helloADFhasdf"))