# -*- coding: utf-8 -*-

'''Bibliotecas'''

import wx
from addados import AddDados
import bancodedados
import math

pi = math.pi
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

'''Tela Cadastrar Cápsula'''
class Coleta(wx.Dialog):

#----------------------------------------------------------------------
        def __init__(self, *args, **kwargs):
            wx.Dialog.__init__(self, None, -1, 'EAU')

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
            pressaoSeguinte = self.pressaoAplicada.GetValue()
            pressaoSeguinte = format(pressaoSeguinte ).replace(',','.')

            if pressaoSeguinte != '' and pressaoSeguinte > 0:
                pressao = self.pressaoAplicada.GetValue()
                pressao = format(pressao).replace(',','.')
                cont = self.numEstagios
                cont = int(cont)
                bancodedados.InserirDadosPressao(cont, pressao)
                dialogo = AddDados()
                resultado = dialogo.ShowModal()
                cont = cont + 1
                self.numEstagios = str(cont)
                self.iniciar.Destroy()
                self.iniciar = wx.Button(self.panel, -1, 'Iniciar',(255, 350), (225,-1), wx.ALIGN_LEFT)
                self.Fechar = wx.Button(self.panel, -1, 'Fechar',(20, 350), (225,-1), wx.ALIGN_LEFT)
                self.Bind(wx.EVT_BUTTON, self.Iniciar, self.iniciar)
                self.Bind(wx.EVT_BUTTON, self.dlg, self.Fechar)
                self.title.Destroy()
                self.FontTitle = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
                self.title = wx.StaticText(self.panel, -1, 'Estágio ' + self.numEstagios, (20,20), (460,-1), wx.ALIGN_CENTER)
                self.title.SetFont(self.FontTitle)
                pressaoSeguinte = self.pressaoAplicada.GetValue()
                pressaoSeguinte = format(pressaoSeguinte ).replace(',','.')
                pressaoSeguinte = float(pressaoSeguinte)
                pressaoSeguinte = pressaoSeguinte*2
                pressaoSeguinte = str(pressaoSeguinte)
                self.pressaoAplicada.Destroy()
                self.pressaoAplicada = wx.TextCtrl(self.panel, -1, pressaoSeguinte, (370,90),(100,-1), wx.TE_RIGHT)
                self.Refresh()
                self.Update()
            else:
                print('O valor de pressao aplicada nao e adequado')
                menssagError = wx.MessageDialog(self, 'O valor para pressão aplicada não é adequado', 'EAU', wx.OK | wx.ICON_INFORMATION)
                aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                menssagError.ShowModal()
                menssagError.Destroy()

#----------------------------------------------------------------------
        def textDinamic01(self, event):
            '''Ativar e desativar caixa de texto (Altura do corpo de Prova)'''
            a = self.massaAplicada.GetValue()
            a = format(a).replace(',','.')

            try:
                d = bancodedados.diametro_anel()
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
            '''Ativar e desativar caixa de texto (Altura do corpo de Prova)'''
            a = self.pressaoAplicada.GetValue()
            a = format(a).replace(',','.')

            try:
                d = bancodedados.diametro_anel()
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
            '''Diálogo se deseja realmente sair'''
            dlg = wx.MessageDialog(None, 'Deseja mesmo fechar o ensaio?', 'EAU', wx.YES_NO | wx .CENTRE| wx.NO_DEFAULT )
            result = dlg.ShowModal()

            if result == wx.ID_YES:
                self.Close(True)
                '''self.Bind(wx.EVT_INIT_DIALOG, self.onExit, dlg)'''
            else:
                dlg.Destroy()

#----------------------------------------------------------------------
        def onExit(self, event):
            '''Opcao Sair'''
            self.Close(True)

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
