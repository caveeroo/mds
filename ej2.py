import re
text = input()
expresion = r'^(?:E[- ]{0,1})?\d{4}[- ]{0,1}[A-Z]{3}$'

results = re.search(expresion, text)
if results:
    print(results.group(0))
