from knock21 import filter_english
from re import compile as regex

sod = regex(r'\{\{(?P<domain_key>\w+)\s+(?P<domain_value>\w+)\b')
eod = regex(r'\}\}')
kv_template = regex(r'\|(?P<key>\w+)\s=\s(?P<value>.+)')

def phase(lines):
    domain = None
    fields = {}
    for line in lines:
        if domain is None:
            start = sod.match(line)
            if start:
                domain = (start.group('domain_key'), start.group('domain_value'))
        elif eod.match(line):
            break
        else:
            result = kv_template.match(line)
            if result:
                # if last_value
                last_key = result.group('key')
                fields[last_key] = result.group('value')
            else:
                fields[last_key] += line
    return domain, fields

if __name__ == '__main__':
    domain, fields = phase(filter_english())
    print("{1}の{0}".format(*domain))
    for k,v in fields.items():
        print("%s:\t%s" % (k, v))
