# -*- coding: utf-8 -*-
#SQL

import sqlite3
import time
import datetime

connection = sqlite3.connect('banco.db')
c = connection.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS capsulas (id INTEGER PRIMARY KEY AUTOINCREMENT, capsula text, massa real)')
    c.execute('CREATE TABLE IF NOT EXISTS datafinalDoEnsaio (id INTEGER PRIMARY KEY AUTOINCREMENT, datafinal text)')
    c.execute('CREATE TABLE IF NOT EXISTS dadosIniciais (id INTEGER PRIMARY KEY AUTOINCREMENT, datestamp text, tipoAnel text, diametro_anel real, altura_anel real, massa_anel real, massa_conj real, alt_corpo_prova real, massa_espc real, dateColeta text, local text, operador text, profundidade real)')
    c.execute('CREATE TABLE IF NOT EXISTS umidadeInicial (id integer, cap01 text, cap02 text, cap03 text, massaSeca01 real, massaSeca02 real, massaSeca03 real, massaUmida01 real, massaUmida02 real, massaUmida03 real)')
    c.execute('CREATE TABLE IF NOT EXISTS pressaoAplicada (id integer, id_Estagio integer, pressao_aplicada real)')
    c.execute('CREATE TABLE IF NOT EXISTS coletaDados (id integer, id_Estagio integer, tempo real, raizdotempo real, altura real)')
    c.execute('CREATE TABLE IF NOT EXISTS idDeletados (idDeletados integer)')

create_table()

'''Cria uma Lista Index de visualização e indentificaçãoptimize'''
def ListaVisualizacao():
    a = ids()
    b = juncaoLista()
    cont = 0
    id = len(a) - 1
    c = []
    while cont <= id:
        c.append(a[cont] + b[cont])
        cont = cont +1

    return c

'''Junta as listas para visualização'''
def juncaoLista():
    a = dataInicial()
    b = datafinal()
    c = numEstagio()
    d = []
    cont = 0
    id = len(a) - 1
    e = ['']
    f = ['']
    while cont <= id:
        try:
            d.append([a[cont] + b[cont] + c[cont]])
            cont = cont +1
        except IndexError:
            d.append([a[cont] + e + f])
            cont = cont +1

    return d

'''Lista com os ids'''
def ids():
    lista_id = []

    for row in c.execute('SELECT * FROM dadosIniciais'):
        lista_id.append([row[0]])

    return lista_id

'''Captura as datas finais dos ensaios para criar uma lista para visualização'''
def datafinal():
    list_datefinal = []

    for row in c.execute('SELECT * FROM datafinalDoEnsaio'):
        list_datefinal.append([row[1]])

    return list_datefinal

'''Captura as datas iniciais dos ensaios para criar uma lista para visualização'''
def dataInicial():
    list_dateincial = []

    for row in c.execute('SELECT * FROM dadosIniciais'):
        list_dateincial.append([row[1]])

    return list_dateincial

'''Captura a quantidade de estagio de cada ensaio e cria uma lista para visualização'''
def numEstagio():
    id = 1
    a = ler_quant_ensaios()
    list_numEstagios = []
    b = ler_ID_ensaios_deletados()

    while id <= a:
        if id not in b:
            for row in c.execute('SELECT max(id_Estagio) FROM pressaoAplicada WHERE id = ? ', (id, )):
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

'''Adiciona no banco os dados de tempo e raizdotempo e altura do corpo de prova'''
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

'''Ver a quantidade de ensaios que já foram deletados'''
def quant_ensaios_deletados():
    identificador = []
    for rows in c.execute('SELECT * FROM idDeletados'):
        identificador.append(rows[0])

    id = len(identificador)
    return id

'''Ver os id dos ensaios que foram deletados'''
def ler_ID_ensaios_deletados():
    identificador = []
    for rows in c.execute('SELECT * FROM idDeletados'):
        identificador.append(rows[0])

    return identificador

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

'''Data de quando o ensaio termina'''
def data_termino_Update():
    id = ler_quant_ensaios()
    date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%H:%M:%S  %d/%m/%Y'))
    c.execute("UPDATE datafinalDoEnsaio SET datafinal = ? WHERE id = ?", (date, id,))
    connection.commit()

'''Preenche a dataTermino como Null para não bugar a tabelaInicial'''
def data_termino():
    date = ''
    c.execute("INSERT INTO datafinalDoEnsaio (id, datafinal) VALUES (NULL, ?)", (date,))
    connection.commit()

'''Adiciona os dados iniciais do ensaio no banco'''
def data_entry_dados(tipoAnel, d_anel, a_anel, m_anel, m_conj, alt_cprova, m_esp, dateColeta, local, operador, profundidade):
    datestamp = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%H:%M:%S  %d/%m/%Y'))
    dateColeta = str(datetime.datetime.strptime(str(dateColeta), '%m/%d/%y %H:%M:%S').strftime('%d-%m-%Y'))
    c.execute("INSERT INTO dadosIniciais (id, datestamp, tipoAnel, diametro_anel, altura_anel, massa_anel, massa_conj, alt_corpo_prova, massa_espc, dateColeta, local, operador, profundidade) VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (datestamp, tipoAnel, d_anel, a_anel, m_anel, m_conj, alt_cprova, m_esp, dateColeta, local, operador, profundidade))
    connection.commit()

'''Adiciona os valores para calcular o teor de umidade inicial'''
def data_entry_umidade(cap01, cap02, cap03, mSeca01, mSeca02, mSeca03, mUmida01, mUmida02, mUmida03):
    id = ler_quant_ensaios()
    c.execute("INSERT INTO umidadeInicial (id, cap01, cap02, cap03, massaSeca01, massaSeca02, massaSeca03, massaUmida01, massaUmida02, massaUmida03) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, cap01, cap02, cap03, mSeca01, mSeca02, mSeca03, mUmida01, mUmida02, mUmida03))
    connection.commit()

'''Deleta o ensaio no banco de dados'''
def delete(id):
    c.execute("DELETE FROM datafinalDoEnsaio WHERE id = ?", (id,))
    c.execute("DELETE FROM dadosIniciais WHERE id = ?", (id,))
    c.execute("DELETE FROM umidadeInicial WHERE id = ?", (id,))
    c.execute("DELETE FROM pressaoAplicada WHERE id = ?", (id,))
    c.execute("DELETE FROM coletaDados WHERE id = ?", (id,))
    c.execute("INSERT INTO idDeletados (idDeletados) VALUES (?)", (id,))
    connection.commit()

################################################################################################################################################
