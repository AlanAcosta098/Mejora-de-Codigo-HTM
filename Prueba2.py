import os #proporciona funciones de interaccion con el Sistema operativo
import requests #proporciona funciones para realizar solicitudes http 

# Función para descargar una imagen desde una URL
def descargar_imagen(url, nombre_archivo):
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            with open(nombre_archivo, 'wb') as archivo:
                archivo.write(respuesta.content)
            print("Imagen descargada exitosamente como", nombre_archivo)
            return True
        else:
            print("Error al descargar la imagen. Código de estado:", respuesta.status_code)
    except Exception as e:
        print("Ocurrió un error:", e)
    return False



Grado_Primaria = int(input("Elige el grado de primaria: "))

# Verifica si el número ingresado es válido
if Grado_Primaria < 1 or Grado_Primaria > 6:
    print("Número inválido. Debe ser del 1 al 6.")
else:
    # Pregunta al usuario qué libro quiere
    print("¿Qué libro quieres?")
    print("1. Un libro sin recetas")
    print("2. Multiples lenguajes")
    print("3. Libro de proyectos de Aula")
    print("4. Libro de proyectos Comunitarios")
    print("5. Libro de proyectos Escolares")
    print("6. Nuestros Saberes")
    print("7. Multiples lenguajes, Trazos y palabras")

    opcion_libro = int(input("Selecciona una opción del 1 al 7: "))

    # Asigna el valor correspondiente a la variable "Libro" según la opción elegida
    if opcion_libro == 1:
        Libro = "LPM"
    elif opcion_libro == 2:
        Libro = "MLA"
    elif opcion_libro == 3:
        Libro = "PAA"
    elif opcion_libro == 4:
        Libro = "PCA"
    elif opcion_libro == 5:
        Libro = "PEA"
    elif opcion_libro == 6:
        Libro = "SDA"
    elif opcion_libro == 7:
        Libro = "TPA"
    else:
        print("Opción inválida. Debe ser del 1 al 7.")

elemento = f'P{Grado_Primaria}{Libro}'
urls_libros = [f'https://www.conaliteg.sep.gob.mx/2023/c/{elemento}/']

extension = ".jpg"

# Iterar a través de cada enlace de libro
for base_url in urls_libros:
    # Extraer el nombre del libro del enlace
    nombre_libro = base_url.split("/")[-2]
    
    # Crear una carpeta para el libro si no existe
    carpeta_libro = f"{nombre_libro}/"
    if not os.path.exists(carpeta_libro):
        os.makedirs(carpeta_libro)

    contador = 0
    while True:
        numero_imagen = str(contador).zfill(3) #Convertir contador a cadena de 3 digitos con relleno de ceros
        url_imagen = f"{base_url}{numero_imagen}{extension}" #Construir URL completa de la imagen
        print("Intentando descargar:", url_imagen) 

        nombre_archivo = f"{carpeta_libro}imagen_descargada_{contador}.jpg" #Crear nombre de archivo

        # Intentar descargar la imagen usando la funcion descargar_imagen
        if not descargar_imagen(url_imagen, nombre_archivo):
            break

        contador += 1 #incrementar contador para la siguiente imagen

