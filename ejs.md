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
$\d{4}^
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