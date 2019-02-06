# -*- coding: utf-8 -*-
#SQL

import sqlite3
import time
import datetime

connection = sqlite3.connect('banco.db')
c = connection.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS capsulas (id integer, capsula text, massa real)')
    c.execute('CREATE TABLE IF NOT EXISTS dadosIniciais (id integer, datestamp text, tipoAnel text, diametro_anel real, altura_anel real, massa_anel real, massa_conj real, at integer, alt_corpo_prova real, massa_espc real)')
    c.execute('CREATE TABLE IF NOT EXISTS umidadeInicial (id integer, cap01 text, cap02 text, cap03 text, massaSeca01 real, massaSeca02 real, massaSeca03 real, massaUmida01 real, massaUmida02 real, massaUmida03 real)')

create_table()
sql01 = 'SELECT * FROM capsulas ORDER BY capsula ASC'
sql02 = 'SELECT * FROM dadosIniciais'
sql03 = 'SELECT * FROM umidadeInicial'

'''Ver a quantidade de ensaios que tem no banco para criar o proximo id'''
def ler_quant_ensaios():
    identificador = []
    for rows in c.execute(sql02):
        identificador.append(rows[0])

    return identificador

'''Ver a quantidade de umidades que tem no banco para criar o proximo id'''
def ler_quant_Umidade():
    identificador = []
    for rows in c.execute(sql03):
        identificador.append(rows[0])

    return identificador

'''Ver a quantidade de capsulas que tem no banco para criar o proximo id'''
def ler_cap():
    lista_capsulas = []
    for row in c.execute(sql01):
        lista_capsulas.append(row[1])

    return lista_capsulas
'''Cadastra uma capsula no banco'''
def data_entry_cap(a, b):
    quantidade = ler_cap()
    id = len(quantidade)
    c.execute("INSERT INTO capsulas (id, capsula, massa) VALUES (?, ?, ?)", (id, a, b))
    connection.commit()

'''Adiciona os dados iniciais do ensaio no banco'''
def data_entry_dados(tipoAnel, d_anel, a_anel, m_anel, m_conj, at, alt_cprova, m_esp):
    datestamp = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
    quantidade = ler_quant_ensaios()
    id = len(quantidade)
    c.execute("INSERT INTO dadosIniciais (id, datestamp, tipoAnel, diametro_anel, altura_anel, massa_anel, massa_conj, at, alt_corpo_prova, massa_espc) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, datestamp, tipoAnel, d_anel, a_anel, m_anel, m_conj, at, alt_cprova, m_esp))
    connection.commit()

'''Adiciona os valores para calcular o teor de umidade inicial'''
def data_entry_umidade(cap01, cap02, cap03, mSeca01, mSeca02, mSeca03, mUmida01, mUmida02, mUmida03):
    quantidade = ler_quant_Umidade()
    id = len(quantidade)
    c.execute("INSERT INTO umidadeInicial (id, cap01, cap02, cap03, massaSeca01, massaSeca02, massaSeca03, massaUmida01, massaUmida02, massaUmida03) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, cap01, cap02, cap03, mSeca01, mSeca02, mSeca03, mUmida01, mUmida02, mUmida03))
    connection.commit()





########################################################################
