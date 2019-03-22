# -*- coding: utf-8 -*-

'''Bibliotecas'''

import wx
import bancodedados
import wx.lib.mixins.listctrl  as  listmix

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

class EditableListCtrl(wx.ListCtrl, listmix.TextEditMixin):

    #----------------------------------------------------------------------
        def __init__(self, parent, ID=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):
            wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
            listmix.TextEditMixin.__init__(self)

########################################################################
'''Tela Cadastrar Cápsula'''
class AddDados(wx.Dialog):

#----------------------------------------------------------------------
        def __init__(self, *args, **kwargs):
            wx.Dialog.__init__(self, None, -1, 'EAU - Beta')

            self.panel = wx.Panel(self)
            self.SetSize((240,390))
            self.Centre()
            self.Show()

            rows = [("0", "12.215"),
                    ("8", "11.930"),
                    ("15", "11.922"),
                    ("30", "11.918"),
                    ("60", "11.912"),
                    ("240", "11.904"),
                    ("480", "11.900"),
                    ("900", "11.895"),
                    ("1800", "11.889"),
                    ("3600", "11.883"),
                    ("7200", "11.879"),
                    ("14400", "11.873"),
                    ("28800", "11.869"),
                    ("86400", "11.859")
                    ]

            self.list_ctrl = EditableListCtrl(self.panel, size = (195,294), pos = (20,20), style = wx.LC_REPORT | wx.BORDER_SUNKEN | wx.LC_HRULES | wx.LC_VRULES)

            self.list_ctrl.InsertColumn(0, "Tempo (s)", width=80)
            self.list_ctrl.InsertColumn(1, "Altura (mm)", width=110)

            index = 0

            for row in rows:
                self.list_ctrl.InsertItem(index, row[0])
                self.list_ctrl.SetItem(index, 1, row[1])
                index += 1

            self.confirmar = wx.Button(self.panel, -1, 'Coletar',(70, 323), (100,-1), wx.ALIGN_LEFT)
            self.Bind(wx.EVT_BUTTON, self.Confirmar, self.confirmar)
#----------------------------------------------------------------------
        def Confirmar(self, event):
            indice = 0
            while True:
                tempo = self.list_ctrl.GetItemText(indice, 0)
                altura = self.list_ctrl.GetItemText(indice, 1)
                tempo = float(format(tempo).replace(',','.'))
                altura = float(format(altura).replace(',','.'))
                bancodedados.InserirDados(tempo, altura)
                indice = indice + 1
                if indice == 14:
                    break

            self.Close(True)
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
