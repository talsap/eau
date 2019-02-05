# -*- coding: utf-8 -*-
#SQL

import sqlite3

connection = sqlite3.connect('banco.db')
c = connection.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS capsulas (id integer, capsula text, massa real)')

create_table()
sql = 'SELECT * FROM capsulas'

def ler_cap():
    lista_capsulas = []
    for row in c.execute(sql):
        lista_capsulas.append(row[1])

    return lista_capsulas

def data_entry_cap(a, b):
    quantidade = ler_cap()
    id = len(quantidade)
    c.execute("INSERT INTO capsulas (id, capsula, massa) VALUES (?, ?, ?)", (id, a, b))
    connection.commit()






########################################################################
