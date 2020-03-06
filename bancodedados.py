# -*- coding: utf-8 -*-
#SQL

import sqlite3
import time
import datetime
import math

pi = math.pi

connection = sqlite3.connect('banco.db', check_same_thread = False)
c = connection.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS capsulas (id INTEGER PRIMARY KEY AUTOINCREMENT, capsula text, massa real)')
    c.execute('CREATE TABLE IF NOT EXISTS datafinalDoEnsaio (id INTEGER PRIMARY KEY AUTOINCREMENT, datafinal text)')
    c.execute('CREATE TABLE IF NOT EXISTS dadosIniciais (id INTEGER PRIMARY KEY AUTOINCREMENT, datestamp text, tipoAnel text, diametro_anel real, altura_anel real, massa_anel real, massa_conj real, alt_corpo_prova real, massa_espc real, dateColeta text, local text, operador text, profundidade real, nome_Ensaio text)')
    c.execute('CREATE TABLE IF NOT EXISTS umidadeInicial (id integer, cap01 text, cap02 text, cap03 text, massaSeca01 real, massaSeca02 real, massaSeca03 real, massaUmida01 real, massaUmida02 real, massaUmida03 real)')
    c.execute('CREATE TABLE IF NOT EXISTS pressaoAplicada (id integer, id_Estagio integer, pressao_aplicada real, status_estagio integer)')
    c.execute('CREATE TABLE IF NOT EXISTS coletaDados (id integer, id_Estagio integer, tempo real, raizdotempo real, altura real)')
    c.execute('CREATE TABLE IF NOT EXISTS idDeletados (idDeletados integer)')
    c.execute('CREATE TABLE IF NOT EXISTS dateEstagio (id integer, id_Estagio integer, dateInicio text)')
    c.execute('CREATE TABLE IF NOT EXISTS ensaioTara (id integer, tara real)')
    c.execute('CREATE TABLE IF NOT EXISTS pressaoAssentamento (id integer,  pressaoAssentamento real)')

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

'''Retorna uma lista com os dados iniciais do ensaio para criar o CSV'''
def ListaDadosInicias(id):
    lista = []
    for row in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        lista.append(row[1])
        lista.append(row[2])
        lista.append(row[3])
        lista.append(row[4])
        lista.append(row[5])
        lista.append(row[6])
        lista.append(row[7])
        lista.append(row[8])
        lista.append(row[9])
        lista.append(row[10])
        lista.append(row[11])
        lista.append(row[12])
        lista.append(row[13])

    return lista

'''Retorna com o id_Estágio que esta com status de Incompleto'''
def idEstagioStatusIncompleto(id):
    lista = []
    for row in c.execute('SELECT * FROM pressaoAplicada WHERE id = ? and status_estagio = ?', (id,1,)):
        lista.append(row[1])

    return lista[0]

'''Retorna com a Data Final do ensaio para criar o CSV'''
def DataFinalDoEnsaio(id):
    lista = []
    for row in c.execute('SELECT * FROM datafinalDoEnsaio WHERE id = ?', (id,)):
        lista.append(row[1])

    return lista[0]

'''Cria uma Lista com todos os Status de cada Estágio'''
def ListStatursEstagio(id):
    lista = []
    for row in c.execute('SELECT * FROM pressaoAplicada WHERE id = ?', (id,)):
        lista.append(row[3])

    return lista

'''Cria uma Lista Index de visualização dos dados Calculados'''
def JuncaoListaCalculados(id):
    a = ComboEstagios(id)
    b = P_Aplicadas(id)
    c = e_finalEstagio(id)
    cont = 0
    cond = len(a) - 1
    d = []
    while cont <= cond:
        d.append([a[cont]] + [b[cont]] + [c[cont]])
        cont = cont +1

    return d

'''Retorna com uma Lista de todas as Pressoes aplicadas no ensaio'''
def P_Aplicadas(id):
    lista_P = []
    quantEstagio = ler_quant_estagios_no_ensaio(id)
    index = 1

    while index <= quantEstagio:
        for row in c.execute('SELECT * FROM pressaoAplicada WHERE id = ? and id_Estagio = ?', (id, index,)):
            lista_P.append(str(row[2]))

        index = index+1

    return lista_P

'''Retorna com uma Lista de todos os índices de vazios no final de cada Estágio'''
def e_finalEstagio(id):
    lista_E = []
    quantEstagio = ler_quant_estagios_no_ensaio(id)
    AltSol = AlturaSolidos(id)
    AltIncialCp = AlturaInicialCP(id)
    index = 1
    Delta = 0
    while index <= quantEstagio:
        for row0 in c.execute('SELECT max(tempo) FROM coletaDados WHERE id = ? and id_Estagio = ?', (id, index,)):
            row0 = format(row0).replace('(','')
            row0 = format(row0).replace(')','')
            row0 = format(row0).replace(',','')
            tempMax = float(row0)

        for row1 in c.execute('SELECT min(tempo) FROM coletaDados WHERE id = ? and id_Estagio = ?', (id, index,)):
            row1 = format(row1).replace('(','')
            row1 = format(row1).replace(')','')
            row1 = format(row1).replace(',','')
            tempMin = float(row1)

        for rowm in c.execute('SELECT altura FROM coletaDados WHERE id = ? and id_Estagio = ? and tempo = ?', (id, index, tempMin)):
            rowm = format(rowm).replace('(','')
            rowm = format(rowm).replace(')','')
            rowm = format(rowm).replace(',','')
            rowm = float(rowm)

        for rowM in c.execute('SELECT altura FROM coletaDados WHERE id = ? and id_Estagio = ? and tempo = ?', (id, index, tempMax)):
            rowM = format(rowM).replace('(','')
            rowM = format(rowM).replace(')','')
            rowM = format(rowM).replace(',','')
            rowM = float(rowM)

        Delta = Delta + rowm - rowM
        Altura = AltIncialCp - Delta
        e = (Altura/AltSol) - 1
        lista_E.append(str(round(e,4)))

        index = index+1

    return lista_E

'''Retorna com a Altura Inicial do Corpo de Prova'''
def AlturaInicialCP(id):
    altura = []
    for row in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        altura.append(row[7])

    return altura[0]

'''Retorna com a Altura dos Sólidos em milímetros'''
def AlturaSolidos(id):
    altCP = AlturaInicialCP(id)
    e = indiceVaziosInicial(id)

    H = (altCP)/(1+e)

    return H

'''Retorna com o Grau de Saturacao Inicial valor em Decimal'''
def grauSaturacaoInicial(id):
    teorUmidade = teorUmidadeInicial(id)
    massaEspGraos = massaEspecificaGraos(id)
    e = indiceVaziosInicial(id)
    massaEspAGUA = 1.00      #valor considerado 1.00g/cm³

    S = (teorUmidade*massaEspGraos)/(e*massaEspAGUA)

    return S

'''Retorna com o Indice de Vazios Inicial'''
def indiceVaziosInicial(id):
    massaEspGraos = massaEspecificaGraos(id)
    massaAparenteSeca = massaAparenteSecaInicial(id)

    e = (massaEspGraos/massaAparenteSeca) - 1

    return e

'''Retorna com a Massa Especifica Aparente Seca Inicial'''
def massaAparenteSecaInicial(id):
    massaAparenteUmida = massaEspecificaAparenteUmidaInicial(id)
    teorInicial = 100*(teorUmidadeInicial(id))

    massaAparenteSeca = (100*massaAparenteUmida)/(100 + teorInicial)

    return massaAparenteSeca

'''Retorna com a Massa Especifica dos Grãos do Solo'''
def massaEspecificaGraos(id):
    massaEspecifica = []
    for row in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        massaEspecifica.append(row[8])

    return massaEspecifica[0]

'''Retorna com o cálculo da Massa Especifica Aparente Umida Inicial'''
def massaEspecificaAparenteUmidaInicial(id):
    volume = volumeCorpoProva(id)
    massaAnel = []
    massaConj = []

    for row in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        massaAnel.append(row[5])
        massaConj.append(row[6])

    massaCP = massaConj[0] - massaAnel[0]
    massaEspecifica = massaCP/volume

    return massaEspecifica

'''Retorna com o cálculo do volume inicial do corpo de prova em cm³'''
def volumeCorpoProva(id):
    diametro = []
    altura_cp = []

    for row in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        diametro.append(row[3])
        altura_cp.append(row[7])

    diametro = diametro[0]/10
    altura_cp = altura_cp[0]/10
    volume = (pi/4)*(diametro**2)*altura_cp

    return volume

'''Retorna com o cálculo do teor de umidade inicial'''
def teorUmidadeInicial(id):
    list_caps = caps(id)
    massaCap1 = []
    massaCap2 = []
    massaCap3 = []
    massaW1 = []
    massaW2 = []
    massaW3 = []
    massaS1 = []
    massaS2 = []
    massaS3 = []

    for row in c.execute('SELECT * FROM umidadeInicial WHERE id = ?', (id,)):
        massaS1.append(row[4])
        massaS2.append(row[5])
        massaS3.append(row[6])
        massaW1.append(row[7])
        massaW2.append(row[8])
        massaW3.append(row[9])

    for row in c.execute('SELECT massa FROM capsulas WHERE capsula = ?', (list_caps[0],)):
        massaCap1.append(row[0])

    for row in c.execute('SELECT massa FROM capsulas WHERE capsula = ?', (list_caps[1],)):
        massaCap2.append(row[0])

    for row in c.execute('SELECT massa FROM capsulas WHERE capsula = ?', (list_caps[2],)):
        massaCap3.append(row[0])

    try:
        teor_umidade1 = (massaW1[0] - massaS1[0])/(massaS1[0] - massaCap1[0])
        teor_umidade2 = (massaW2[0] - massaS2[0])/(massaS2[0] - massaCap2[0])
        teor_umidade3 = (massaW3[0] - massaS3[0])/(massaS3[0] - massaCap3[0])
        teor_umidade =  (teor_umidade1 + teor_umidade2 + teor_umidade3)/3
    except:
        teor_umidade = 0

    return teor_umidade

'''Retorna com os Pressões aplicas em cada Estágio'''
def Pressao(id, id_Estagio):
    a = []
    for row in c.execute('SELECT * FROM pressaoAplicada WHERE id = ? and id_Estagio = ?', (id, id_Estagio,)):
        a.append(str(row[2]))

    return a

'''Retorna uma lista com os dados coletados'''
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

'''Retorna uma lista com os dados coletados para montar CSV'''
def TabelaEstagioCSV(id, id_Estagio):
    lista = []
    tempos = []
    raiztempo = []
    alturas = []
    cont = 0
    for rows in c.execute('SELECT * FROM coletaDados WHERE id = ? and id_Estagio = ?', (id, id_Estagio,)):
        tempos.append(rows[2])
        raiztempo.append(rows[3])
        alturas.append(rows[4])

    id = len(tempos) - 1
    while cont <= id:
        lista.append([tempos[cont]] + [raiztempo[cont]] + [alturas[cont]])
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
        lista.append('Estagio '+str(i+1))
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

'''Cria uma Lista Index de visualização das Capsulas Cadastrdas'''
def ListaVisualizacaoCap():
    a = idsCap()
    b = juncaoListaCap()
    cont = 0
    id = len(a) - 1
    c = []
    while cont <= id:
        c.append(a[cont] + b[cont])
        cont = cont +1

    return c

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

'''Junta as listas para visualização das Capsulas'''
def juncaoListaCap():
    a = NomeCap()
    b = massaCap()
    d = []
    cont = 0
    id = len(a) - 1
    e = ['']
    f = ['']
    while cont <= id:
        try:
            d.append([a[cont] + b[cont]])
            cont = cont +1
        except IndexError:
            d.append([e + f])
            cont = cont +1

    return d

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

'''Lista com os ids das Capsulas cadastradas'''
def idsCap():
    lista_id = []

    for row in c.execute('SELECT * FROM capsulas ORDER BY capsula ASC'):
        lista_id.append([row[0]])

    return lista_id

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

'''Captura as massas das capsulas cadastradas'''
def massaCap():
    list_massa = []

    for row in c.execute('SELECT * FROM capsulas ORDER BY capsula ASC'):
        list_massa.append([str(row[2])])

    return list_massa

'''Captura os nomes das capsulas cadastradas'''
def NomeCap():
    list_nomeCap = []

    for row in c.execute('SELECT * FROM capsulas ORDER BY capsula ASC'):
        list_nomeCap.append([row[1]])

    return list_nomeCap

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

'''Retorna o Status de cada estágio'''
def StatuStagio(id, id_Estagio):
    lista = []
    for row in c.execute('SELECT * FROM pressaoAplicada WHERE id = ? and id_Estagio = ?', (id, id_Estagio)):
        lista.append(row[3])

    return int(lista[0])

'''Adiciona no banco o Status do estágio'''
def InserirStatuStagio_id(id, id_Estagio):
    status = 0
    c.execute("UPDATE pressaoAplicada SET status_estagio = ? WHERE id = ? and id_Estagio = ?", (status, id, id_Estagio))
    connection.commit()

'''Adiciona no banco o Status do estágio'''
def InserirStatuStagio():
    id = ler_quant_ensaios()
    id_Estagio = ler_quant_estagios() - 1
    status = 0
    c.execute("UPDATE pressaoAplicada SET status_estagio = ? WHERE id = ? and id_Estagio = ?", (status, id, id_Estagio))
    connection.commit()

'''Adiciona no banco os dados da pressão correspondete a cada Estágio dependendo do id e também o valor do status_estagio que inicialmente e zero'''
def InserirDadosPressao_id(id, a, b):
    status = 1
    c.execute("INSERT INTO pressaoAplicada (id, id_Estagio, pressao_aplicada, status_estagio) VALUES (?, ?, ?, ?)", (id, a, b, status))
    connection.commit()

'''Adiciona no banco os dados da pressão correspondete a cada Estágio'''
def InserirDadosPressao(a, b):
    id = ler_quant_ensaios()
    status = 1
    c.execute("INSERT INTO pressaoAplicada (id, id_Estagio, pressao_aplicada, status_estagio) VALUES (?, ?, ?, ?)", (id, a, b, status))
    connection.commit()

'''Adiciona no banco os dados de tempo e raizdotempo e altura do corpo de prova dependendo do id'''
def InserirDados_id(id, id_Estagio, a, b):
    id_Estagio = ler_quant_estagios_id(id) - 1
    if a == 0:
        raizdotempo = 0
    else:
        raizdotempo = a**0.5
    c.execute("INSERT INTO coletaDados (id, id_Estagio, tempo, raizdotempo, altura) VALUES (?, ?, ?, ?, ?)", (id, id_Estagio, a, raizdotempo, b))
    connection.commit()

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

'''Seleciona as Capsulas cadastradas no Banco de dados de acordo com o id'''
def capsulas_id(id):
    lista = []
    for rows in c.execute('SELECT * FROM capsulas WHERE id = ?', (id,)):
        lista.append(rows[1])
        lista.append(str(rows[2]))

    return lista

'''Seleciona o diametro correspondente no banco de dados de acordo com o id'''
def diametro_anel_id(id):
    for rows in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        diametro = rows[3]

    diametro = diametro/100
    return diametro

'''Seleciona o diametro correspondente no banco de dados'''
def diametro_anel():
    id = ler_quant_ensaios()
    for rows in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        diametro = rows[3]

    diametro = diametro/100
    return diametro

'''Ver a quantidade de Estagios que tem no ensaio'''
def ler_quant_estagios_no_ensaio(id):
    identificador = []
    for rows in c.execute('SELECT * FROM pressaoAplicada WHERE id = ?', (id,)):
        identificador.append(rows[1])

    id = len(identificador)
    return id

'''Ver a quantidade de Estagios que tem no ensaio para criar o proximo id_Estagio a depender do id'''
def ler_quant_estagios_id(id):
    identificador = []
    for rows in c.execute('SELECT * FROM pressaoAplicada WHERE id = ?', (id,)):
        identificador.append(rows[1])

    id = len(identificador) + 1
    return id

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

'''Ver a quantidade de capsulas que tem no banco de dados'''
def ler_quant_cap():
    for rows in c.execute('SELECT * FROM capsulas'):
        identificador  = rows[0]

    try:
        return identificador
    except UnboundLocalError:
        return 0

'''Ver a quantidade de ensaios que tem no banco para criar os ids'''
def ler_quant_ensaios():
    for rows in c.execute('SELECT * FROM dadosIniciais'):
        identificador  = rows[0]

    try:
        return identificador
    except UnboundLocalError:
        return 0

'''Ver qual o identificadores do ensaio de acordo com o id'''
def ler_DO_IDE(id):
    lista_IDE = []
    for row in c.execute('SELECT * FROM dadosIniciais WHERE id = ?', (id,)):
        if row[13]!= '':
            lista_IDE.append(row[13])

    return lista_IDE

'''Função que Retorna o id para um novo ensaio'''
def idReturn():
    id = []
    for row in c.execute('SELECT max(id) FROM dadosIniciais'):
        row = format(row).replace('(','')
        row = format(row).replace(')','')
        row = format(row).replace(',','')
        id.append(int(row))

    return id[0]

'''Ver os identificadores de ensaio já cadastrados no banco'''
def ler_IDE():
    lista_IDE = []
    for row in c.execute('SELECT * FROM dadosIniciais'):
        if row[13]!= '':
            lista_IDE.append(row[13])

    return lista_IDE

'''Pega o valor de Tara do ensaio'''
def TARA(id):
    Tara = []
    for row in c.execute('SELECT * FROM ensaioTara  WHERE id = ?', (id,)):
        Tara.append(row[1])

    return Tara[0]

'''Ver as capsulas que já tem no banco'''
def ler_cap():
    lista_capsulas = []
    for row in c.execute('SELECT * FROM capsulas ORDER BY capsula ASC'):
        lista_capsulas.append(row[1])

    return lista_capsulas

'''Atualiza uma capsula no banco'''
def update_capsulas(id, a, b):
    c.execute("UPDATE capsulas SET capsula = ? WHERE id = ?", (a, id,))
    c.execute("UPDATE capsulas SET massa = ? WHERE id = ?", (b, id,))
    connection.commit()

'''Cadastra uma capsula no banco'''
def data_entry_cap(a, b):
    c.execute("INSERT INTO capsulas (id, capsula, massa) VALUES (NULL, ?, ?)", (a, b))
    connection.commit()

'''Data de quando o ensaio termina de acordo com o id'''
def data_termino_Update_id(id):
    date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%H:%M:%S  %d/%m/%Y'))
    c.execute("UPDATE datafinalDoEnsaio SET datafinal = ? WHERE id = ?", (date, id,))
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

'''Adiciona no banco a Pressao de Assentamento Utilizada no ensaio'''
def pAssentamento(id, Assentamento):
    c.execute("INSERT INTO pressaoAssentamento (id, pressaoAssentamento) VALUES (?, ?)", (id, Assentamento))
    connection.commit()

'''Adiciona a TARA do transdutor no ensaio'''
def EnsaioTara(id, Tara):
    c.execute("INSERT INTO ensaioTara (id, tara) VALUES (?, ?)", (id, Tara))
    connection.commit()

'''Adiciona a data exata na qual o Estágio de pressão foi iniciado'''
def dataEstagioInicio(id, id_Estagio):
    datestamp = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%H:%M:%S  %d/%m/%Y'))
    c.execute("INSERT INTO dateEstagio (id, id_Estagio, dateInicio) VALUES (?, ?, ?)", (id, id_Estagio, datestamp))
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

'''Deleta uma Cápsula no banco de dados de acordo com o id'''
def deleteCap(id):
    c.execute("DELETE FROM capsulas WHERE id = ?", (id,))
    connection.commit()

'''Deleta o ensaio no banco de dados'''
def delete(id):
    c.execute("DELETE FROM datafinalDoEnsaio WHERE id = ?", (id,))
    c.execute("DELETE FROM dadosIniciais WHERE id = ?", (id,))
    c.execute("DELETE FROM umidadeInicial WHERE id = ?", (id,))
    c.execute("DELETE FROM pressaoAplicada WHERE id = ?", (id,))
    c.execute("DELETE FROM coletaDados WHERE id = ?", (id,))
    c.execute("DELETE FROM dateEstagio WHERE id = ?", (id,))
    c.execute("DELETE FROM ensaioTara WHERE id = ?", (id,))
    c.execute("DELETE FROM pressaoAssentamento WHERE id = ?", (id,))
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
