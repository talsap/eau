# -*- coding: utf-8 -*-

'''Bibliotecas'''

import wx
import bancodedados
import datetime
import wx.lib.mixins.listctrl  as  listmix

'''Classe da Lista editável'''
class EditableListCtrl(wx.ListCtrl, listmix.TextEditMixin):
    #--------------------------------------------------
        def __init__(self, parent, ID=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):
            wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
            listmix.TextEditMixin.__init__(self)

'''Tela De dialogo Se a coleta vai ser MANUAL ou AUTOMATICA'''
class ColetaStatusManual(wx.Dialog):

    def __init__(self, id, id_Estagio, *args, **kwargs):
        wx.Dialog.__init__(self, None, -1, 'EAU - Coletar Dado final Manualmente', style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        self.id = id
        self.id_Estagio = id_Estagio

        self.InitUI()
        self.SetSize((300, 630))
        self.Centre()
        self.SetTitle("EAU - Coleta Manual")

    def InitUI(self):
        id = self.id
        id_Estagio = self.id_Estagio
        num = ['1','2','3','4','5','6','7','8','9','10']
        rows = bancodedados.TabelaEstagio(id, id_Estagio)
        pnl = wx.Panel(self)

        self.FontTitle =wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
        self.title = wx.StaticText(self, -1, "Estágio " + str(self.id_Estagio), (20,20), (260,-1), wx.ALIGN_CENTER)
        self.title.SetFont(self.FontTitle)
        self.text00 = wx.StaticText(self, -1, "Quantos dados deseja adicionar?", (20,55), (200,-1), wx.ALIGN_RIGHT)
        self.ComboEstagios = wx.ComboBox(self, -1, num[0], (225,50),(50,-1), num)
        self.Bind(wx.EVT_COMBOBOX, self.EstagioVisualizacao, self.ComboEstagios)

        self.list_ctrl = wx.ListCtrl(self, size = (255,360), pos = (20,90), style =  wx.LC_REPORT | wx.BORDER_SUNKEN | wx.LC_HRULES | wx.LC_VRULES)
        self.list_ctrl.InsertColumn(0, "Tempo (s)", width=125)
        self.list_ctrl.InsertColumn(1, "Altura (mm)", width=130)

        index = 0
        for row in rows:
            self.list_ctrl.InsertItem(index, row[0])
            self.list_ctrl.SetItem(index, 1, row[1])
            index += 1
    #--------------------------------------------------
    def EstagioVisualizacao(self, event):
         pass


    def ColetarManual(self):
        id = self.id
        id_Estagio = self.id_Estagio
        print id, id_Estagio
