import json
import re

f = open("jawiki-country.json").read()
line = f.split("\n")
for i in line:
  if "\"title\": \"イギリス\"" in i:
    kiji = json.loads(i)
    with open("igirisu.txt", "w") as fout:
	    fout.write(kiji["text"])