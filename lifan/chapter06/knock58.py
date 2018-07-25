import xml.etree.ElementTree as ET

tree = ET.parse('../files/nlp.txt.xml')

for token in tree.iter('coreference'):
	mention_list = []
	for mention in token.iter('mention'):
		attr = mention.attrib
		if 'representative' in attr:
			represent = mention.findtext('text')
		else:
			mention_list.append(mention.findtext('text'))
	print(f"{represent}\t{mention_list}")