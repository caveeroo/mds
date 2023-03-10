import re
text = input()

expresion = r"(?<!-)\b[0-9]{4}\b"

results = re.search(expresion, text)
if results:
    print(results.group(0))
