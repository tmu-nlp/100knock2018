import re
import json

def pass_string(string):
    return string

def fundamental_data(file, func):
    response = []
    data = {}
    start = re.compile(r"\{\{基礎情報")
    end = re.compile(r"\}\}")
    row = re.compile(r"^\s?\|?\s?(.+?)\s?=(.*)\|?")
    flag = False

    pre_key = None
    for line in file:
        if start.match(line):
            flag = True
            continue

        if end.match(line):
            flag = False

        if flag:
            l = row.match(line)

            if l:
                data[l.group(1).strip()] = func(l.group(2).strip())
                pre_key = l.group(1).strip()

            else:
                m = re.match(r"(.*)\}\}$", line)

                if m:
                    data[pre_key] += func(m.group(1).strip())
                    flag = False

                else:
                    data[pre_key] += func(line.strip())
        else:
            if len(data) > 0:
                response.append(data.copy())
                data.clear()

    return response

if __name__ == "__main__":
    inputfile = 'jawiki.txt'
    outputfile = 'jawiki-fundamental.json'
    f = open(inputfile)
    res = fundamental_data(f, pass_string)
    with open(outputfile, 'w') as g:
        json.dump(res, g, ensure_ascii=False)
