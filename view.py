import sqlite3 as lite

con = lite.connect('ficha.db')

def inserir_info(i):
    with con:
        cur = con.cursor()
        query = ("INSERT INTO formulario(nome, email, telefon, dia_, etado, assunto) VALUES(?, ?, ?, ?, ?, ?)")
        cur.execute(query,i)




def mostrar_info():
    with con:
        lista = []
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        informacao = cur.fetchall()

        for i in informacao:
            lista.append(i)

    return lista