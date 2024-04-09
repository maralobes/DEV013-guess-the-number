# Python 🐍

## 1. Preámbulo

Python es uno de los lenguajes de programación más populares y versátiles en la
actualidad. Su éxito radica en su simplicidad y legibilidad, convirtiéndolo en
una opción ideal para aquellos que se inician en la programación. A pesar de la
diversidad de plataformas y herramientas disponibles, es esencial tener un
sólido entendimiento de los conceptos fundamentales de Python. Además, Python
es un lenguaje de programación multiparadigma, lo que significa que puedes
utilizar diferentes estilos de programación para resolver problemas, lo que
añade a su flexibilidad y poder. El objetivo de este proyecto fue conocer el
mundo de Python mediante un juego sencillo y entretenido.

## 2. Consideraciones Generales

- Duración del proyecto: 2 sprints.
- Está implementado en Python. La única dependencia externa utilizada
 fue pytest para pruebas unitarias.
- El juego se llevó a cabo en la terminal, así como también las pruebas unitarias.
- Se utilizó un número aleatorio entre 1 y 100 como número secreto.
- La jugadora y el ordenador se turnan para adivinar el número.
- Después de cada turno, se muestra información sobre la suposición realizada.
- El juego termina cuando se adivine el número. Se muestra una lista de
  todas las tentativas de la jugadora ganadora.

## 3. Consideraciones Técnicas

El juego se llevó a cabo en la terminal usando Python. La lógica del juego se
basó en estructuras de control, incluyendo bucles, condicionales y
colecciones. Fue necesario dividir el código y mejorar su legibilidad y
mantenimiento. Se utilizó una funcionalidad de la biblioteca de
utilidades de Python para la generación de números aleatorios (random). Se
realizaron pruebas unitarias para sus clases y métodos utilizando PyTest y
simulación de generación de números aleatorios con unittest.mock.

## 4. Hitos

A continuación, se desglosan los hitos que guiaron la construcción del proyecto.

### 4.1 Crear el entorno de desarrollo

El primer paso fue configurar mi entorno de desarrollo. Para este proyecto,
necesité Python 3 y un editor de texto o un entorno de desarrollo integrado
(IDE), que en este caso usé Visual Studio Code.

1. Instalé Python 3 desde el sitio oficial de Python.

2. Eligí Visual Studio Code como IDE.

3. Configuré mi IDE para usar Python 3.

### 4.2 Crear un script de Python

A continuación, creé un script de Python simple para asegurarme de que mi
configuración funcionara correctamente.

1. Creé un nuevo archivo llamado `main.py`. <br>
2. Ejecuté `main.py`.

### 4.3 Implementar el juego

Empecé a implementar el juego.

1. Generé un número aleatorio entre 1 y 100. Usé la función `randint`
en el módulo `random` para hacer esto.

2. Implementé un bucle que solicita a la jugadora que adivine el número. Usé la
función `input` para obtener la entrada de la jugadora.

3. Comparé la entrada de la jugadora con el número secreto. Si la jugadora
adivina correctamente, termina el juego. Si la jugadora adivina
incorrectamente, proporciona una pista sobre si el número secreto es mayor o
menor que la entrada de la jugadora.

4. Implementé la lógica para el turno del ordenador. El ordenador hace
una suposición aleatoria. Queda como pendiente implementar alguna estrategia para que sus
suposiciones sean más inteligentes.

5. El juego continúa hasta que la jugadora o el ordenador adivinen
correctamente el número.

6. Añadí pruebas unitarias para mi código. Para ello, usé el módulo incorporado de Python
llamado `unittest`.

### 4.4 Mejorar el juego

Una vez que obtuve una versión básica del juego funcionando, hice las siguientes
mejoras:

1. Llevé un registro de las suposiciones de la jugadora y del ordenador. Cuando
el juego termine, se muestran todas las suposiciones que hizo la jugadora ganadora. 
Para ello, usé .append para añadir los números a una lista.

2. Añadí una opción para jugar de nuevo. Cuando el juego termina, se le pregunta a la
jugadora si quiere jugar de nuevo.

3. Añadí comentarios a mi código para explicar qué hace cada parte, con el fin de hacer
que mi código sea más fácil de entender y mantener.

### Objectivos de aprendizaje con Python

Algunos de los objetivos de aprendizaje con este proyecto se enlistan a continuación: 

- [ ] **Variables (declaración, asignación, ámbito)**

- [ ] **Uso de condicionales (if, elif, ternario)**

- [ ] **Operadores (identidad, aritméticos, comparación etc)**

- [ ] **Docstrings (y su diferencia de comentarios)**

- [ ] **Linting (pylint)**

#### Tipos de datos

- [ ] **Tipos de datos primitivos (int, float, str, bool)**

- [ ] **Listas (arrays)**

- [ ] **Tuples**

- [ ] **Dictionaries (Dicts)**

- [ ] **Sets**

#### Funciones

- [ ] **Conceptos basicos (params, args, default values, return)**

#### Iteración

- [ ] **Uso de bucles/ciclos (while, for..in)**

#### Testing en Python

- [ ] **Pruebas unitarias (unit tests, unittest, pytest)**

- [ ] **Uso de mocks (y patch)**

- [ ] **Uso de fixtures**

#### Modularización

- [ ] **Módulos**

#### Manejo de dependencias

- [ ] **pip (instalación y uso de paquetes)**

- [ ] **Virtual Environment (ambientes virtuales, virtualenv)**

- [ ] **requirements.txt**>
