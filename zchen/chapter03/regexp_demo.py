# -*- coding: utf-8 -*-
from re import compile as regex

data = '"1", "2"'
s = regex(r'(")\w+?(\1)')
for i in s.finditer(data):
    print(i)
print(s.sub('~', data))
print(s.subn('~', data))
print(s.split(data))

word = "prefix-core-mets-suffix"
r = regex(r'prefix-(?P<stem>\w+)(-\w+)(?:-suffix)|(?P<named>\.?)')
print("group() = search/match/cover:", r.search(word).group())
print("group(0) is the same:", r.search(word).group(0))
print("a named group can be indexed:", r.search(word).group(1))
print("Group at position", r.search(word).groups(), "ungrouped affixes will not appear.")
print("Named group:", r.search(word).groupdict(0))
