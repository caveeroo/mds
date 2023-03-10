import re
text = input()
expresion = r'\b(?:E[- ]{0,1})?\d{4}[- ]{0,1}[A-Z]{3}\b'

results = re.findall(expresion, text)
for match in results:
    print(match)
