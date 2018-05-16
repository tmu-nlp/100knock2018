def gettemplate(x,y,z):
	result = '%s時の%sは%s' % (x,y,z)
	return result

s = gettemplate(12,'気温',22.4)
print(s)
