import gspread
from google.oauth2.service_account import Credentials
from iosmanage import get_archivos

scope=[
    "https://www.googleapis.com/auth/spreadsheets"
]
creds = Credentials.from_service_account_file("./credentials.json",scopes=scope)
client = gspread.authorize(creds)

sheetid = "1ryDAAKKe2thiksaN_FVnVELmJ5e2NRuB9183FlRp78Q" ##desde d/ hasta / de la url de calculo 

sheet = client.open_by_key(sheetid)

def writeinsheet(dir):
    files = get_archivos(dir)
    numrows = len(sheet.sheet1.col_values(1))
    start_row = numrows + 1
    # Preparar los datos para la actualización
    values = []
    for arch, disk in zip(files[0], files[1]):
        values.append([arch,disk])
        
    sheet.sheet1.batch_update([{'range': f'A{start_row}','    values': values,}])
