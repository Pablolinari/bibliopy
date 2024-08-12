import gspread
from google.oauth2.service_account import Credentials
from iosmanage import get_archivos
import pandas as pd
scope=[
    "https://www.googleapis.com/auth/spreadsheets"
]
creds = Credentials.from_service_account_file("./credentials.json",scopes=scope)
client = gspread.authorize(creds)

sheetid = "1ryDAAKKe2thiksaN_FVnVELmJ5e2NRuB9183FlRp78Q" ##desde d/ hasta / de la url de calculo 

sheet = client.open_by_key(sheetid)

sheet.get_worksheet(0)
def writeinsheet(dir,number,data=None):
    files = get_archivos(dir)
    numrows = len(sheet.get_worksheet(number).col_values(1))
    if numrows ==0 :
        sheet.get_worksheet(number).update('A1','Peliculas')
        sheet.get_worksheet(number).update('B1','Disco')
        numrows+=1
    start_row = numrows + 1
    # Preparar los datos para la actualización
    values = []
    if data is None:
        for arch, disk,tam in zip(files[0], files[1],files[2]):
            values.append([arch,disk,tam])
    else:
        values=data.values.tolist()
        
    sheet.get_worksheet(number).batch_update([{'range': f'A{start_row}','values': values,}])
def getsheetdata():
    df = pd.DataFrame(sheet.get_worksheet(0).get_all_records())
    return df




def selectduplicated(data):
    df = pd.DataFrame(data)
    dfp = df[df.columns[0]]
    duplicados = dfp.duplicated(keep=False)
    print (duplicados)
    return df[duplicados]

