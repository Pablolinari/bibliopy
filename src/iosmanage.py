import os
import psutil
import pandas as pd
# lista todos los archivos de un directorio y subdirectorios dando el nombre el directorio al que pertenece 
# y el tamanio en GB
def get_archivos(ruta_dir):
    print(ruta_dir)
    values=[]
    auxruta_dir =ruta_dir.split('\\')[-1]
    for dir_actual ,carpetas,archivos in os.walk(ruta_dir):
        aux = dir_actual.index(auxruta_dir)
        aux = dir_actual[aux:]
        for archivo in archivos :
            tam =os.path.getsize("%s\\%s"%(dir_actual,archivo))
            print(tam)
            tam=tam/(1024**3)
            print(tam)
            archivo = archivo.split('.')[0]
            values.append([archivo,aux,tam])
    return values

#Da una lista de discos duros del sistema

def obtener_disco_duro():
    particiones = psutil.disk_partitions()
    discos = [particion.device for particion in particiones]
    return discos

