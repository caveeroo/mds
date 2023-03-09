import re
text = input()

expresion = r'^\d{4}$'

results = re.search(expresion, text)
if results:
    print(results.group(0))
