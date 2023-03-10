import re

text = input()
expresion = r'\b(\d{4})-(\d{2})-(\d{2})\b'

def replace(match):
    return match.group(3) + '-' + match.group(2) + '-' + match.group(1)

result = re.sub(expresion, replace, text)
print(result)