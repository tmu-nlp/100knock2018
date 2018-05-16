from knock25 import phase
from knock26 import remove_pair, wiki_stress
from knock27 import wiki_inner_link
from knock21 import filter_english
from re import compile as regex

wiki_template = r"(\{\{)(?P<content_template>.+?)(\}\})"

if __name__ == "__main__":
    domain, fields = phase(filter_english())
    fields = remove_pair(fields, wiki_inner_link, wiki_stress, wiki_template)
    print("{1}の{0}".format(*domain))
    for k,v in fields.items():
        print("%s:\t%s" % (k, v))
