from xml.etree import ElementTree as ET

with open('nlp.txt.xml') as fr:
    lines = fr.readlines()

root = ET.fromstringlist(lines)
sentences = root.findall("document/sentences/sentence")
co_sentences = {}
for co_ref in root.findall("document/coreference/coreference"):
    mentions=[]
    for i, mention in enumerate(co_ref):
        if "representative" in mention.attrib:
            representative = i
        sent_id = int(mention.find('sentence').text)-1
        mentions.append((sent_id, mention.find('text').text))
        if sent_id not in co_sentences:
            co_sentences[sent_id] = " ".join(w.text for w in sentences[sent_id].findall('tokens/token/word'))

    for sent_id, text in mentions:
        sentence = co_sentences[sent_id]
        s = sentence.replace(text,f'[{text}]({mentions[representative][1]})')
        print(s)
