# Plantilla

```python
import re
text = input()
expresion = r''

results = re.search(expresion, text)
if results:
    print(results.group(0))
```

# Ejercicio 1

Enunciado:

Dato un texto de una sola línea, determinar todos los años (números formados estrictamente por 4
dígitos) que aparecen. Un año es una cadena numérica de longitud 4, con cualquier valor en el rango
[0000, 9999]. Se tendrán que imprimir por pantalla en el lenguaje deseado usando una expresión
regular todos los años que vienen en el texto en orden de aparición, en una línea cada uno

Expresión:

```
^\d{4}$
```

# Ejercicio 2

Dato un texto de una línea, determinar todas las matrículas que aparecen. Una matrícula es una
cadena que tiene las siguientes características:
• 4 dígitos seguida de un separador (guión, espacio o nada) y 3 letras en mayúsculas al final tal
que [0000 − AAA, ..., 9999 − ZZZ].
• Las matrículas pueden llevar una E mayúscula delante para indicar que se trata de un vehículo
especial. Ejemplos: E1337ZZZ, E-0000 PCB.
• Los dígitos pueden estar separadas de las letras utilizando un guión, un espacio, o ningún
separador.
Se tendrán que imprimir por pantalla usando el lenguaje elegido usando una expresión regular todas
las matrículas que vienen en el texto en orden de aparición

Expresión:

```
^(E[- ]{0,1})?\d{4}[- ]{0,1}[A-Z]{3}$
```

Una e opcional con la interrogación, separador opcional (si el separador es nada, se comple con el 0), cuatro dígitos obligatorio (\d), separador opcional y tres mayúsculas con el rango A-Z


Dado un formato de fechas yyyy-mm-dd, se pide convertir a dd.mm.yyyy.
Para cada match encontrado en los documentos propuestos se tendr  ́a que imprimir en el siguiente
formato (los rangos de fecha puede ser erroneos, pueden existir un mes 20).
• Para el caso “El profesor Isaac Lozano puso una fecha de entrega el 2023-04-16 a las 23:55”.
Se imprimir ́a “El profesor Isaac Lozano puso una fecha de entrega el 16.04.2023 a las 23:55”

Expresion: (\d{4})-(\d{2})-(\d{2})

Usamos grupos para poder hacer el replacement fácil luego.

Script: 
```python
import re
text = input()

expresion = r'(\d{4})-(\d{2})-(\d{2})'

results = re.search(expresion, text)
if results:
    lista = results.groups(0)
    replacement = lista[2] + "-" + lista[1] + "-" + lista[0]
    print(re.sub(expresion,replacement, text))
```