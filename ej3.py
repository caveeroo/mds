import re
text = input()

expresion = r'(\d{4})-(\d{2})-(\d{2})'

results = re.search(expresion, text)
if results:
    lista = results.groups(0)
    replacement = lista[2] + "-" + lista[1] + "-" + lista[0]
    print(re.sub(expresion,replacement, text))
