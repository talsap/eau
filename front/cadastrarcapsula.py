# -*- coding: utf-8 -*-

'''Bibliotecas'''

import wx
import bancodedados
import novoensaio

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

'''Tela Cadastrar Cápsula'''
class cadCapsula(wx.Dialog):

#----------------------------------------------------------------------
        def __init__(self, *args, **kwargs):
            wx.Dialog.__init__(self, None, -1, 'EAU')

            self.panel = wx.Panel(self)
            self.SetSize((200,175))
            self.Centre()
            self.Show()

            self.nomeCap = wx.TextCtrl(self.panel, -1, '', (60,20), (120,-1), wx.TE_RIGHT)
            self.text12 = wx.StaticText(self.panel, -1, 'Nome:', (15,25), (35,-1), wx.ALIGN_LEFT)
            self.massaCap = wx.TextCtrl(self.panel, -1, '', (105,60), (75,-1), wx.TE_RIGHT)
            self.text12 = wx.StaticText(self.panel, -1, 'Massa (g):', (45,65), (60,-1), wx.ALIGN_LEFT)
            self.Cadastrar = wx.Button(self.panel, -1, 'Cadastrar', pos = (60, 100))
            self.Bind(wx.EVT_BUTTON, self.CadCapOk, self.Cadastrar)

#----------------------------------------------------------------------
        def CadCapOk(self, event):
            a = self.nomeCap.GetValue()
            b = self.massaCap.GetValue()
            b = format(b).replace(',','.')
            try:
                b = float(b)
            except ValueError:
                print('O valor digitado nao e o esperado')
                menssagError = wx.MessageDialog(self, 'Preencha os campos corretamente', 'EAU', wx.OK|wx.ICON_INFORMATION)
                aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                menssagError.ShowModal()
                menssagError.Destroy()
                b = -1

            self.capCadastradas = bancodedados.ler_cap()

            if a!= '' and  b!= '' and b>0:
                if a in self.capCadastradas:
                    print('Ja existe essa capsula')
                    menssagError = wx.MessageDialog(self, 'Já existe uma capsula com esse nome', 'EAU', wx.OK|wx.ICON_INFORMATION)
                    aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                    menssagError.ShowModal()
                    menssagError.Destroy()
                else:
                    bancodedados.data_entry_cap(a,b)
                    self.Close(True)

            else:
                print('O valor digitado nao e o esperado')

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
