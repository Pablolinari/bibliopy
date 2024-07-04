import gspread
from google.oauth2.service_account import Credentials
from iosmanage import get_archivos

scope=[
    "https://www.googleapis.com/auth/spreadsheets"
]
creds = Credentials.from_service_account_file("credentials.json",scopes=scope)
client = gspread.authorize(creds)
sheetid = "1ryDAAKKe2thiksaN_FVnVELmJ5e2NRuB9183FlRp78Q"
sheettt = client.open_by_key(sheetid)
def opensheet(sheetid):
    return client.open_by_key(sheetid)


def writeinsheet(dir, sheet):
    files = get_archivos(dir)
    numrows = len(sheet.col_values(1))
    start_row = numrows + 1
    # Preparar los datos para la actualización
    values = []
    for arch, disk in zip(files[0], files[1]):
        values.append([arch, disk])
    
    # Crear el rango de celdas a actualizar
    range_to_update = f"A{start_row}:B{start_row}"
    
    # Crear el cuerpo de la solicitud para batch_update
    body = {
        "valueInputOption": "RAW",
        "data": [
            {
                "range": range_to_update,
                "values": values
            }
        ]
    }
    
    # Ejecutar batch_update
    sheet.batch_update(body)
    
writeinsheet("~/Escritorio",sheettt.sheet1)
sheettt.sheet1.update_acell("A1",3)
