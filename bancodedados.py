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
    c.execute('CREATE TABLE IF NOT EXISTS dadosIniciais (id INTEGER PRIMARY KEY AUTOINCREMENT, datestamp text, tipoAnel text, diametro_anel real, altura_anel real, massa_anel real, massa_conj real, alt_corpo_prova real, massa_espc real, dateColeta text, local text, operador text, profundidade real, nome_Ensaio text)')
    c.execute('CREATE TABLE IF NOT EXISTS umidadeInicial (id integer, cap01 text, cap02 text, cap03 text, massaSeca01 real, massaSeca02 real, massaSeca03 real, massaUmida01 real, massaUmida02 real, massaUmida03 real)')
    c.execute('CREATE TABLE IF NOT EXISTS pressaoAplicada (id integer, id_Estagio integer, pressao_aplicada real)')
    c.execute('CREATE TABLE IF NOT EXISTS coletaDados (id integer, id_Estagio integer, tempo real, raizdotempo real, altura real)')
    c.execute('CREATE TABLE IF NOT EXISTS idDeletados (idDeletados integer)')

create_table()

'''Atualiza todos os dados iniciais do ensaio no banco de dados'''
def UpdateDadosEnsaio(id, tipoA, diametro, alturaA, massaA, massaC, altCP, massaEsp, dateCol, local, oper, prof, c1, c2, c3, ms1, ms2, ms3, mu1, mu2, mu3, IDE):
    c.execute("UPDATE dadosIniciais SET tipoAnel = ? WHERE id = ?", (tipoA, id,))
    c.execute("UPDATE dadosIniciais SET diametro_anel = ? WHERE id = ?", (diametro, id,))
    c.execute("UPDATE dadosIniciais SET altura_anel = ? WHERE id = ?", (alturaA, id,))
    c.execute("UPDATE dadosIniciais SET massa_anel = ? WHERE id = ?", (massaA, id,))
    c.execute("UPDATE dadosIniciais SET massa_conj = ? WHERE id = ?", (massaC, id,))
    c.execute("UPDATE dadosIniciais SET alt_corpo_prova = ? WHERE id = ?", (altCP, id,))
    c.execute("UPDATE dadosIniciais SET massa_espc = ? WHERE id = ?", (massaEsp, id,))
    c.execute("UPDATE dadosIniciais SET dateColeta = ? WHERE id = ?", (dateCol, id,))
    c.execute("UPDATE dadosIniciais SET local = ? WHERE id = ?", (local, id,))
    c.execute("UPDATE dadosIniciais SET operador = ? WHERE id = ?", (oper, id,))
    c.execute("UPDATE dadosIniciais SET profundidade = ? WHERE id = ?", (prof, id,))
    c.execute("UPDATE dadosIniciais SET nome_Ensaio = ? WHERE id = ?", (IDE, id,))
    c.execute("UPDATE umidadeInicial SET cap01 = ? WHERE id = ?", (c1, id,))
    c.execute("UPDATE umidadeInicial SET cap02 = ? WHERE id = ?", (c2, id,))
    c.execute("UPDATE umidadeInicial SET cap03 = ? WHERE id = ?", (c3, id,))
    c.execute("UPDATE umidadeInicial SET massaSeca01 = ? WHERE id = ?", (ms1, id,))
    c.execute("UPDATE umidadeInicial SET massaSeca02 = ? WHERE id = ?", (ms2, id,))
    c.execute("UPDATE umidadeInicial SET massaSeca03 = ? WHERE id = ?", (ms3, id,))
    c.execute("UPDATE umidadeInicial SET massaUmida01 = ? WHERE id = ?", (mu1, id,))
    c.execute("UPDATE umidadeInicial SET massaUmida02 = ? WHERE id = ?", (mu2, id,))
    c.execute("UPDATE umidadeInicial SET massaUmida03 = ? WHERE id = ?", (mu3, id,))
    connection.commit()

'''Retorna com os Pressões aplicas em cada Estágio'''
def Pressao(id, id_Estagio):
    a = []
    for row in c.execute('SELECT * FROM pressaoAplicada WHERE id = ? and id_Estagio = ?', (id, id_Estagio,)):
        a.append(str(row[2]))

    return a

'''Retorna uma lista com os dados coletados que podem ser editados'''
def TabelaEstagio(id, id_Estagio):
    lista = []
    tempos = []
    alturas = []
    cont = 0
    for rows in c.execute('SELECT * FROM coletaDados WHERE id = ? and id_Estagio = ?', (id, id_Estagio,)):
        tempos.append(str(rows[2]))
        alturas.append(str(rows[4]))

    id = len(tempos) - 1
    while cont <= id:
        lista.append([tempos[cont]] + [alturas[cont]])
        cont = cont + 1

    return lista

'''Retorna uma Lista de Estágios para visualização e edição'''
def ComboEstagios(id):
    lista = []
    i = 0

    for row in c.execute('SELECT max(id_Estagio) FROM pressaoAplicada WHERE id = ? ', (id, )):
        row = format(row).replace('(','')
        row = format(row).replace(')','')
        row = format(row).replace(',','')
        row = int(row)



    while i < row:
        lista.append('Estágio '+str(i+1))
        i = i+1

    return lista

'''Atualiza os valores das massas secas no banco de dados'''
def UpdateMassaSeca(id, m, n, o):
    c.execute("UPDATE umidadeInicial SET massaSeca01 = ? WHERE id = ?", (m, id,))
    c.execute("UPDATE umidadeInicial SET massaSeca02 = ? WHERE id = ?", (n, id,))
    c.execute("UPDATE umidadeInicial SET massaSeca03 = ? WHERE id = ?", (o, id,))
    connection.commit()

'''Funcao responsavel em pegar todos os dados iniciais do ensaio para exibicao'''
def DadosIniciaisParaEdit(id):
    lista_dados = []
    #pega o tipo de anel (i = 0)
    for row in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        lista_dados.append(str(row[2]))

    #pega o diametro interno do anel (i = 1)
    for row in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        lista_dados.append(str(row[3]))

    #pega altura do anel (i = 2)
    for row in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        lista_dados.append(str(row[4]))

    #pega massa do anel (i = 3)
    for row in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        lista_dados.append(str(row[5]))

    #pega altura do corpo-de-prova (i = 4)
    for row in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        lista_dados.append(str(row[7]))

    #pega a massa especifica dos grãos (i = 5)
    for row in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        lista_dados.append(str(row[8]))

    #pega a massa do corpo-de-prova (i = 6)
    for row in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        lista_dados.append(str(row[6]-row[5]))

    #pega o local da coleta (i = 7)
    for row in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        lista_dados.append(row[10])

    #pega o operador da coleta (i = 8)
    for row in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        lista_dados.append(row[11])

    #pega a profundidade da coleta (i = 9)
    for row in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        lista_dados.append(str(row[12]))

    #pega a data da coleta (i = 10)
    for row in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        data = row[9]
        data = format(data).replace('-','/')
        lista_dados.append(data)

    #pega o IDE (Identificador do ensaio) da coleta (i = 11)
    for row in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        lista_dados.append(str(row[13]))

    return lista_dados

'''Funcao responsavel em pegar as capsulas usadas no ensaio'''
def caps(id):
    caps = []
    for row in c.execute('SELECT * FROM umidadeInicial WHERE id = ?', (id,)):
        caps.append(row[1])
    for row in c.execute('SELECT * FROM umidadeInicial WHERE id = ?', (id,)):
        caps.append(row[2])
    for row in c.execute('SELECT * FROM umidadeInicial WHERE id = ?', (id,)):
        caps.append(row[3])

    return caps

'''Funcao responsavel em pegar os valores de Massa Seca'''
def mSeca(id):
    massaSeca = []
    for row in c.execute('SELECT * FROM umidadeInicial WHERE id = ?', (id,)):
        massaSeca.append(str(row[4]))
    for row in c.execute('SELECT * FROM umidadeInicial WHERE id = ?', (id,)):
        massaSeca.append(str(row[5]))
    for row in c.execute('SELECT * FROM umidadeInicial WHERE id = ?', (id,)):
        massaSeca.append(str(row[6]))

    return massaSeca

'''Funcao responsavel em pegar os valores de Massa Umida'''
def mUmida(id):
    massaUmida = []
    for row in c.execute('SELECT * FROM umidadeInicial WHERE id = ?', (id,)):
        massaUmida.append(str(row[7]))
    for row in c.execute('SELECT * FROM umidadeInicial WHERE id = ?', (id,)):
        massaUmida.append(str(row[8]))
    for row in c.execute('SELECT * FROM umidadeInicial WHERE id = ?', (id,)):
        massaUmida.append(str(row[9]))

    return massaUmida

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
    g = IDE()
    h = ['']
    while cont <= id:
        try:
            d.append([g[cont] + a[cont] + b[cont] + c[cont]])
            cont = cont +1
        except IndexError:
            d.append([h + a[cont] + e + f])
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

'''Captura os IDE (Identificadores de cada Ensaio)'''
def IDE():
    list_IDE = []

    for row in c.execute('SELECT * FROM dadosIniciais'):
        list_IDE.append([row[13]])

    return list_IDE

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
def data_entry_dados(tipoAnel, d_anel, a_anel, m_anel, m_conj, alt_cprova, m_esp, dateColeta, local, operador, profundidade, IDE_E):
    datestamp = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%H:%M:%S  %d/%m/%Y'))
    dateColeta = str(datetime.datetime.strptime(str(dateColeta), '%m/%d/%y %H:%M:%S').strftime('%d-%m-%Y'))
    c.execute("INSERT INTO dadosIniciais (id, datestamp, tipoAnel, diametro_anel, altura_anel, massa_anel, massa_conj, alt_corpo_prova, massa_espc, dateColeta, local, operador, profundidade, nome_Ensaio) VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (datestamp, tipoAnel, d_anel, a_anel, m_anel, m_conj, alt_cprova, m_esp, dateColeta, local, operador, profundidade, IDE_E))
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

'''Deleta um estagio no banco de dados e organiza os demais estagios em sequencia'''
def deleteEstagio(id, id_Estagio, diferenca):
    c.execute("DELETE FROM pressaoAplicada WHERE id = ? and id_Estagio = ?", (id, id_Estagio))
    c.execute("DELETE FROM coletaDados WHERE id = ? and id_Estagio = ?", (id, id_Estagio))
    connection.commit()
    cont = 1
    novo_id = id_Estagio

    while cont<=diferenca:
        c.execute("UPDATE pressaoAplicada SET id_Estagio = ? WHERE id = ? and id_Estagio = ?", (novo_id, id, (id_Estagio + cont),))
        c.execute("UPDATE coletaDados SET id_Estagio = ? WHERE id = ? and id_Estagio = ?", (novo_id, id, (id_Estagio + cont),))
        connection.commit()
        novo_id = novo_id + 1
        cont = cont + 1

'''Função responsavel por adicionar novos dados coletados no ensaio em funcao de um determinado Estagio'''
def updateAdados(id, id_Estagio, a, b):
    if a == 0:
        raizdotempo = 0
    else:
        raizdotempo = a**0.5

    c.execute("INSERT INTO coletaDados (id, id_Estagio, tempo, raizdotempo, altura) VALUES (?, ?, ?, ?, ?)", (id, id_Estagio, a, raizdotempo, b))
    connection.commit()

'''Função responsavel por excluir os dados coletados em funcao de um determinado Estagio'''
def updateAdadosDEL(id, id_Estagio):
    c.execute("DELETE FROM coletaDados WHERE id = ? and id_Estagio = ?", (id, id_Estagio))
    connection.commit()

'''Função responsavel por editar os dados de pressao Apicada para cada Estagio'''
def updateAdadosPressao(id, id_Estagio, pressao):
    c.execute("UPDATE pressaoAplicada SET pressao_aplicada = ? WHERE id = ? and id_Estagio = ?", (pressao, id, id_Estagio))
    connection.commit()

################################################################################################################################################
