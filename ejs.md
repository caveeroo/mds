# Plantilla

```python
import re
text = input()
expresion = r''

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

```regex
(?<!-)\b[0-9]{4}\b
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

```regex
^(E[- ]{0,1})?\d{4}[- ]{0,1}[A-Z]{3}$
```

Una e opcional con la interrogación, separador opcional (si el separador es nada, se comple con el 0), cuatro dígitos obligatorio (\d), separador opcional y tres mayúsculas con el rango A-Z

# Ejercicio 3

Dado un formato de fechas yyyy-mm-dd, se pide convertir a dd.mm.yyyy.
Para cada match encontrado en los documentos propuestos se tendrá que imprimir en el siguiente
formato (los rangos de fecha puede ser erroneos, pueden existir un mes 20).
• Para el caso “El profesor Isaac Lozano puso una fecha de entrega el 2023-04-16 a las 23:55”.
Se imprimir ́a “El profesor Isaac Lozano puso una fecha de entrega el 16.04.2023 a las 23:55”

Expresion:

```regex
(\d{4})-(\d{2})-(\d{2})
```
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

# Ejercicio 4

Enunciado:

Dado un texto, determinar cuando se ha encontrado un email de alumno de nuestra universidad
“@alumnos.urjc.es” o profesor “@urjc.es”. Los emails de alumnos están formados del siguiente
patrón:
• Inicial del usuario seguido de punto
• Apellido del usuario, siempre mayor o igual a 2 caracteres.
• Seguidos de un punto y la fecha de matriculación
• todos finalizan con “@alumnos.urjc.es”

Los correos de los profesores constan de:
• Nombre del profesor seguido de un punto
• Apellido del profesor
• Finalizando con “@urjc.es”
Para cada match encontrado se tendrá que imprimir en el siguiente formato.
• Para el caso de prueba i.lozanoo.2015@alumnos.urjc.es reportaremos “alumno lozanoo matric-
ulado en 2015”
• Para un profesor reportaremos para el ejemplo isaac.lozano@urjc.es “profesor isaac apellido
lozano”

Expresion:

```regex
r'\b([a-zA-Z]\.([a-zA-Z]{2,})\.(\d{4})@alumnos\.urjc\.es)|(([a-zA-Z]+)\.([a-z-A-Z]+)@urjc\.es)\b'
```

Script:

```python
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
```

# Ejercicio 5

Enunciado:

Dado un texto devolver las direcciones postales.
Una dirección estará compuesta de una calle representada por “C/” o ”Calle’ seguido de un espacio con el nombre de la calle (una sola palabra) donde la primera letra debe estar en mayúscula, opcionalmente una coma, un número arbitrario de espacios, el número en cualquiera de los siguientes formatos (Nº7, N 7, 7, Nº 7, n7).
No es valido N º7 ni º7, la N podría estar en mayúsculas o minúsculas. Seguido, una coma, un número arbitrario de espacios y un número de 5 dígitos correspondiente a un código postal. 
Los nombres de las calles deben poder validar calles de Madrid formadas por una sola palabra, no es necesario que reconozca ”Calle Almendro Azul”, porque el nombre de la calle tiene dos palabras en vez de una.

Ejemplos de casos:

• “C/ Dulcinea Nº 10, 28936”
• “Calle Dulcinea 10, 28106”
• “Calle Dulcinea N10, 28091”

Para cada calle encontrada se reportará: 
“CP-Calle-Numero”, por ejemplo: “28926-Dulcinea-10”.

Nota: Si te da error busca las calles más bonitas de Madrid y revisa sintácticamente como se escriben.

