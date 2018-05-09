from knock21 import filter_english
from re import compile as regex

fmt_level = "\033[%dm %d %s\033[0m"
color_scheme = {i-29:i+1 for i in range(31, 38)}
get_affix_eq = regex(r'(?P<prefix>==+)(?P<section>\S+?)(?P=prefix)')
for line in filter_english():
    result = get_affix_eq.search(line)
    if result:
        level = len(result.group('prefix'))
        print(fmt_level % (color_scheme[level], level, '\t' * (level - 2) + result.group('section')))
