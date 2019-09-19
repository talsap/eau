# -*- coding: utf-8 -*-

'''Bibliotecas'''

import wx
import bancodedados
import wx.lib.mixins.listctrl as listmix
from front.cadastrarcapsula2 import cadCapsula2
from front.editarCapsula import edtCapsula
from wx.lib.agw import ultimatelistctrl as ULC

'''Classe da Lista editável'''
class EditableListCtrl(ULC.UltimateListCtrl, listmix.ListCtrlAutoWidthMixin):
    #----------------------------------------------------------------------
        def __init__(self, parent, ID=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):
            ULC.UltimateListCtrl.__init__(self, parent, ID, pos, size, agwStyle = ULC.ULC_REPORT | ULC.ULC_HAS_VARIABLE_ROW_HEIGHT | ULC.ULC_HRULES | ULC.ULC_VRULES | ULC.ULC_NO_HIGHLIGHT)

        def UpdateListCtrl(self):
            self.DeleteAllItems()
            lista = bancodedados.ListaVisualizacaoCap()
            index = 0

            for key, row in lista:
                   pos = self.InsertStringItem(index, row[0])
                   self.SetStringItem(index, 1, row[1])
                   buttonEDT = wx.Button(self, id = key, label="")
                   buttonDEL = wx.Button(self, id = 15000+key, label="")
                   buttonEDT.SetBitmap(wx.Bitmap('icons\icons-editar-arquivo-24px.png'))
                   buttonDEL.SetBitmap(wx.Bitmap('icons\icons-lixo-24px.png'))
                   self.SetItemWindow(pos, col=2, wnd=buttonEDT, expand=True)
                   self.SetItemWindow(pos, col=3, wnd=buttonDEL, expand=True)
                   self.SetItemData(index, key)
                   index += 1

            if len(lista)>=13:
               self.SetColumnWidth(0, width=105)
               self.SetColumnWidth(1, width=110)
               self.SetColumnWidth(2, width=40)
               self.SetColumnWidth(3, width=40)

            else:
               self.SetColumnWidth(0, width=115)
               self.SetColumnWidth(1, width=115)
               self.SetColumnWidth(2, width=40)
               self.SetColumnWidth(3, width=40)

'''Tela Capsulas'''
class Cap(wx.Dialog):
    #--------------------------------------------------
        def __init__(self, *args, **kwargs):
            wx.Dialog.__init__(self, None, -1, 'EAU - Cápsulas', style = wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION)

            self.panel = wx.Panel(self)
            self.SetSize((360,520))
            self.Centre()
            self.Show()

            self.CadastrarCapsulaButton = wx.Button(self.panel, -1, '', (170,20),(30, 30))
            self.CadastrarCapsulaButton.SetBitmap(wx.Bitmap('icons\icons-adicionar-48px.png'))
            self.Bind(wx.EVT_BUTTON, self.CadastrarCapsula, self.CadastrarCapsulaButton)

            lista = bancodedados.ListaVisualizacaoCap()

            '''Lista das Capsulas'''
            self.list_ctrl = EditableListCtrl(self.panel, size=(315,395), pos=(20,75))
            if len(lista)>=13:
                self.list_ctrl.InsertColumn(0, 'CÁPSULA', wx.LIST_FORMAT_CENTRE, width=105)
                self.list_ctrl.InsertColumn(1, 'MASSA (g)', wx.LIST_FORMAT_CENTRE, width=110)
                self.list_ctrl.InsertColumn(2, 'EDT', wx.LIST_FORMAT_CENTRE, width=40)
                self.list_ctrl.InsertColumn(3, 'DEL', wx.LIST_FORMAT_CENTRE, width=40)
            else:
                self.list_ctrl.InsertColumn(0, 'CÁPSULA', wx.LIST_FORMAT_CENTRE, width=115)
                self.list_ctrl.InsertColumn(1, 'MASSA (g)', wx.LIST_FORMAT_CENTRE, width=115)
                self.list_ctrl.InsertColumn(2, 'EDT', wx.LIST_FORMAT_CENTRE, width=40)
                self.list_ctrl.InsertColumn(3, 'DEL', wx.LIST_FORMAT_CENTRE, width=40)

            index = 0

            for key, row in lista:
                pos = self.list_ctrl.InsertStringItem(index, row[0])
                self.list_ctrl.SetStringItem(index, 1, row[1])
                buttonEDT = wx.Button(self.list_ctrl, id = key, label="")
                buttonDEL = wx.Button(self.list_ctrl, id = 15000+key, label="")
                buttonEDT.SetBitmap(wx.Bitmap('icons\icons-editar-arquivo-24px.png'))
                buttonDEL.SetBitmap(wx.Bitmap('icons\icons-lixo-24px.png'))
                self.list_ctrl.SetItemWindow(pos, col=2, wnd=buttonEDT, expand=True)
                self.list_ctrl.SetItemWindow(pos, col=3, wnd=buttonDEL, expand=True)
                self.Bind(wx.EVT_BUTTON, self.Editar, buttonEDT)
                self.Bind(wx.EVT_BUTTON, self.Deletar, buttonDEL)
                self.list_ctrl.SetItemData(index, key)
                index += 1

            self.Bind(wx.EVT_LIST_COL_DRAGGING, self.ColumAdapter, self.list_ctrl)
            self.Bind(wx.EVT_LIST_COL_RIGHT_CLICK, self.ColumAdapter2, self.list_ctrl)
            self.Bind(wx.EVT_LIST_COL_CLICK, self.ColumAdapter3, self.list_ctrl)
            self.vBox = wx.BoxSizer(wx.VERTICAL)
            self.vBox.Add ((-1, 100))
            self.vBox.Add(self.list_ctrl, 1, wx.ALL | wx.EXPAND, 20)
            self.SetSizer(self.vBox)
            self.list_ctrl.UpdateListCtrl()

    #--------------------------------------------------
        def CadastrarCapsula(self, event):
            dialogo = cadCapsula2()
            resultado = dialogo.ShowModal()

            index = 0
            self.list_ctrl.DeleteAllItems()
            lista = bancodedados.ListaVisualizacaoCap()

            for key, row in lista:
                pos = self.list_ctrl.InsertStringItem(index, row[0])
                self.list_ctrl.SetStringItem(index, 1, row[1])
                buttonEDT = wx.Button(self.list_ctrl, id = key, label="")
                buttonDEL = wx.Button(self.list_ctrl, id = 15000+key, label="")
                buttonEDT.SetBitmap(wx.Bitmap('icons\icons-editar-arquivo-24px.png'))
                buttonDEL.SetBitmap(wx.Bitmap('icons\icons-lixo-24px.png'))
                self.list_ctrl.SetItemWindow(pos, col=2, wnd=buttonEDT, expand=True)
                self.list_ctrl.SetItemWindow(pos, col=3, wnd=buttonDEL, expand=True)
                self.Bind(wx.EVT_BUTTON, self.Editar, buttonEDT)
                self.Bind(wx.EVT_BUTTON, self.Deletar, buttonDEL)
                self.list_ctrl.SetItemData(index, key)
                index += 1

            lista = bancodedados.ListaVisualizacaoCap()

            if len(lista)>=13:
                self.list_ctrl.SetColumnWidth(0, width=105)
                self.list_ctrl.SetColumnWidth(1, width=110)
                self.list_ctrl.SetColumnWidth(2, width=40)
                self.list_ctrl.SetColumnWidth(3, width=40)
            else:
                self.list_ctrl.SetColumnWidth(0, width=115)
                self.list_ctrl.SetColumnWidth(1, width=115)
                self.list_ctrl.SetColumnWidth(2, width=40)
                self.list_ctrl.SetColumnWidth(3, width=40)

    #--------------------------------------------------
        def Editar(self, event):
            id = event.GetId()
            dialogo = edtCapsula(id)
            resultado = dialogo.ShowModal()
            self.list_ctrl.UpdateListCtrl()

    #--------------------------------------------------
        def Deletar(self, event):
            id = event.GetId()
            id = id - 15000

            '''Diálogo se deseja realmente excluir a Cápsula'''
            dlg = wx.MessageDialog(None, 'Deseja mesmo excluir essa Cápsula?', 'EAU', wx.YES_NO | wx.CENTRE| wx.NO_DEFAULT )
            result = dlg.ShowModal()

            if result == wx.ID_YES:
                bancodedados.deleteCap(id)
                dlg.Destroy()
                self.list_ctrl.UpdateListCtrl()
            else:
                dlg.Destroy()

    #--------------------------------------------------
        def ColumAdapter(self, event):
             lista = bancodedados.ListaVisualizacaoCap()
             '''Ajusta os tamanhos das colunas ao arrastar'''
             if len(lista) >=13:
                self.list_ctrl.SetColumnWidth(0, width=105)
                self.list_ctrl.SetColumnWidth(1, width=110)
                self.list_ctrl.SetColumnWidth(2, width=40)
                self.list_ctrl.SetColumnWidth(3, width=40)
             else:
                self.list_ctrl.SetColumnWidth(0, width=115)
                self.list_ctrl.SetColumnWidth(1, width=115)
                self.list_ctrl.SetColumnWidth(2, width=40)
                self.list_ctrl.SetColumnWidth(3, width=40)

    #--------------------------------------------------
        def ColumAdapter2(self, event):
            lista = bancodedados.ListaVisualizacaoCap()
            '''Ajusta os tamanhos das colunas ao clicar com botão esquerdo sobre a coluna'''
            if len(lista) >=13:
                self.list_ctrl.SetColumnWidth(0, width=105)
                self.list_ctrl.SetColumnWidth(1, width=110)
                self.list_ctrl.SetColumnWidth(2, width=40)
                self.list_ctrl.SetColumnWidth(3, width=40)
            else:
                self.list_ctrl.SetColumnWidth(0, width=115)
                self.list_ctrl.SetColumnWidth(1, width=115)
                self.list_ctrl.SetColumnWidth(2, width=40)
                self.list_ctrl.SetColumnWidth(3, width=40)

    #--------------------------------------------------
        def ColumAdapter3(self, event):
            lista = bancodedados.ListaVisualizacaoCap()
            '''Ajusta os tamanhos das colunas ao clicar com o botão direito sobre a coluna'''
            if len(lista) >=13:
                self.list_ctrl.SetColumnWidth(0, width=105)
                self.list_ctrl.SetColumnWidth(1, width=110)
                self.list_ctrl.SetColumnWidth(2, width=40)
                self.list_ctrl.SetColumnWidth(3, width=40)
            else:
                self.list_ctrl.SetColumnWidth(0, width=115)
                self.list_ctrl.SetColumnWidth(1, width=115)
                self.list_ctrl.SetColumnWidth(2, width=40)
                self.list_ctrl.SetColumnWidth(3, width=40)
