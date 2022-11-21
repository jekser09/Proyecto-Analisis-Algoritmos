# Proyecto Final Analisis de algortimos Universidad Central
Bienvenidos.

Autor: Johand Esteban Castro Rodriguez

Profesor: Giovanny Alexander Briceño Riveros

## Descripcion:
* En este programa podremos observar la diferencia de tiempo de ordenamiento entre
los algortimos TimSort, QuickSort y BubbleSort.
* Encontraremos una grafica representando los tiempos y una tabla con la informacion necesaria de cada algoritmo.
## Funcionamiento
### Ventana Inicio
En la ventana de inicio, encontraremos 3 botones, al presionarlos se abrira un enlace con la descripcion respectiva de cada algoritmo.
### Ventana Demostracion
En la ventana de demostracion, tendremos varios apartados:
* Datos Aleatorios: En este apartado tendremos por defecto algunos valores:
    - Cantidad de datos: 1000, Iteraciones: 10, Avance: 20 y tipo de datos: Numeros seleccionado.

       los primeros tres son los valores minimos por defecto y no podremos modificarlos por valores menores.

    - Cantidad de datos: Nos va a inidicar la cantidad de datos que inicialmente ordenaremos, para el caso por defecto se creara una lista de 1000 datos de numeros o palabras
    - Iteraciones: Nos va a indicar la cantidad de listas que crearemos y ordenaremos una a una, para el caso por defecto se crearan 10 listas.
    - Avance: Nos va a indicar cuantos datos se añadiran a las listas consecutivas es decir que si nuestro avance tiene un valor de "20" entonces la primera lista tendra 1000 datos y la segunda lista 1020 datos.
    - Tipo de datos: Aqui elegiremos si queremos ordenar numeros o palabras.
    - Boton iniciar: Al presionarlo se tomaran los valores digitados e iniciaran los algoritmos,            posteriormente se pintara la grafica y la tabla se llenara con los datos respectivos.
* Archivos: Aqui el programa sera capaz de leer los datos tomados de varios archivos con extension 'csv' y       ordenarlos.
    - Crear Archivos: El valor por defecto es 1, aqui indicaremos cuantos archivos con extension 'csv' queremos crear.
    - Boton 1: Este boton creara los archivos 'csv' en el directorio 'Archivos entrada', estos archivos contienen numeros o palabras y estos datos se generan de forma aleatoria.
    - Boton 2: Aqui podremos seleccionar el directorio en donde queremos leer los archivos para realizar el ordenamiento.
    - Boton 3: Despues de que se halla seleccionado una ruta en donde se encuentren los archivos requeridos, este boton al ser presionado leera dichos archivos y ejecutara los algoritmos respectivos, dibujara la grafica y rellenara la tabla respectivamente.
* Extras: Este programa por defecto creara los direcotorios (o archivos) 'Archivos entrada' y 'Archivo salida' si no los encuentra.
    - Directorio Archivos salida: aqui se crearan archivos con los datos ordenados.
    - Boton con ?: Este boton nos trae al repositorio del programa en donde encontramos el codigo y la explicacion del mismo.