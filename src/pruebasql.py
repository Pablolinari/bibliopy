import sqlite3

connect = sqlite3.connect('peliculas.db')

#create a cursor
c = connect.cursor()

#create a table 

c.execute(""" CREATE TABLE biblioteca (
    
    nombre_pelicula text,
    nombre_disco text,
    espacio real
)
""")
#commit our command 
connect.commit()

#close connection (good practice )
connect.close()

