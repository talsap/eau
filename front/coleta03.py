# -*- coding: utf-8 -*-

'''Bibliotecas'''

import wx
import time
import datetime
import math
import serial
import threading
import front.tela
import bancodedados
from sys import *
from serial.tools import list_ports
from front.massaSeca import massaSeca

'''Variaveis Globais'''
rate = 9600
opcaoC = "C"
opcaoD = "D"
opcaoI = "I"
pi = math.pi

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
'''Tela Coleta03. Responsavel de Coletar Dados Para Status Estágio Incompleto. Iniciado na tela Editar'''
class Coleta03(wx.Dialog):
#----------------------------------------------------------------------
        def __init__(self, id, *args, **kwargs):
            wx.Dialog.__init__(self, None, -1, 'EAU - Coleta de Dados', style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
            '''y corresponde sobre o status do preenchimento da massa seca'''
            self.id = id
            self.condicaoConeccao = False

            self.panel = wx.Panel(self)
            self.SetSize((500,425))
            self.Centre()
            self.Show()

            '''ComboBox Port Serial'''
            portlist = [port for port,desc,hwin in list_ports.comports()]

            try:
                self.cboCPort = wx.ComboBox(self.panel, -1, portlist[0] , (410,40), (60, -1), choices=portlist)
            except IndexError:
                self.cboCPort = wx.ComboBox(self.panel, -1, '', (410,40), (60, -1), choices=portlist)
                self.Bind(wx.EVT_COMBOBOX_DROPDOWN, self.onCheck, self.cboCPort)

            self.text00 = wx.StaticText(self.panel, -1, "COM Port", (350,44), (60,-1), wx.ALIGN_LEFT)
            self.numEstagios = '1'
            self.FontTitle = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
            self.title = wx.StaticText(self.panel, -1, 'Estágio ' + self.numEstagios, (20,20), (460,-1), wx.ALIGN_CENTER)
            self.title.SetFont(self.FontTitle)
            self.massaAplicada = wx.TextCtrl(self.panel, -1, '', (370,70),(100,-1), wx.TE_RIGHT)
            self.Bind(wx.EVT_TEXT, self.textDinamic01, self.massaAplicada)
            self.texto01 = wx.StaticText(self.panel, -1, 'Massa Aplicada (kg)',(258,75), (109,-1), wx.ALIGN_LEFT)
            self.pressaoAplicada = wx.TextCtrl(self.panel, -1, '', (370,100),(100,-1), wx.TE_RIGHT)
            self.Bind(wx.EVT_TEXT, self.textDinamic02, self.pressaoAplicada)
            self.texto01 = wx.StaticText(self.panel, -1, 'Pressão Aplicada (kPa)',(245,105), (119,-1), wx.ALIGN_LEFT)
            self.prompt = wx.TextCtrl(self.panel, -1, wx.EmptyString, (20, 138), wx.Size(450,200), style = wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_RICH | wx.TE_RICH2)
            self.iniciar = wx.Button(self.panel, -1, 'Iniciar',(137.5, 350), (225,-1), wx.ALIGN_LEFT)
            self.Bind(wx.EVT_BUTTON, self.Iniciar, self.iniciar)

            self.Refresh()
            self.Update()

#----------------------------------------------------------------------
        def ColetaPressaoAssentamento(self, event):
            id = self.id
            pressaoSeguinte = self.pressaoAplicada.GetValue()
            pressaoSeguinte = format(pressaoSeguinte).replace(',','.')
            try:
                pressaoSeguinte = float(pressaoSeguinte)
            except ValueError:
                pressaoSeguinte = -1

            if pressaoSeguinte != '' and pressaoSeguinte > 0:
                self.iniciar.Destroy()
                self.iniciar = wx.Button(self.panel, -1, 'Coletar Pressão de Assentamento',(137.5, 350), (225,-1), wx.ALIGN_LEFT | wx.TE_READONLY)
                self.iniciar.SetForegroundColour((119,118,114))
                self.iniciar.Update()
                self.prompt.AppendText("Coletando Pressão de Assentamento...\n")
                bancodedados.pAssentamento(id, pressaoSeguinte)
                self.Update()
                time.sleep(3)
                self.prompt.AppendText("Aguarde o tempo acabar.\n")
                self.Update()
                self.timer.Start(1000)
            else:
                print('O valor de pressao aplicada nao e adequado')
                menssagError = wx.MessageDialog(self, 'O valor para pressão aplicada não é adequado', 'EAU', wx.OK | wx.ICON_INFORMATION)
                aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                menssagError.ShowModal()
                menssagError.Destroy()

#----------------------------------------------------------------------
        def AguardarTime(self):
            id = self.id
            self.conexao.write(opcaoI)
            time.sleep(3)
            self.prompt.AppendText("Transdutor zerado apartir daqui.\n\n")
            self.Update()
            Tara = float(self.conexao.readline())
            bancodedados.EnsaioTara(id, Tara)
            self.TARA_COLETADA = True
            self.Assentamento = False
            if self.Assentamento == False:
                massaSeguinte = self.massaAplicada.GetValue()
                massaSeguinte = format(massaSeguinte).replace(',','.')
                massaSeguinte = float(massaSeguinte)
                massaSeguinte = massaSeguinte*2
                massaSeguinte = str(massaSeguinte)
                pressaoSeguinte = self.pressaoAplicada.GetValue()
                pressaoSeguinte = format(pressaoSeguinte ).replace(',','.')
                pressaoSeguinte = float(pressaoSeguinte)
                pressaoSeguinte = pressaoSeguinte*2
                pressaoSeguinte = str(pressaoSeguinte)
                self.title.Destroy()
                self.massaAplicada.Destroy()
                self.pressaoAplicada.Destroy()
                self.FontTitle = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
                self.title = wx.StaticText(self.panel, -1, 'Estágio ' + self.numEstagios, (20,20), (460,-1), wx.ALIGN_CENTER)
                self.title.SetFont(self.FontTitle)
                self.massaAplicada = wx.TextCtrl(self.panel, -1, massaSeguinte, (370,70),(100,-1), wx.TE_RIGHT)
                self.Bind(wx.EVT_TEXT, self.textDinamic01, self.massaAplicada)
                self.pressaoAplicada = wx.TextCtrl(self.panel, -1, pressaoSeguinte, (370,100),(100,-1), wx.TE_RIGHT)
                self.Bind(wx.EVT_TEXT, self.textDinamic02, self.pressaoAplicada)
                self.title.Update()
                self.massaAplicada.Update()
                self.pressaoAplicada.Update()
                self.Update()
                self.iniciar.Destroy()
                try:
                    self.Fechar.Destroy()
                    self.iniciar = wx.Button(self.panel, -1, 'Coletar',(255, 350), (225,-1), wx.ALIGN_LEFT | wx.TE_READONLY)
                    self.Fechar = wx.Button(self.panel, -1, 'Terminar Estágio',(20, 350), (225,-1), wx.ALIGN_LEFT)
                    self.Fechar.SetForegroundColour((119,118,114))
                    self.Bind(wx.EVT_BUTTON, self.ColetaDados, self.iniciar)
                    self.Update()
                except:
                    self.iniciar = wx.Button(self.panel, -1, 'Coletar',(255, 350), (225,-1), wx.ALIGN_LEFT)
                    self.Fechar = wx.Button(self.panel, -1, 'Terminar Estágio',(20, 350), (225,-1), wx.ALIGN_LEFT | wx.TE_READONLY)
                    self.Fechar.SetForegroundColour((119,118,114))
                    self.Bind(wx.EVT_BUTTON, self.ColetaDados, self.iniciar)
                    self.Update()

#----------------------------------------------------------------------
        def ColetaDados(self, event):
            pressaoSeguinte = self.pressaoAplicada.GetValue()
            pressaoSeguinte = format(pressaoSeguinte).replace(',','.')
            id = self.id
            AlturaInicialCP = bancodedados.DadosIniciaisParaEdit(id)    #lista dos dados iniciais
            AlturaInicialCP = float(AlturaInicialCP[4])                 #para indice 4 retorna altura do corpo de prova

            try:
                pressaoSeguinte = float(pressaoSeguinte)
            except ValueError:
                pressaoSeguinte = -1

            if pressaoSeguinte != '' and pressaoSeguinte > 0:
                self.iniciar.Destroy()
                try:
                    self.Fechar.Destroy()
                    self.iniciar = wx.Button(self.panel, -1, 'Coletar',(255, 350), (225,-1), wx.ALIGN_LEFT | wx.TE_READONLY)
                    self.Fechar = wx.Button(self.panel, -1, 'Terminar Estágio',(20, 350), (225,-1), wx.ALIGN_LEFT)
                    self.iniciar.SetForegroundColour((119,118,114))
                    self.Bind(wx.EVT_BUTTON, self.Terminar, self.Fechar)
                    self.Update()
                except:
                    self.iniciar = wx.Button(self.panel, -1, 'Coletar',(255, 350), (225,-1), wx.ALIGN_LEFT)
                    self.Fechar = wx.Button(self.panel, -1, 'Terminar Estágio',(20, 350), (225,-1), wx.ALIGN_LEFT | wx.TE_READONLY)
                    self.iniciar.SetForegroundColour((119,118,114))
                    self.Bind(wx.EVT_BUTTON, self.Terminar, self.Fechar)
                    self.Update()

                cont = self.numEstagios #cont corresponde ao Estágio
                cont = int(cont)
                self.cont = cont
                bancodedados.InserirDadosPressao_id(id, cont, pressaoSeguinte)
                if cont == 1 and self.TARA_COLETADA == False:
                    self.prompt.AppendText(" _ _ _ _ _ _ _ _ Estagio " + str(cont) + " _ _ _ _ _ _ _ _ \n")
                    self.conexao.write(opcaoI)
                    tudopronto = False
                    try:
                        Tara = float(self.conexao.readline())
                        valor = Tara
                        bancodedados.EnsaioTara(id, Tara)
                        bancodedados.dataEstagioInicio(id, cont)
                        tudopronto = True
                        self.NOVATREADING(id, cont, AlturaInicialCP, Tara, valor, tudopronto)
                    except ValueError:
                        self.prompt.AppendText("erro1! O tempo de resposta do arduino com o software impede de coletar.\n")
                        #erro1. Entende-se que o software está recebedo um valor errado da porta serial, devido ao delay médio de +- 2.5 seg de resposta. Esse erro pode acontecer em computadres lentos.
                else:
                    self.prompt.AppendText(" _ _ _ _ _ _ _ _ Estagio " + str(cont) + " _ _ _ _ _ _ _ _ \n")
                    self.conexao.write(opcaoI)
                    tudopronto = False
                    try:
                        valor = float(self.conexao.readline())
                        Tara =  bancodedados.TARA(id)
                        bancodedados.dataEstagioInicio(id, cont)
                        tudopronto = True
                        self.NOVATREADING(id, cont, AlturaInicialCP, Tara, valor, tudopronto)
                    except:
                        elf.prompt.AppendText("erro1! O tempo de resposta do arduino com o software impede de coletar.\n")
                        #erro1. Entende-se que o software está recebedo um valor errado da porta serial, devido ao delay médio de +- 2.5 seg de resposta. Esse erro pode acontecer em computadres lentos.

            else:
                print('O valor de pressao aplicada nao e adequado')
                menssagError = wx.MessageDialog(self, 'O valor para pressão aplicada não é adequado', 'EAU', wx.OK | wx.ICON_INFORMATION)
                aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                menssagError.ShowModal()
                menssagError.Destroy()

#----------------------------------------------------------------------
        def NOVATREADING(self, id, cont, AlturaInicialCP, Tara, valor, tudopronto):
            #----------------------------------------------------------------------
            def worker(self, id, id_Estagio, AlturaInicialCP, Tara, valorI, tudopronto):
                self.prompt.AppendText("   Tempo (s)   |   Deformação (mm)\n")
                contador = 0
                loadingValor = 0
                acadaMin = 540
                self._stop_flag = False

                while tudopronto == True:
                    if contador == 0:
                        try:
                            altura = AlturaInicialCP - Tara + valorI
                            bancodedados.InserirDados_id(id, id_Estagio, float(contador), altura)
                            self.prompt.AppendText("       "+str(contador).zfill(5)+"       |          "+str(round(altura, 3))+"\n")
                            self.Update()
                        except ValueError:
                            self.prompt.AppendText("\n#error.")


                    if contador == 2 or contador == 4 or contador == 6 or contador == 8 or contador == 10:
                        loadingValor = loadingDestroy(self.x, self.line)
                        try:
                            self.conexao.write(opcaoI)
                            valor = float(self.conexao.readline())
                            altura = AlturaInicialCP - Tara + valor
                            bancodedados.InserirDados_id(id, id_Estagio, float(contador), altura)
                            self.prompt.AppendText("       "+str(contador).zfill(5)+"       |          "+str(round(altura, 3))+"\n")
                            self.Update()
                        except ValueError:
                            self.prompt.AppendText("\n#error.")


                    if contador == 15 or contador == 20 or contador == 25 or contador == 30 or contador == 35 or contador == 40 or contador == 45 or contador == 50 or contador == 55 or contador == 60:
                        loadingValor = loadingDestroy(self.x, self.line)
                        try:
                            self.conexao.write(opcaoI)
                            valor = float(self.conexao.readline())
                            altura = AlturaInicialCP - Tara + valor
                            bancodedados.InserirDados_id(id, id_Estagio, float(contador), altura)
                            self.prompt.AppendText("       "+str(contador).zfill(5)+"       |          "+str(round(altura, 3))+"\n")
                            self.Update()
                        except ValueError:
                            self.prompt.AppendText("\n#error.")

                    if contador == 75 or contador == 90 or contador == 105 or contador == 120 or contador == 135 or contador == 150 or contador == 165 or contador == 180:
                        loadingValor = loadingDestroy(self.x, self.line)
                        try:
                            self.conexao.write(opcaoI)
                            valor = float(self.conexao.readline())
                            altura = AlturaInicialCP - Tara + valor
                            bancodedados.InserirDados_id(id, id_Estagio, float(contador), altura)
                            self.prompt.AppendText("       "+str(contador).zfill(5)+"       |          "+str(round(altura, 3))+"\n")
                            self.Update()
                        except ValueError:
                            self.prompt.AppendText("\n#error.")

                    if contador == 210 or contador == 240 or contador == 270 or contador == 300 or contador == 330 or contador == 360 or contador == 390 or contador == 420 or contador == 450 or contador == 480:
                        loadingValor = loadingDestroy(self.x, self.line)
                        try:
                            self.conexao.write(opcaoI)
                            valor = float(self.conexao.readline())
                            altura = AlturaInicialCP - Tara + valor
                            bancodedados.InserirDados_id(id, id_Estagio, float(contador), altura)
                            self.prompt.AppendText("       "+str(contador).zfill(5)+"       |          "+str(round(altura, 3))+"\n")
                            self.Update()
                        except ValueError:
                            self.prompt.AppendText("\n#error.")

                    if contador == acadaMin:
                        loadingValor = loadingDestroy(self.x, self.line)
                        try:
                            self.conexao.write(opcaoI)
                            valor = float(self.conexao.readline())
                            altura = AlturaInicialCP - Tara + valor
                            bancodedados.InserirDados_id(id, id_Estagio, float(contador), altura)
                            self.prompt.AppendText("       "+str(contador).zfill(5)+"       |          "+str(round(altura, 3))+"\n")
                            self.Update()
                            acadaMin = acadaMin + 60
                        except ValueError:
                            self.prompt.AppendText("\n#error.")

                    if  loadingValor<4:
                        self.prompt.write(".")
                        if loadingValor == 0:
                            self.line = self.prompt.GetNumberOfLines()
                            self.x = int(self.prompt.GetLastPosition())

                        loadingValor += 1

                    if  loadingValor==4:
                        loadingValor = loadingDestroy(self.x, self.line)

                    contador = contador + 1
                    time.sleep(1)
                    if self._stop_flag:
                        tudopronto = False
                        break

            #----------------------------------------------------------------------
            self.t = threading.Thread(target=worker, args=(self, id, cont, AlturaInicialCP, Tara, valor, tudopronto))
            try:
                self.t.start()
            except:
                self.t.run()

            #----------------------------------------------------------------------
            def loadingDestroy(x, line):
                b = self.prompt.GetLineLength(line)
                self.prompt.Remove(x-1,x+b)
                return 0

#----------------------------------------------------------------------
        def Iniciar(self, event):
            Assentamento = self.Assentamento
            condicaoPorta = False
            porta = self.cboCPort.GetValue()
            time.sleep(1)
            self.prompt.AppendText("Inicializando...\n")
            self.Update()
            time.sleep(1.3)
            self.prompt.AppendText("Testando Conexão com porta serial...\n" )
            self.Update()

            if porta == '':
                print("Nenhuma porta esta selecionada")
                time.sleep(0.2)
                self.prompt.AppendText("Nenhuma porta serial foi selecionada.\n")
                self.Update()

            else:
                a = self.testar()
                time.sleep(1)
                if a == 'c':
                  self.prompt.AppendText("Conexão estabelecida.\n\n")
                  self.Update()
                  condicaoPorta = True

            if condicaoPorta == True and Assentamento == True:
                self.prompt.AppendText("Adicione uma pressão de Assentamento.\n")
                self.iniciar.Destroy()
                self.iniciar = wx.Button(self.panel, -1, 'Coletar Pressão de Assentamento',(137.5, 350), (225,-1), wx.ALIGN_LEFT | wx.TE_READONLY)
                self.Bind(wx.EVT_BUTTON, self.ColetaPressaoAssentamento, self.iniciar)
                self.Update()

            if condicaoPorta == True and Assentamento == False:
                self.iniciar.Destroy()
                try:
                    self.Fechar.Destroy()
                    self.iniciar = wx.Button(self.panel, -1, 'Coletar',(255, 350), (225,-1), wx.ALIGN_LEFT | wx.TE_READONLY)
                    self.Fechar = wx.Button(self.panel, -1, 'Terminar Estágio',(20, 350), (225,-1), wx.ALIGN_LEFT)
                    self.Fechar.SetForegroundColour((119,118,114))
                    self.Bind(wx.EVT_BUTTON, self.ColetaDados, self.iniciar)
                    self.Update()
                except:
                    self.iniciar = wx.Button(self.panel, -1, 'Coletar',(255, 350), (225,-1), wx.ALIGN_LEFT)
                    self.Fechar = wx.Button(self.panel, -1, 'Terminar Estágio',(20, 350), (225,-1), wx.ALIGN_LEFT | wx.TE_READONLY)
                    self.Fechar.SetForegroundColour((119,118,114))
                    self.Bind(wx.EVT_BUTTON, self.ColetaDados, self.iniciar)
                    self.Update()

#----------------------------------------------------------------------
        def updatePageFinalEstagio(self):
            '''Atualiza a página quando acabar a coleta de Dados'''
            id = self.id
            cont = self.numEstagios #cont corresponde ao Estágio
            cont = int(cont)
            cont = cont + 1
            self.numEstagios = str(cont)
            time.sleep(1)

            '''y corresponde o status sobre o preenchimento da massa seca'''
            y = int(self.y)

            if cont == 2 and y == 0:
                dialogo = massaSeca(id)
                resultado = dialogo.ShowModal()

            self.iniciar.Destroy()
            self.Fechar.Destroy()
            self.iniciar = wx.Button(self.panel, -1, 'Continuar',(255, 350), (225,-1), wx.ALIGN_LEFT)
            self.Fechar = wx.Button(self.panel, -1, 'Finalizar Ensaio',(20, 350), (225,-1), wx.ALIGN_LEFT)
            self.Bind(wx.EVT_BUTTON, self.Continuar, self.iniciar)
            self.Bind(wx.EVT_BUTTON, self.dlg, self.Fechar)
            self.iniciar.Update()
            self.Fechar.Update()
            self.Update()

#----------------------------------------------------------------------
        def Continuar(self, event):
            condicaoPorta = False
            porta = self.cboCPort.GetValue()
            self.prompt.Clear()
            if porta == '':
                print("Nenhuma porta esta selecionada")
                time.sleep(0.2)
                self.prompt.AppendText("Nenhuma porta serial foi selecionada.\n")
                self.Update()

            else:
                a = self.testar()
                time.sleep(1)
                if a == 'c':
                  self.prompt.AppendText("Conexão estabelecida.\n\n")
                  self.Update()
                  condicaoPorta = True

            if condicaoPorta == True:
                massaSeguinte = self.massaAplicada.GetValue()
                massaSeguinte = format(massaSeguinte).replace(',','.')
                massaSeguinte = float(massaSeguinte)
                massaSeguinte = massaSeguinte*2
                massaSeguinte = str(massaSeguinte)
                pressaoSeguinte = self.pressaoAplicada.GetValue()
                pressaoSeguinte = format(pressaoSeguinte ).replace(',','.')
                pressaoSeguinte = float(pressaoSeguinte)
                pressaoSeguinte = pressaoSeguinte*2
                pressaoSeguinte = str(pressaoSeguinte)
                self.title.Destroy()
                self.massaAplicada.Destroy()
                self.pressaoAplicada.Destroy()
                self.FontTitle = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
                self.title = wx.StaticText(self.panel, -1, 'Estágio ' + self.numEstagios, (20,20), (460,-1), wx.ALIGN_CENTER)
                self.title.SetFont(self.FontTitle)
                self.massaAplicada = wx.TextCtrl(self.panel, -1, massaSeguinte, (370,70),(100,-1), wx.TE_RIGHT)
                self.Bind(wx.EVT_TEXT, self.textDinamic01, self.massaAplicada)
                self.pressaoAplicada = wx.TextCtrl(self.panel, -1, pressaoSeguinte, (370,100),(100,-1), wx.TE_RIGHT)
                self.Bind(wx.EVT_TEXT, self.textDinamic02, self.pressaoAplicada)
                self.title.Update()
                self.massaAplicada.Update()
                self.pressaoAplicada.Update()
                self.Update()

                self.iniciar.Destroy()
                try:
                    self.Fechar.Destroy()
                    self.iniciar = wx.Button(self.panel, -1, 'Coletar',(255, 350), (225,-1), wx.ALIGN_LEFT | wx.TE_READONLY)
                    self.Fechar = wx.Button(self.panel, -1, 'Terminar Estágio',(20, 350), (225,-1), wx.ALIGN_LEFT)
                    self.Fechar.SetForegroundColour((119,118,114))
                    self.Bind(wx.EVT_BUTTON, self.ColetaDados, self.iniciar)
                    self.Update()
                except:
                    self.iniciar = wx.Button(self.panel, -1, 'Coletar',(255, 350), (225,-1), wx.ALIGN_LEFT)
                    self.Fechar = wx.Button(self.panel, -1, 'Terminar Estágio',(20, 350), (225,-1), wx.ALIGN_LEFT | wx.TE_READONLY)
                    self.Fechar.SetForegroundColour((119,118,114))
                    self.Bind(wx.EVT_BUTTON, self.ColetaDados, self.iniciar)
                    self.Update()

#----------------------------------------------------------------------
        def textDinamic01(self, event):
            '''Ativar e desativar caixa de texto (Altura do corpo de Prova)'''
            a = self.massaAplicada.GetValue()
            a = format(a).replace(',','.')
            id = self.id

            try:
                d = bancodedados.diametro_anel_id(id)
                a = float(a)
                b = a*9.81*4/(pi*d*d)
                b = format(round(b, 2))
                c  = str(b)
                self.pressaoAplicada.Destroy()
                self.pressaoAplicada = wx.TextCtrl(self.panel, -1, c, (370,100),(100,-1), wx.TE_RIGHT)
                self.Bind(wx.EVT_TEXT, self.textDinamic02, self.pressaoAplicada)
                self.Refresh()

            except ValueError:
                pass

#----------------------------------------------------------------------
        def textDinamic02(self, event):
            '''Ativar e desativar caixa de texto (Altura do corpo de Prova)'''
            a = self.pressaoAplicada.GetValue()
            a = format(a).replace(',','.')
            id = self.id

            try:
                d = bancodedados.diametro_anel_id(id)
                a = float(a)
                b = a*d*d*pi/(9.81*4)
                b = format(round(b, 2))
                c  = str(b)
                self.massaAplicada.Destroy()
                self.massaAplicada = wx.TextCtrl(self.panel, -1, c, (370,70),(100,-1), wx.TE_RIGHT)
                self.Bind(wx.EVT_TEXT, self.textDinamic01, self.massaAplicada)
                self.Refresh()
            except ValueError:
                pass

#----------------------------------------------------------------------
        def Terminar(self, event):
            '''Para quando o usuario deseja-se terminar o Estagio de pressão'''
            dlg = wx.MessageDialog(None, 'Deseja terminar esse Estágio de Pressão?', 'EAU', wx.YES_NO | wx .CENTRE| wx.NO_DEFAULT )
            result = dlg.ShowModal()
            id_Estagio = self.cont
            id = self.id

            if result == wx.ID_YES:
                bancodedados.InserirStatuStagio_id(id, id_Estagio)
                self._stop_flag = True
                self.updatePageFinalEstagio()
            else:
                dlg.Destroy()

#----------------------------------------------------------------------
        def dlg(self, event):
            '''Diálogo se deseja realmente sair'''
            dlg = wx.MessageDialog(None, 'Deseja mesmo finalizar o ensaio?', 'EAU', wx.YES_NO | wx .CENTRE| wx.NO_DEFAULT )
            result = dlg.ShowModal()
            id = self.id

            if result == wx.ID_YES:
                try:
                    self.conexao.write(opcaoD)
                except:
                    pass

                bancodedados.data_termino_Update_id(id)
                self.Close(True)
                a = wx.Window.FindWindowByName('Facade', parent = None)
                a.list_ctrl.UpdateListCtrl()

            else:
                dlg.Destroy()

#---------------------------------------------------------------------------------------------------------------------------------
        def testar(self):
            '''Testa a Conecção'''
            porta = self.cboCPort.GetValue()

            if self.condicaoConeccao == False:
                try:
                    self.conexao = serial.Serial(porta, rate)
                    self.prompt.AppendText("Verificando Conexão com porta serial "+str(porta)+"...\n" )
                    time.sleep(2)
                    self.conexao.write(opcaoC)
                    self.Update()
                    a = self.conexao.readline()
                    self.condicaoConeccao = True
                    return a[0]
                except:
                    time.sleep(1)
                    self.prompt.AppendText("Não foi possível manter a conexão! Verifique a conexao usb.\n" )
                    self.Update()
                    return 0
            else:
                try:
                    self.conexao.write(opcaoC)
                    self.prompt.AppendText("Verificando Conexão com porta serial "+str(porta)+"...\n" )
                    self.Update()
                    a = self.conexao.readline()
                    return a[0]
                except:
                    self.prompt.AppendText("Não foi possível manter a conexão!\n" )
                    self.condicaoConeccao = False
                    self.Update()
                    return 0

#---------------------------------------------------------------------------------------------------------------------------------
        def onCheck(self, event):
            '''Atualiza os COM Port quando clica-se no ComboBox'''
            '''ComboBox Port Serial'''
            portlist = [port for port,desc,hwin in list_ports.comports()]

            self.cboCPort.Destroy()
            try:
                self.cboCPort = wx.ComboBox(self.panel, -1, portlist[0] , (410,40), (60, -1), choices=portlist)
                self.cboCPort.Update()
            except IndexError:
                self.cboCPort = wx.ComboBox(self.panel, -1, '', (410,40), (60, -1), choices=portlist)
                self.Bind(wx.EVT_COMBOBOX_DROPDOWN, self.onCheck, self.cboCPort)
                self.cboCPort.Update()

#----------------------------------------------------------------------
        def update(self, event):
            cronometro = str(datetime.datetime.fromtimestamp(self.crono).strftime('%M:%S'))
            self.prompt.AppendText(cronometro)
            self.prompt.Update()
            time.sleep(0.3)
            l = self.prompt.GetNumberOfLines()
            g = int(self.prompt.GetLastPosition())
            h = self.prompt.GetLineLength(l)
            self.prompt.Remove(g-5,g-4+h)
            self.crono = self.crono - 1
            if self.crono == 0:
                self.timer.Stop()
                self.AguardarTime()

#----------------------------------------------------------------------
        def onExit(self, event):
            '''Opcao Sair'''
            self.Close(True)

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
