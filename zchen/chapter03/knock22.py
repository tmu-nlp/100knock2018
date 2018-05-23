from knock21 import line_with_category
from re import compile as regex

# Need NOT define affixes like this
# get_category = compile(r'(?<=Category:).+(?=\W+)')
# explictly define it and extract with group WITH a name or number
get_category = regex(r'Category:(?P<category>.+?)\|*\**\]\]')
for line in line_with_category():
    result = get_category.search(line)
    if result:
        print(result.group(1))
