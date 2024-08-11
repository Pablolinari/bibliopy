import pandas as pd


def selectduplicated(data):
    df = pd.DataFrame(data)
    dfp = df['pelicula']
    duplicados = dfp.duplicated(keep=False)
    print (duplicados)
    return df[duplicados]


