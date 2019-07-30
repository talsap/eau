# -*- coding: utf-8 -*-

'''Bibliotecas'''

import wx
import bancodedados


##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
'''Class Export CSV'''
class Csv(wx.Dialog):

#---------------------------------------------------------------------------------------------------------------------------------
     def __init__(self, id, *args, **kwargs):
        wx.Dialog.__init__(self, None, -1, 'EAU - CSV')
        id = 4
        self.id = 4
        frame = self.basic_gui()

     def basic_gui(self):
        id = self.id
        massaEspGra = bancodedados.massaEspecificaGraos(id)
        massaS = bancodedados.mSeca(id)
        b = bancodedados.ListStatursEstagio(id)
        condition = 0
        c = 1

        if c in b:
            condition = 0

        if massaEspGra == '' or massaS[0] == '' or massaS[1] == '' or massaS[2] == '' or massaEspGra == 0  or massaS[0] == 0 or massaS[1] == 0 or massaS[2] == 0 or condition == 0:
            menssagError = wx.MessageDialog(self, 'NADA CALCULADO AINDA!\n\n Seu arquivo .CSV ainda não pode ser exportado!\n Alguns dados precisam ser coletados.', 'EAU', wx.OK|wx.ICON_INFORMATION)
            aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
            menssagError.ShowModal()
            menssagError.Destroy()
            self.Destroy()

        else:
            pass
