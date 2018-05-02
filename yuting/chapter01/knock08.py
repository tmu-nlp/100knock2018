def cipher(target):
	result =''
	for c in target:
		if c.islower():
			result += chr(219 - ord(c))
		else:
			result += c
	return result

target = input('please input-->')

result = cipher(target)
print('hint:' + result)

result2 = cipher(result)
print('recover:' + result2)

if result2 != target:
	print('miss')
