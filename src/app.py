import streamlit as st
from streamlit_gsheets import GSheetsConnection
from main import writeinsheet
from main import selectduplicated
import os
import time
from pathlib import Path
import psutil
st.set_page_config(layout="wide")
conn = st.connection("gsheets",type=GSheetsConnection)

#directorio donde se encuentran los discos C:\\Users\\34674\\Desktop\\bibliopy

#solo busca carpetas
#opt = [nombre for nombre in os.listdir(maindir) if os.path.isdir(os.path.join(maindir, nombre))]
# Función para obtener discos duros
def obtener_disco_duro():
    particiones = psutil.disk_partitions()
    discos = [particion.device for particion in particiones]
    return discos

# Obtener la lista de discos duros
discos_duros = obtener_disco_duro()

# Mostrar la lista de discos en un selector de Streamlit
if st.toggle("Intrtoducir ruta",):
    maindir=(st.text_input("Ruta del disco"))
else:
    maindir = st.selectbox("Selecciona un disco duro", discos_duros)
print(maindir)
col1 ,col2 = st.columns(2)
data1 = conn.read(worksheet='Peliculas',ttl=5)
data2 = conn.read(worksheet='Repetidas',ttl=5)

with col1:
    st.header('Peliculas actuales')
    st.dataframe(data1,width=1000,height=500)
with col2:
    st.header('Peliculas repetidas')
    st.dataframe(data2,width=1000,height=500)

#dir = st.selectbox("Direccion",opt)
#st.write("La direccion elegida es ",dir)
if st.button("cargar peliculas"):
    with st.spinner("Cargando datos"):
        writeinsheet(maindir,'Peliculas')
    time.sleep(2)
    st.rerun()
if st.button("refresh"):
    with st.spinner("Cargando datos"):
        writeinsheet(maindir,'Repetidas',data2)
    time.sleep(2)
    st.rerun()


