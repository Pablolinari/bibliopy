import streamlit as st 
import psutil
def obtener_disco_duro():
    particiones = psutil.disk_partitions()
    print(particiones)
    discos = [particion.device for particion in particiones]
    return discos

print(obtener_disco_duro())