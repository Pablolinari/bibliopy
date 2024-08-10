from pandas.core.dtypes.cast import ensure_dtype_can_hold_na
from pyarrow import null
import streamlit
import os 


class data:
    def __init__(self,maindir,sheetid):
        self.maindir = maindir
        self.sheetid =sheetid
        self.dir=null
    @property
    def maindir(self):
        return self.maindir
    def sheetid(self):
        return self.sheetid 

    def dir(self ,dir):
        self.dir = dir
    def get_archivos(self , ruta_dir):
        peliculas = []
        disco =[]
        auxruta_dir =ruta_dir.split('\\')[-1]
        for dir_actual ,carpetas,archivos in os.walk(ruta_dir):
            aux = dir_actual.index(auxruta_dir)
            aux = dir_actual[aux:]
            for archivo in archivos :
                archivo = archivo.split('.')[0]
                peliculas.append(archivo)
                disco.append(aux)
        return [peliculas,disco]
    def writeinsheet(self ,dir):

        sheet = client.open_by_key(sheetid)
        files = get_archivos(self,dir)
        numrows = len(sheet.sheet1.col_values(1))
        start_row = numrows + 1
        # Preparar los datos para la actualización
        values = []
        for arch, disk in zip(files[0], files[1]):
            values.append([arch,disk])
        
        sheet.sheet1.batch_update([{'range': f'A{start_row}','    values': values,}])
