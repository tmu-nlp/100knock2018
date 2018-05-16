import json

# Note: json.load([line] or [file]) not work! should use json.loads(line)

def get_text():
	with open('../jawiki-country.json', 'r') as f:
		for line in f:
			line_json = json.loads(line)
			if line_json["title"] == "イギリス":
				return line_json['text']

if __name__ == '__main__':
	print(get_text())