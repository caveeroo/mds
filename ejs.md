# Plantilla

```python
import re
text = input()

expresion = '\\w+'

results = re.findall(expresion, text)
for match in results:
    print(match)
```

# Ejercicio 1

Enunciado:

Dato un texto de una sola línea, determinar todos los años (números formados estrictamente por 4
dígitos) que aparecen. Un año es una cadena numérica de longitud 4, con cualquier valor en el rango
[0000, 9999]. Se tendrán que imprimir por pantalla en el lenguaje deseado usando una expresión
regular todos los años que vienen en el texto en orden de aparición, en una línea cada uno

Expresión:

```
\d{4}
```
aasdfasfas
asdf