# -*- coding: utf-8 -*-

'''Bibliotecas'''

import wx
import wx.adv
import bancodedados
from novoensaio import TelaNovoEnsaio

'''Tela Novo Ensaio'''
class TelaNovo(wx.Dialog):
    #--------------------------------------------------
        def __init__(self, *args, **kwargs):
            wx.Dialog.__init__(self, None, -1, 'EAU - Novo Ensaio', style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION)

            self.panel = wx.Panel(self)
            self.SetSize((450,300))
            self.Centre()
            self.Show()

            self.FontTitle =wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
            self.title = wx.StaticText(self.panel, -1, 'Cabeçalho', (20,20), (400,-1), wx.ALIGN_CENTER)
            self.title.SetFont(self.FontTitle)
            self.texto01 = wx.StaticText(self.panel, -1, 'Identificador do Ensaio',(20,54), (128,-1), wx.ALIGN_LEFT)
            self.identificador = wx.TextCtrl(self.panel, -1, '', (148,50),(272,-1), wx.TE_RIGHT)
            self.texto02 = wx.StaticText(self.panel, -1, 'DADOS DA COLETA:',(20,80), (460,-1), wx.ALIGN_LEFT)
            self.texto03 = wx.StaticText(self.panel, -1, 'Data da coleta', (241,103), (80,-1), wx.ALIGN_LEFT)
            self.date = wx.adv.DatePickerCtrl(self.panel, id= wx.ID_ANY, dt=wx.DefaultDateTime, pos=(323,100), size=wx.DefaultSize, style = wx.adv.DP_SHOWCENTURY | wx.adv.DP_DROPDOWN , validator=wx.DefaultValidator, name="datectrl")
            self.texto04 = wx.StaticText(self.panel, -1, 'Local',(85,135), (35,-1), wx.ALIGN_LEFT)
            self.localColeta = wx.TextCtrl(self.panel, -1, '', (120,130),(300,-1), wx.TE_RIGHT)
            self.localColeta.SetMaxLength(40)
            self.texto05 = wx.StaticText(self.panel, -1, 'Operador',(111,165), (55,-1), wx.ALIGN_LEFT)
            self.operador = wx.TextCtrl(self.panel, -1, '', (168,160), (252,-1), wx.TE_RIGHT)
            self.operador.SetMaxLength(40)
            self.texto06 = wx.StaticText(self.panel, -1, 'Profundidade (m)',(250,196), (100,-1), wx.ALIGN_LEFT)
            self.profundidade = wx.TextCtrl(self.panel, -1, '', (350,191),(70,-1), wx.TE_RIGHT)
            self.continuar = wx.Button(self.panel, -1, 'Continuar', (20, 230), (400,-1), wx.ALIGN_LEFT)
            self.Bind(wx.EVT_BUTTON, self.Prosseguir, self.continuar)

    #--------------------------------------------------
        def Prosseguir(self, event):
            a = self.date.GetValue()
            b = self.localColeta.GetValue()
            c = self.operador.GetValue()
            d = self.profundidade.GetValue()
            d = format(d).replace(',','.')
            d = format(d).replace('-','')
            e = self.identificador.GetValue()

    #--------------------------------------------------
            try:
                if d!= '':
                    d = float(d)

            except ValueError:
                print('Os valores digitados em algum dos campos nao esta da maneira esperada')
                menssagError = wx.MessageDialog(self, 'Os valores digitados em algum dos campos não está da maneira esperada', 'EAU', wx.OK|wx.ICON_INFORMATION)
                aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                menssagError.ShowModal()
                menssagError.Destroy()
                d = -1

    #--------------------------------------------------
            self.identificadorCadastrados = bancodedados.ler_IDE()

            if d<0 or d>=0 or d == '':
                if e in self.identificadorCadastrados:
                    print('Ja existe esse identificador')
                    menssagError = wx.MessageDialog(self, 'Já existe um ensaio com esse identificador', 'EAU', wx.OK|wx.ICON_INFORMATION)
                    aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                    menssagError.ShowModal()
                    menssagError.Destroy()
                else:
                    self.Close(True)
                    con = TelaNovoEnsaio(a, b, c, d, e)
                    resultado = con.ShowModal()

            else:
                print('Algum dos campos esta digitado errado')
