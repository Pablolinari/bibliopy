import gspread
from google.oauth2.service_account import Credentials
from iosmanage import get_archivos
import pandas as pd
import streamlit as st
scope=[
    "https://www.googleapis.com/auth/spreadsheets"
]
skey = st.secrets.get('gcp_service_account')
creds = Credentials.from_service_account_info(skey,scopes=scope)
client = gspread.authorize(creds)

sheetid = "1ryDAAKKe2thiksaN_FVnVELmJ5e2NRuB9183FlRp78Q" ##desde d/ hasta / de la url de calculo 

sheet = client.open_by_key(sheetid)


#Escribe en la hoja sheet los archivos listados de dir que se le han pasado 
#si data != None se escribe el df pasado
   
def writesheetdata(dir,number,data=None):
    values = get_archivos(dir)
    numrows = len(sheet.get_worksheet(number).col_values(1))
    if numrows ==0 :
        sheet.get_worksheet(number).update('A1:C1',[['Peliculas','Disco','Tamaño']])

        numrows+=1
    start_row = numrows + 1
    # Preparar los datos para la actualización
    if data is not None:
        values=data.values.tolist()
    
    sheete=sheet.get_worksheet(number)
    sheete.batch_update([{'range': f'A{start_row}','values': values,}])

def getsheetdata(index):
    pd.options.display.float_format = lambda x: f'{x:.2f}'.replace('.', ',')
    return pd.DataFrame(sheet.get_worksheet(index).get_all_records())

def selectduplicated(data):
    df = pd.DataFrame(data)
    dfp = df[df.columns[0]]
    duplicados = dfp.duplicated(keep=False)
    return df[duplicados]
def getsheets():
    values=[]
    for ssheet in sheet:
        values.append(ssheet.title)
    return values

    

    