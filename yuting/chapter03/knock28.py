import re
import json
from knock25 import fundamental_data
from knock26 import remove_emphasis
from knock27 import remove_internalLink

def remove_markup(string):
    markups = [
        re.compile(r"\[https?://[a-zA-Z0-9\./]+\s(.+)?\]"),
        re.compile(r"#REDIRECT\s?(.+)"),
        re.compile(r"<!--\s?(.+)\s?-->"),
        re.compile(r"\{\{.*[Ll]ang\|[a-zA-Z\-]+\|(.+)\}\}"),
        re.compile(r"(.*)<ref.+(</ref>)?>"),
        re.compile(r"(.*?)<br\s?/?>"),
        re.compile(r"<[a-z]+.*>(.*?)</[a-z]+>")
    ]
    removed_string = remove_internalLink(string)
    for m in markups:
        removed_string = m.sub(r"\1", removed_string)
    return removed_string

if __name__ == "__main__":
    inputfile = 'jawiki.txt'
    outputfile = 'jawiki-markup.json'
    f = open(inputfile)
    res = fundamental_data(f, remove_markup)
    with open(outputfile, 'w') as g:
        json.dump(res, g, ensure_ascii=False)

#markupを可能な限り除去し、国の基本情報を整形














