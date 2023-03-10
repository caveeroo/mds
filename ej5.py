import re

text = input()
expresion = r'\b(?:(?:C\/)|(?:Calle)) ([A-Z][a-zA-Z]+)[,\s]*(?:(?:[nN]º?\s?)?)(\d+),\s*(\d{5})\b'

result = re.findall(expresion, text)
for r in result:
    print(r[2] + '-' + r[0] + '-' + r[1])