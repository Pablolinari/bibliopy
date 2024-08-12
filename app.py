import streamlit as st
from main import writesheetdata, getsheetdata,selectduplicated
import time
from pathlib import Path
from iosmanage import obtener_disco_duro
import pandas as pd

st.set_page_config(layout="wide",page_title='Biblioteca',page_icon=":cinema:")

    
#LISTA DE DISCOS  DUROS
discos_duros = obtener_disco_duro()

# Mostrar la lista de discos en un selector de Streamlit
if st.toggle("Intrtoducir ruta",):
    maindir=(st.text_input("Ruta del disco"))
else:
    maindir = st.selectbox("Selecciona un disco duro", discos_duros,index=None,placeholder='Elegir un disco')

col1 ,col2 = st.columns(2)

data0 =getsheetdata(0)
data1=getsheetdata(1)
with col1:
    st.header('Peliculas actuales')
    st.dataframe(data0,width=1000,height=500)
if st.toggle("ver peliculas repetidas"):
    with col2:
        st.header('Peliculas repetidas')
        st.dataframe(data1,width=1000,height=500)


if st.button("cargar peliculas"):
    with st.spinner("Cargando peliculas"):
        writesheetdata(maindir,0)
        writesheetdata(maindir,1,data0)

if st.button('Actualizar vista'):
    data0=getsheetdata(0)
    data1=getsheetdata(1)






    

    



