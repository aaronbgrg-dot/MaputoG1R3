titulo: nombre de grupo e integrantes
contenidos:
  · funcionamiento del script (general)
  · funcionemiento del script (específico)
  · formato apariencia
  · apartados por persona
# Maputo (Grupo 1)
Proyecto de python realizado para el Reto 3 del centro de FP Cebanc por:
+ Unai Manterola
+ Aaron Benítez
+ Xabier Morales

# Contenido
> [!NOTE]
> Aquí describimos el funcionamiento del script que hemos realizado, 
> donde primero analizaremos el funcionamiento general del script, y luego iremos archivo a archivo mirando que función cumple cada uno de estos.

## Funcionamiento General
El archivo principal que se ejecuta al comienzo es _main.py_, que llama a una función del archivo _inicioSesion.py_ y muestra una pantalla de "Inicio de sesion".

![Pantalla de inicio de sesión en cmd](https://github.com/user-attachments/assets/fe70b18a-0f3f-4953-b348-8db599987201)
<br></br>

Luego, al pasar esta pantalla, nos podemos encontrar varias opciones:

**1. Realizar operaciones:**
Tal y como indica el nombre, te permite realizar varias operaciones relacionadas con una base de datos creada con **SQLite**.

![Pantalla con diferentes operaciones](https://github.com/user-attachments/assets/2253e3a2-7744-4830-865f-0653adfade79)
En este apartado uno interactua con una base de datos, donde puede añadir elementos a diferentes entidades y realizar busquedas de ciertos datos.
<br></br>

**2. Calculadora de precios:**
Permite revisar diferentes ofertas para las piezas de cada coche.

![Pantalla despues de realizar una operación](https://github.com/user-attachments/assets/fd0cb267-4a4f-4c88-bdcc-7f7fa5229860)
El usuario introduce el modelo de un coche, el nombre de una pieza, y el numero de ofertas que quiere ver 
_(con un número predeterminado de 5 en caso de que no se introduzca nada)_, y el script muestra diferentes "ofertas" para esa pieza. 
<br></br>

**3. Generar contraseña nueva:**
Genera una contraseña aleatoria entre los valores 0000 y 9999.

![Contraseña generada](https://github.com/user-attachments/assets/42f1b6a8-7079-42c9-b90d-500a0671a4e0)
Utiliza las herramientas de la biblioteca **_random_** para generar el número pseudoaleatorio.
<br></br>

**4. Cerrar Sesión:**
Finaliza la ejecución del script

![Imagen que muestra mensaje de finalización](https://github.com/user-attachments/assets/fac1c2e8-2973-41b2-8d91-bd284a5e8d5f)
Muestra un mensaje de despedida y utilizando el módulo **_time_** espera unos segundos antes de finalizar la ejecución del script.
<br></br>

## Funcionamiento Específico
Aquí analizamos como funciona cada uno de los archivos del script a fondo.

### main.py
Aunque es el archivo "principal" que se debe de ejecutar primero, no tiene nada de código como tal, simplemente llama a una función del archivo _inicioSesion.py_
`inicioSesion.login_menu()`.
<br></br>

### inicioSesion.py
Contiene la mayoría de la lógica detras de nuestro script. Aquí estan contenidas las funciones que controlan el funcionamiento de los menus y alguna que otra de las opciones opción.
`login_menu()` y `login_error()` controlan todo lo relacionado con el inicio de sesión, utilizando los datos de _config.json_ para verificar las credenciales de los usuarios **(usuario y contraseña)**, las demás funciones, tal y como se ha mencionado antes, tienen que ver con el aspecto y funcionalidad de los menus, todo está formateado de manera que el contenido esté centrado para darle un aspecto más "único".

### base.py | cambiarFases.py | querysBD.py
En estos tres archivos se controla todo lo relacionado con la base de datos de nuestro script, creado con **_sqlite3_**. En _base.py_ se encuentran las funciones que crean la base de datos y todas las entidades de la base. En _cambiarFases.py_ está todo lo relacionado con la inserción de datos en la base, que tiene como nombre Maputo_SL. Y en querysBD.py estan las funciones que permiten realizar busquedas de datos en la tabla **errores** de la base de datos, es decir, cada vez que se ejecutan las funciones de _cambiarFases.py_ hay una probabilidad de que salte "un error", y estos errores se almacenan en la tabla del mismo nombre, **errores**, y los datos almacenados en esta entidad son las que luego en el script se pueden visualizar.

### ./bdCoches/cribado.py | ./bdCoches/coches.txt
Estos dos archivos van de la mano, _cribado.py_ se conecta al .txt, recoge los datos de los coches que se encuentran en ese archivo y luego limpia los datos para luego introducirlos a la entidad de la base de datos, **coches**.

### calculadora.py | datos.py | precios.py
En el archivo _datos.py_ se encuentran datos relacionados con coches, cada coche tiene varias piezas y estas piezas tiene un precio asociado. En _calculadora.py_ se le pide al usuario que introduzca el nombre de un coche, una pieza, y el número de ofertas que quiere visualizar, luego, en _precios.py_ se calcula el precio de las ofertas, ya que por cada oferta que el usuario quiera ver (el numero predeterminado de ofertas es 5) el precio de estos varía, no son un valor estático.
<br></br>

## Apartados por persona
**Unai Manterola:** <br></br>
Unai ha desarrollado:
+ _inicioSesion.py_
+ _cribado.py_

Y se ha encargado establecer el formato para la apariencia del script y de añadir los comentarios del código.
<br></br>

**Aaron Benítez:**
Aaron ha desarrollado:
+ _calculadora.py_
+ _datos.py_
+ _precios.py_
<br></br>

**Xabier Morales:**
Xabier ha desarrollado:
+ _main.py_
+ _base.py_
+ _cambiarFases.py_
+ _inicioSesion.py_
+ _querysBD.py_
<br></br>

# Notas
> [!IMPORTANT]
> Cuando se utiliza la opción de generar una contraseña nueva, esta realmente cambia entre ejecuciones, se recomienda anotar cada vez que se genera una contraseña nueva para no tener que revisar constantemente el archivo _config.json_. 
<br></br>

> [!NOTE]
> Cuando se utiliza la calculadora de precios, hay que proveer el nombre del coche y la pieza tal y como están escritos en _datos.py_ pues el script si no, no lo reconoce.
<br></br>

> [!WARNING]
> En el archivo _querysBD.py_, si se intenta utilizar la segunda opción de "contador de errores" para visualizar la cantidad de errores de un coche que no existe en la tabla errores, salta un error.
<br></br>

> [!WARNING]
> Hay varias instancias a lo largo del script donde, si no se introduce ningún dato cuando se utiliza un `input()`, salta un error. 
