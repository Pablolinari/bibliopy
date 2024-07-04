import os
import sys
import pandas as pd 




def get_archivos(ruta_dir):
    peliculas = []
    disco =[]
    auxruta_dir =ruta_dir.split('\\')[-1]
    for dir_actual ,carpetas,archivos in os.walk(ruta_dir):
        print(f'Directorio :{dir_actual}')
        aux = dir_actual.index(auxruta_dir)
        aux = dir_actual[aux:]
        for archivo in archivos :
            archivo = archivo.split('.')[0]
            print (f'Archivos : {archivo}')
            peliculas.append(archivo)
            disco.append(aux)
    return [peliculas,disco]

out = get_archivos("/home/pablolinari/Escritorio/biblioteca/src")
print(out)