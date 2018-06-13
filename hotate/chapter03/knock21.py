from knock20 import extraction
import re

s = extraction('イギリス')
l = [line for line in s.split('\n') if 'Category' in line]
print(l)
