# This function seems obsoleted in Py3
from functools import reduce
from operator import add

a = "パトカー"
b = "タクシー"

tos = reduce(add, zip(a, b))
print("".join(tos))
