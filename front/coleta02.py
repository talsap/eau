# -*- coding: utf-8 -*-

'''Bibliotecas'''

import wx
from addados02 import AddDados02
from massaSeca import massaSeca
import bancodedados
import math

pi = math.pi
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

'''Tela Cadastrar Cápsula'''
class Coleta02(wx.Dialog):

#----------------------------------------------------------------------
        def __init__(self, id, *args, **kwargs):
            wx.Dialog.__init__(self, None, -1, 'EAU - Coleta de Dados', style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

            '''id do ensaio ao qual será realizado a coleta de dados'''
            self.id = id

            self.panel = wx.Panel(self)
            self.SetSize((500,425))
            self.Centre()
            self.Show()

            self.numEstagios = '1'
            self.FontTitle = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
            self.title = wx.StaticText(self.panel, -1, 'Estágio ' + self.numEstagios, (20,20), (460,-1), wx.ALIGN_CENTER)
            self.title.SetFont(self.FontTitle)

            self.massaAplicada = wx.TextCtrl(self.panel, -1, '', (370,60),(100,-1), wx.TE_RIGHT)
            self.Bind(wx.EVT_TEXT, self.textDinamic01, self.massaAplicada)
            self.texto01 = wx.StaticText(self.panel, -1, 'Massa Aplicada (kg)',(258,65), (109,-1), wx.ALIGN_LEFT)
            self.pressaoAplicada = wx.TextCtrl(self.panel, -1, '', (370,90),(100,-1), wx.TE_RIGHT)
            self.Bind(wx.EVT_TEXT, self.textDinamic02, self.pressaoAplicada)
            self.texto01 = wx.StaticText(self.panel, -1, 'Pressão Aplicada (kPa)',(245,95), (119,-1), wx.ALIGN_LEFT)
            self.prompt = wx.TextCtrl(self.panel, -1, wx.EmptyString, (20, 130), wx.Size( 450,200), style = wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_NO_VSCROLL)
            self.iniciar = wx.Button(self.panel, -1, 'Iniciar',(137.5, 350), (225,-1), wx.ALIGN_LEFT)
            self.Bind(wx.EVT_BUTTON, self.Iniciar, self.iniciar)

            self.Refresh()
            self.Update()


#----------------------------------------------------------------------
        def Iniciar(self, event):
            id = self.id
            pressaoSeguinte = self.pressaoAplicada.GetValue()
            pressaoSeguinte = format(pressaoSeguinte ).replace(',','.')

            try:
                pressaoSeguinte = float(pressaoSeguinte)
            except ValueError:
                pressaoSeguinte = -1

            if pressaoSeguinte != '' and pressaoSeguinte > 0:
                cont = self.numEstagios
                cont = int(cont)
                bancodedados.InserirDadosPressao_id(id, cont, pressaoSeguinte)
                dialogo = AddDados02(id, cont)
                resultado = dialogo.ShowModal()
                cont = cont + 1
                self.numEstagios = str(cont)
                self.iniciar.Destroy()
                self.iniciar = wx.Button(self.panel, -1, 'Continuar',(255, 350), (225,-1), wx.ALIGN_LEFT)
                self.Fechar = wx.Button(self.panel, -1, 'Finalizar',(20, 350), (225,-1), wx.ALIGN_LEFT)
                self.Bind(wx.EVT_BUTTON, self.Iniciar, self.iniciar)
                self.Bind(wx.EVT_BUTTON, self.dlg, self.Fechar)
                self.title.Destroy()
                self.FontTitle = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
                self.title = wx.StaticText(self.panel, -1, 'Estágio ' + self.numEstagios, (20,20), (460,-1), wx.ALIGN_CENTER)
                self.title.SetFont(self.FontTitle)

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
                self.massaAplicada.Destroy()
                self.pressaoAplicada.Destroy()
                self.massaAplicada = wx.TextCtrl(self.panel, -1, massaSeguinte, (370,60),(100,-1), wx.TE_RIGHT)
                self.Bind(wx.EVT_TEXT, self.textDinamic01, self.massaAplicada)
                self.pressaoAplicada = wx.TextCtrl(self.panel, -1, pressaoSeguinte, (370,90),(100,-1), wx.TE_RIGHT)
                self.Bind(wx.EVT_TEXT, self.textDinamic02, self.pressaoAplicada)
                self.massaAplicada.Update()
                self.pressaoAplicada.Update()

            else:
                print('O valor de pressao aplicada nao e adequado')
                menssagError = wx.MessageDialog(self, 'O valor para pressão aplicada não é adequado', 'EAU', wx.OK | wx.ICON_INFORMATION)
                aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                menssagError.ShowModal()
                menssagError.Destroy()

#----------------------------------------------------------------------
        def textDinamic01(self, event):
            id = self.id
            '''Ativar e desativar caixa de texto (Altura do corpo de Prova)'''
            a = self.massaAplicada.GetValue()
            a = format(a).replace(',','.')

            try:
                d = bancodedados.diametro_anel_id(id)
                a = float(a)
                b = a*9.81*4/(pi*d*d)
                b = format(round(b, 2))
                c  = str(b)
                self.pressaoAplicada.Destroy()
                self.pressaoAplicada = wx.TextCtrl(self.panel, -1, c, (370,90),(100,-1), wx.TE_RIGHT)
                self.Bind(wx.EVT_TEXT, self.textDinamic02, self.pressaoAplicada)
                self.Refresh()

            except ValueError:
                pass

#----------------------------------------------------------------------
        def textDinamic02(self, event):
            id = self.id
            '''Ativar e desativar caixa de texto (Altura do corpo de Prova)'''
            a = self.pressaoAplicada.GetValue()
            a = format(a).replace(',','.')

            try:
                d = bancodedados.diametro_anel_id(id)
                a = float(a)
                b = a*d*d*pi/(9.81*4)
                b = format(round(b, 2))
                c  = str(b)
                self.massaAplicada.Destroy()
                self.massaAplicada = wx.TextCtrl(self.panel, -1, c, (370,60),(100,-1), wx.TE_RIGHT)
                self.Bind(wx.EVT_TEXT, self.textDinamic01, self.massaAplicada)
                self.Refresh()
            except ValueError:
                pass

#----------------------------------------------------------------------
        def dlg(self, event):
            id = self.id
            '''Diálogo se deseja realmente sair'''
            dlg = wx.MessageDialog(None, 'Deseja mesmo finalizar o ensaio?', 'EAU', wx.YES_NO | wx .CENTRE| wx.NO_DEFAULT )
            result = dlg.ShowModal()

            if result == wx.ID_YES:
                bancodedados.data_termino_Update_id(id)
                self.Close(True)
            else:
                dlg.Destroy()

#----------------------------------------------------------------------
        def onExit(self, event):
            '''Opcao Sair'''
            self.Close(True)

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
