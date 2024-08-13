archivo = open("leer.txt","r")
contenido = archivo.read()
print(contenido)
archivo.close()

archivo_escritura = open("nuevo_archivo_leer.txt","w")
contenido="Este es un ejemplo de escritura de archivos en Python"
archivo_escritura.write(contenido)
archivo_escritura.close()