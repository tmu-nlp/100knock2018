from knock25 import phase
from knock26 import remove_pair, wiki_stress
from knock21 import filter_english

wiki_inner_link = r"\[\[(?P<content_link>.+?)\]\]"

if __name__ == "__main__":
    domain, fields = phase(filter_english())
    fields = remove_pair(fields, wiki_inner_link, wiki_stress)
    print("{1}の{0}".format(*domain))
    for k,v in fields.items():
        print("%s:\t%s" % (k, v))
