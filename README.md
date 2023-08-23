# Script_Libros_SEP
Este script fue cambiado por Alan Acosta Monter, incluyendo un menú para seleccionar el libro que queremos, esto con un arreglo que puede ser con un valor dinamico, segun el usuario lo determine

En nuestro código, en primer lugar importamos librerías que nos van a ayudar a realizar solicitudes http(requests) y que nos van a permitir interactuar con nuestro SO para la creación de de carpetas, directorios, etc..(os)

Después definimos una función llamada descargar imagen, la cual recibe 2 parámetros una URL y un nombre de archivo, dentro de la función colocamos un ty-except debido a que cuando lleguemos al límite de las páginas del libro ya no nos regresara una respuesta de 200, la cual quiere decir que una petición HTTP ya ha sido exitosa y de no ser por este try-except se causaría un error al ejecutar el código. Antes de obtener esta respuesta debemos usar el método requests.get(url) para obtenerla y guardarla en una variable llamada “respuesta”, en el if colocamos la parte que mencionamos anteriormente que podría producir un error, ya corroborando que la respuesta es satisfactoria procedemos a usar un open para abrir un archivo con el nombre que le mandamos, el with es para que el archivo se cierre una vez se haya usado, los datos de este archivo son los de las imágenes, imprimimos un mensaje para corroborar que todo salió bien y retornamos un true. La parte del else y del exception solo son para mandar mensajes en caso de que algo salga mal, además esto permite que el programa no se detenga cuando tengamos estos errores, sobretodo porque algunos son buscados ya que necesitamos que ocurra un error en una hipotética página sucesiva a la última página del libro ya que esto permitirá que el programa proceda a descargar el resto de libros.

Una vez que tenemos esa función, generamos un arreglo con todos los links de los libros de cada grado, (esta parte la realizamos de manera manual tuvimos que buscar los links de cada libro y colocarlos en el arreglo).

Ya con el arreglo, definimos una variable llamada extensión, que nos servirá para buscar todas las imágenes de cada link en el que estamos entrando.

Después con un for vamos a recorrer el arreglo de links y para cada link, en primer lugar vamos a sacar el nombre del libro, para ello utilizamos split y dividimos la URL en partes utilizando "/" como separador y obtenemos el penúltimo elemento de esas partes, que es el nombre del libro.

Una vez hecho eso, si no existe, creamos una carpeta con el nombre del libro utilizando un método de la librería os (os.makedirs), después definimos una variable contador, este nos va a ayudar a ir desplazándose por las imágenes de cada libro y llevar un control sobre las mismas. 

Después con un ciclo while infinito, convertimos el contador en una cadena de texto rellenada con ceros a la izquierda para tener tres dígitos y creamos la URL completa de la imagen utilizando el enlace base, el número de imagen y la extensión.
Imprimimos un mensaje en el que vamos a corroborar más adelante si la imagen se descargó con éxito, después definimos el nombre de la imagen que va a descargar incluyendo la carpeta del libro, el nombre base y el contador.
 
Una vez hecho esto llamamos a la función descargar_imagen con la URL de la imagen y el nombre de archivo, y si la descarga falla, se rompe el bucle while.

Finalmente aumentamos el contador para obtener la siguiente imagen en el próximo ciclo while. 
