import streamlit as st
from streamlit_gsheets import GSheetsConnection
from main import writeinsheet
conn = st.connection("gsheets",type=GSheetsConnection)
data = conn.read(worksheet="Hoja 1")
st.dataframe(data)
if st.button('Actualizar datos'):
    conn.reset
    st.dataframe(conn.read(worksheet="Hoja 1"))
