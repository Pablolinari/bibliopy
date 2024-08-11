import os

def get_archivos(ruta_dir):
    peliculas = []
    disco =[]
    tamanio=[]
    auxruta_dir =ruta_dir.split('\\')[-1]
    for dir_actual ,carpetas,archivos in os.walk(ruta_dir):
        aux = dir_actual.index(auxruta_dir)
        aux = dir_actual[aux:]
        for archivo in archivos :
            tamanio.append(os.path.getsize("%s\\%s"%(dir_actual,archivo))/(1024**3))
            archivo = archivo.split('.')[0]
            peliculas.append(archivo)
            disco.append(aux)
    return [peliculas,disco,tamanio]


