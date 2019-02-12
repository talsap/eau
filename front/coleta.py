# -*- coding: utf-8 -*-

'''Bibliotecas'''

import wx
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
            self.SetSize((500,500))
            self.Centre()
            self.Show()

            self.numEstagios = str(bancodedados.ler_quant_estagios())
            self.FontTitle = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
            self.title = wx.StaticText(self.panel, -1, 'Estágio ' + self.numEstagios, (20,20), (460,-1), wx.ALIGN_CENTER)
            self.title.SetFont(self.FontTitle)

            self.massaAplicada = wx.TextCtrl(self.panel, -1, '', (370,60),(100,-1), wx.TE_RIGHT)
            self.Bind(wx.EVT_TEXT, self.textDinamic01, self.massaAplicada)
            self.texto01 = wx.StaticText(self.panel, -1, 'Massa Aplicada (kg)',(258,65), (109,-1), wx.ALIGN_LEFT)
            self.pressaoAplicada = wx.TextCtrl(self.panel, -1, '', (370,90),(100,-1), wx.TE_RIGHT)
            self.Bind(wx.EVT_TEXT, self.textDinamic02, self.pressaoAplicada)
            self.texto01 = wx.StaticText(self.panel, -1, 'Pressão Aplicada (kPa)',(245,95), (119,-1), wx.ALIGN_LEFT)
            self.Refresh()
            self.Update()

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

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
