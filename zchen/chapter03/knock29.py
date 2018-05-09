from knock25 import phase
from knock21 import filter_english
from re import compile as regex
import requests

def get_response(name):
    params = {'action': 'query', 'format': 'json', 'prop': 'imageinfo', 'iiprop': 'url', 'titles': 'File:{}'.format(name)}
    response = requests.get('https://en.wikipedia.org/w/api.php', params)
    return response.json()

if __name__ == "__main__":
    domain, fields = phase(filter_english())
    mess = str(get_response(fields['国旗画像']))
    get_url = regex(r"'url':\s'(.+?)'")
    result = get_url.search(mess)
    print(result.group(1))
