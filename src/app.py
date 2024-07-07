import streamlit as st
from streamlit_gsheets import GSheetsConnection
from main import writeinsheet
import os
import time
st.Pag
conn = st.connection("gsheets",type=GSheetsConnection)
data = conn.read(worksheet='Hoja 1',ttl=5)
st.dataframe(data)
if st.button("refresh"):
    data = conn.read(worksheet='Hoja 1',ttl=5)

maindir="/home/pablolinari/Escritorio"
opt =os.listdir(maindir)
dir = st.selectbox("Direccion",opt)
st.write("el tipo de direccion es ",'dir')
if st.button("cargar peliculas"):
    with st.spinner("Cargando datos"):
        writeinsheet(f'{maindir}/{dir}')
    time.sleep(2)
    data = conn.read(worksheet='Hoja 1')



