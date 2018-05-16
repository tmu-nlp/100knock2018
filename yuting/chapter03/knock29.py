import requests
import json

inputfile = 'jawiki-markup.json'
outputfile = 'jawiki-nationalflags.txt'

with open(inputfile, 'r') as f:
    template = json.load(f)

wikipedia_api = "http://ja.wikipedia.org/w/api.php?"
prop = {
    'action': "query",
    'prop': "imageinfo",
    'iiprop': "url",
    'format': "json",
    'formatversion': '2',
    'utf8': '',
    'continue': ''
}

g = open(outputfile, "w")

for country in template:
    if u'国旗画像' in country:
        countryname = country[u'略名']
        filename = country[u'国旗画像']
        prop['titles'] = "Image:" + filename
        res = requests.get(url=wikipedia_api, params=prop)
        datum = json.loads(res.text)
        try:
            file_url = datum['query']['pages'][0]['imageinfo'][0]['url']
        except:
            print(datum)
            break
        print(filename, file_url)
        g.write(countryname.replace('|', ''))
        g.write(", %s\n" % file_url)
