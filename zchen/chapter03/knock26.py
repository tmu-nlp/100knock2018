from knock25 import phase
from knock21 import filter_english
from re import compile as regex

wiki_stress = r"'{3}(?P<content_stress>.+?)'{3}"

def remove_pair(fields, *pair_regex_with_content):
    rg = regex(r"|".join(pair_regex_with_content))
    for k,v in fields.items():
        new_v = ""
        prefix_pos = 0
        for anchor in rg.finditer(v):
            new_v += v[prefix_pos:anchor.start()]
            for meta_name, matched_value in anchor.groupdict().items():
                if matched_value and "content" in meta_name:
                    new_v += matched_value
                    prefix_pos = anchor.end()
        if prefix_pos > 0:
            fields[k] = new_v + v[prefix_pos:]
    return fields

if __name__ == "__main__":
    domain, fields = phase(filter_english())
    fields = remove_pair(fields, wiki_stress)
    print("{1}の{0}".format(*domain))
    for k,v in fields.items():
        print("%s:\t%s" % (k, v))
