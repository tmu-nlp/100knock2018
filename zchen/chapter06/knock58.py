from collections import defaultdict
from xml.etree import ElementTree as ET

with open('nlp.txt.xml') as fr:
    lines = fr.readlines()
sentences = ET.fromstringlist(lines).findall('document/sentences/sentence')

def extract_type(sentences):
    for i, sentence in enumerate(sentences):
        print('\nsentence', i)

        tokens = []
        for dep in sentence.findall("./dependencies[@type='collapsed-dependencies']/dep"):
            tokens.append((dep[0].text, dep[1].text, dep.get("type")))

        for  (px, cx, typex) in tokens:
            if typex == "nsubj":
                print(f"{typex}: {px} <- {cx}")

                for (py, cy, typey) in tokens:
                    if px == cy:
                        print(f"  dobj({typey}): {py} <- {cy}")


print(extract_type(sentences))
