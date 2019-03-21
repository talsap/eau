# -*- coding: utf-8 -*-
#SQL

import sqlite3
import time
import datetime

connection = sqlite3.connect('banco.db')
c = connection.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS capsulas (id INTEGER PRIMARY KEY AUTOINCREMENT, capsula text, massa real)')
    c.execute('CREATE TABLE IF NOT EXISTS dadosIniciais (id INTEGER PRIMARY KEY AUTOINCREMENT, datestamp text, tipoAnel text, diametro_anel real, altura_anel real, massa_anel real, massa_conj real, alt_corpo_prova real, massa_espc real)')
    c.execute('CREATE TABLE IF NOT EXISTS umidadeInicial (id integer, cap01 text, cap02 text, cap03 text, massaSeca01 real, massaSeca02 real, massaSeca03 real, massaUmida01 real, massaUmida02 real, massaUmida03 real)')
    c.execute('CREATE TABLE IF NOT EXISTS pressaoAplicada (id integer, id_Estagio integer, pressao_aplicada real)')
    c.execute('CREATE TABLE IF NOT EXISTS coletaDados (id integer, id_Estagio integer, tempo real, raizdotempo real, altura real)')

create_table()

def ListaVisualizacao():
    a = ids()
    b = juncaoLista()
    cont = 0
    id = len(a) - 1
    c = []
    while cont <= id:
        c.append( a[cont] + b[cont])
        cont = cont +1
    return c

def juncaoLista():
    a = dataVisualizacao()
    b = numEstagio()
    cont = 0
    id = len(a) - 1
    c = []
    while cont <= id:
        c.append([a[cont] + b[cont]])
        cont = cont +1
    return c

def ids():
    lista_id = []

    for row in c.execute('SELECT * FROM dadosIniciais'):
        lista_id.append([row[0]])

    return lista_id

'''Captura as datas e cria uma lista para visualização'''
def dataVisualizacao():
    list_datestamp = []

    for row in c.execute('SELECT * FROM dadosIniciais'):
        list_datestamp.append([row[1]])

    return list_datestamp

'''Captura a quantidade de estagio de cada ensaio e cria uma lista para visualização'''
def numEstagio():
    id = 1
    a = ler_quant_ensaios()
    list_numEstagios = []

    while id <= a:
        for row in c.execute('SELECT max(id_Estagio) FROM pressaoAplicada WHERE id = ?', (id,)):
            row = format(row).replace('(','')
            row = format(row).replace(')','')
            row = format(row).replace(',','')
            list_numEstagios.append([row])
        id = id + 1

    return list_numEstagios

'''Adiciona no banco os dados da pressão correspondete a cada Estágio'''
def InserirDadosPressao(a, b):
    id = ler_quant_ensaios()
    id_Estagio = ler_quant_estagios()
    c.execute("INSERT INTO pressaoAplicada (id, id_Estagio, pressao_aplicada) VALUES (?, ?, ?)", (id, a, b))

'''Adiciona no banco os dados de tempo e altura do corpo-de-prova'''
def InserirDados(a, b):
    id = ler_quant_ensaios()
    id_Estagio = ler_quant_estagios() - 1
    if a == 0:
        raizdotempo = 0
    else:
        raizdotempo = a**0.5
    c.execute("INSERT INTO coletaDados (id, id_Estagio, tempo, raizdotempo, altura) VALUES (?, ?, ?, ?, ?)", (id, id_Estagio, a, raizdotempo, b))
    connection.commit()

'''Seleciona o diametro correspondente no banco de dados'''
def diametro_anel():
    id = ler_quant_ensaios()
    for rows in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        diametro = rows[3]

    diametro = diametro/100
    return diametro

'''Ver a quantidade de Estagios que tem no ensaio para criar o proximo id_Estagio'''
def ler_quant_estagios():
    id = ler_quant_ensaios()
    identificador = []
    for rows in c.execute('SELECT * FROM pressaoAplicada WHERE id = ?', (id,)):
        identificador.append(rows[1])

    id = len(identificador) + 1
    return id

'''Ver a quantidade de ensaios que tem no banco para criar os ids'''
def ler_quant_ensaios():
    for rows in c.execute('SELECT * FROM dadosIniciais'):
        identificador  = rows[0]

    try:
        return identificador
    except UnboundLocalError:
        return 0


'''Ver as capsulas que já tem no banco'''
def ler_cap():
    lista_capsulas = []
    for row in c.execute('SELECT * FROM capsulas ORDER BY capsula ASC'):
        lista_capsulas.append(row[1])

    return lista_capsulas

'''Cadastra uma capsula no banco'''
def data_entry_cap(a, b):
    c.execute("INSERT INTO capsulas (id, capsula, massa) VALUES (NULL, ?, ?)", (a, b))
    connection.commit()

'''Adiciona os dados iniciais do ensaio no banco'''
def data_entry_dados(tipoAnel, d_anel, a_anel, m_anel, m_conj, alt_cprova, m_esp):
    datestamp = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("INSERT INTO dadosIniciais (id, datestamp, tipoAnel, diametro_anel, altura_anel, massa_anel, massa_conj, alt_corpo_prova, massa_espc) VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (datestamp, tipoAnel, d_anel, a_anel, m_anel, m_conj, alt_cprova, m_esp))
    connection.commit()

'''Adiciona os valores para calcular o teor de umidade inicial'''
def data_entry_umidade(cap01, cap02, cap03, mSeca01, mSeca02, mSeca03, mUmida01, mUmida02, mUmida03):
    id = ler_quant_ensaios()
    c.execute("INSERT INTO umidadeInicial (id, cap01, cap02, cap03, massaSeca01, massaSeca02, massaSeca03, massaUmida01, massaUmida02, massaUmida03) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, cap01, cap02, cap03, mSeca01, mSeca02, mSeca03, mUmida01, mUmida02, mUmida03))
    connection.commit()



################################################################################################################################################
