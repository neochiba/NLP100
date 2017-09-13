#coding UTF-8
import json
import gzip
import re

f = "jawiki-country.json.gz"

def UK():
    with gzip.open(f, 'r') as data_file:
        for line in data_file:
            obj = json.loads(line)
            if obj['title'] == 'イギリス':
                return obj['text']

pattern = r'^(==*)\s?(.*)\1$'
repatter = re.compile(pattern, re.MULTILINE)

answer = repatter.findall(UK())

for i in answer:
    num = len(i[0])
    print(i[1], num)
