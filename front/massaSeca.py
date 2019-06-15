# -*- coding: utf-8 -*-

'''Bibliotecas'''

import wx
import bancodedados

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

'''Tela Cadastrar Cápsula'''
class massaSeca(wx.Dialog):

#----------------------------------------------------------------------
        def __init__(self, id, *args, **kwargs):
            wx.Dialog.__init__(self, None, -1, 'EAU', style = wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION)
            self.id = id
            self.panel = wx.Panel(self)
            self.SetSize((400,200))
            self.Centre()
            self.Show()

            capsulas = bancodedados.caps(id)
            self.FontTitle =wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
            self.title = wx.StaticText(self.panel, -1, 'ADICIONE O VALORES PARA MASSA SECA', (20,20), (370,-1), wx.ALIGN_CENTER)
            self.title.SetFont(self.FontTitle)
            self.text01 = wx.StaticText(self.panel, -1, 'Cápsulas', (95,64), (47,-1), wx.ALIGN_LEFT)
            self.cap01 = wx.TextCtrl(self.panel, -1, capsulas[0], (150,60), (70, -1), style = wx.TE_READONLY | wx.TE_RIGHT)
            self.cap02 = wx.TextCtrl(self.panel, -1, capsulas[1], (230,60), (70, -1), style = wx.TE_READONLY | wx.TE_RIGHT)
            self.cap03 = wx.TextCtrl(self.panel, -1, capsulas[2], (310,60), (70, -1), style = wx.TE_READONLY | wx.TE_RIGHT)
            self.text02 = wx.StaticText(self.panel, -1, 'Massa Seca (g)', (65,94), (80,-1), wx.ALIGN_LEFT)
            self.massaSeca01 = wx.TextCtrl(self.panel, -1, '', (150,90), (70, -1), wx.TE_RIGHT)
            self.massaSeca02 = wx.TextCtrl(self.panel, -1, '', (230,90), (70, -1), wx.TE_RIGHT)
            self.massaSeca03 = wx.TextCtrl(self.panel, -1, '', (310,90), (70, -1), wx.TE_RIGHT)
            self.depois = wx.Button(self.panel, -1, 'Preencher Depois', (20, 130), (175,-1), wx.ALIGN_LEFT)
            self.salvar = wx.Button(self.panel, -1, 'Salvar', (205, 130), (175,-1), wx.ALIGN_LEFT | wx.NO_DEFAULT)
            self.Bind(wx.EVT_BUTTON, self.salvarMassaS, self.salvar)
            self.Bind(wx.EVT_BUTTON, self.finsh, self.depois)


#----------------------------------------------------------------------
        def salvarMassaS(self, event):
            id = self.id
            m = self.massaSeca01.GetValue()
            m = format(m).replace(',','.')
            n = self.massaSeca02.GetValue()
            n = format(n).replace(',','.')
            o = self.massaSeca03.GetValue()
            o = format(o).replace(',','.')
            try:
                m = float(m)
                n = float(n)
                o = float(o)
            except ValueError:
                print('Os valores digitados nao e esperdo')
                menssagError = wx.MessageDialog(self, 'Os/ou valores digitados para massa seca não está da maneira esperada', 'EAU', wx.OK|wx.ICON_INFORMATION)
                aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                menssagError.ShowModal()
                menssagError.Destroy()
                m = -1
                n = -1
                o = -1

            if m>0 and n>0 and o>0:
                if m!= '' and n!= '' and o!= '':
                    bancodedados.UpdateMassaSeca(id, m, n, o)
                    self.Close(True)
                else:
                    print('Algum dos campos esta vazio')
            else:
                pass

#----------------------------------------------------------------------
        def finsh(self, event):
            self.Close(True)

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
