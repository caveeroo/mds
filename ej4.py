import re
text = input()


expresion = r'\b([a-zA-Z]\.([a-zA-Z]{2,})\.(\d{4})@alumnos\.urjc\.es)|(([a-zA-Z]+)\.([a-z-A-Z]+)@urjc\.es)\b'

def myprint(match):
    while("" in match):
        match.remove("")

    if '@alumnos.urjc.es' in match[0]:
        print("alumno " + match[1] + " matriculado en " + match[2])
    else:
        print("profesor " + match[1] + " apellido " + match[2])

results = re.findall(expresion, text)
for match in results:
    myprint(list(match))