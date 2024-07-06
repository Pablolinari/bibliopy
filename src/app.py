import streamlit as st
from streamlit_gsheets import GSheetsConnection
from main import *
conn = st.connection("gsheets",type=GSheetsConnection)
data = conn.read(worksheet="Hoja 1")
st.dataframe(data)

