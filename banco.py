#conexão e criação de tabela sqlite

import sqlite3 as lite

#criando conexao

con = lite.connect('ficha.db')

#criando tabela

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, telefone TEXT, dia_em DATE, estado TEXT, assunto TEXT)")