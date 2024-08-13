import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd
from main import writesheetdata, getsheetdata, selectduplicated
from iosmanage import obtener_disco_duro

maindir = ""

def writefilms():
    writesheetdata(maindir, 0)
    print(maindir)

def show_dataframe(df):
    global tree
    # Añadir una columna de índice
    df = df.reset_index()
    df.rename(columns={'index': 'Índice'}, inplace=True)
    
    # Crear un nuevo frame para la tabla
    frame = tk.Frame(mainwindow)
    frame.pack(fill='both', expand=True)
    
    # Crear el estilo para el Treeview
    style = ttk.Style()
    style.configure("Treeview", rowheight=25, borderwidth=1, relief="solid", highlightthickness=1, highlightbackground="black")
    style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
    
    # Crear el Treeview
    tree = ttk.Treeview(frame, style="Treeview")
    tree.pack(side='left', fill='both', expand=True)
    
    # Definir las columnas
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"
    
    # Crear los encabezados de columna
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')
    
    # Insertar los datos
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))
    
    # Añadir una barra de desplazamiento
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side='right', fill='y')

def refresh():
    global tree, data0
    # Limpiar el contenido actual del Treeview
    for item in tree.get_children():
        tree.delete(item)
    
    # Obtener datos actualizados
    data0 = getsheetdata(0)
    
    # Añadir una columna de índice
    data0 = data0.reset_index()
    data0.rename(columns={'index': 'Índice'}, inplace=True)
    
    # Insertar los datos actualizados
    for index, row in data0.iterrows():
        tree.insert("", "end", values=list(row))
    writesheetdata(maindir, 1, selectduplicated(data0))
def search():
    global tree, data0
    search_text = search_entry.get()
    filtered_data = data0[data0.apply(lambda row: row.astype(str).str.contains(search_text, case=False).any(), axis=1)]
    
    # Limpiar el contenido actual del Treeview
    for item in tree.get_children():
        tree.delete(item)
    
    # Insertar los datos filtrados
    for index, row in filtered_data.iterrows():
        tree.insert("", "end", values=list(row))

def select_directory():
    global maindir
    maindir = filedialog.askdirectory()
    if maindir:
        print(f"Directorio seleccionado: {maindir}")

data0 = getsheetdata(0)

# Ventana principal 
mainwindow = tk.Tk()
mainwindow.geometry('1000x800')

# Crear frames para organizar los widgets
left_frame = tk.Frame(mainwindow)
left_frame.pack(side='left', padx=20, pady=20, anchor='n')

# Botón para seleccionar un directorio
select_dir_button = tk.Button(left_frame, text="Seleccionar Directorio", command=select_directory)
select_dir_button.pack(pady=5)

# Botón para enviar películas
submit_pelilculas = tk.Button(left_frame, text="Cargar Peliculas", command=writefilms)
submit_pelilculas.pack(pady=5)

# Botón para refrescar la tabla
refreshbutton = tk.Button(left_frame, text="Mostrar Peliculas", command=refresh)
refreshbutton.pack(pady=5)

# Entrada de texto para el criterio de búsqueda
search_entry = tk.Entry(left_frame)
search_entry.pack(pady=5)

# Botón para buscar en la tabla
search_button = tk.Button(left_frame, text="Buscar", command=search)
search_button.pack(pady=5)

# Mostrar el DataFrame en una tabla
show_dataframe(data0)

mainwindow.mainloop()