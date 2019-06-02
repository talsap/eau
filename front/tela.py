# -*- coding: utf-8 -*-

'''Bibliotecas'''

import wx
import bancodedados
import wx.lib.mixins.listctrl as listmix
from wx.lib.agw import ultimatelistctrl as ULC
from novo import TelaNovo
from Editar import Editar

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
'''Classe da Lista editável'''
class EditableListCtrl(ULC.UltimateListCtrl, listmix.ListCtrlAutoWidthMixin):

    #----------------------------------------------------------------------
        def __init__(self, parent, ID=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):
            ULC.UltimateListCtrl.__init__(self, parent, ID, pos, size, agwStyle = ULC.ULC_REPORT | ULC.ULC_HAS_VARIABLE_ROW_HEIGHT | ULC.ULC_HRULES | ULC.ULC_VRULES | ULC.ULC_NO_HIGHLIGHT)
            listmix.ListCtrlAutoWidthMixin.__init__(self)

##################################################################################################################################
'''Tela Inicial'''
class Tela(wx.Frame):

#---------------------------------------------------------------------------------------------------------------------------------
     def __init__(self, *args, **kwargs):
         super(Tela, self).__init__(title = 'EAU - Beta' ,style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION, *args, **kwargs)

         self.basic_gui()

     def basic_gui(self):
         self.panel = wx.Panel(self)

         self.SetSize((700,500))
         self.Centre()
         self.Show()

         '''StatusBar'''
         self.CreateStatusBar()
         self.SetStatusText('Ensaio de Andesamento Unidimensional')

         '''MenuBarra'''
         arquivoMenu = wx.Menu()
         ajudaMenu = wx.Menu()
         menuBar = wx.MenuBar()
         menuBar.Append(arquivoMenu, '&Arquivo')
         menuBar.Append(ajudaMenu, '&Ajuda')

         novoEnsaioMenuItem = arquivoMenu.Append(wx.NewId(),'Novo Ensaio\tCtrl+N', 'Novo Ensaio')
         exitMenuItem = arquivoMenu.Append(wx.NewId(), 'Sair\tCtrl+S','Sair')
         ajudaMenuItem = ajudaMenu.Append(wx.NewId(),'Ajuda\tCtrl+A','Ajuda')
         self.Bind(wx.EVT_MENU, self.NovoEnsaio, novoEnsaioMenuItem)
         self.Bind(wx.EVT_MENU, self.onExit, exitMenuItem)
         self.Bind(wx.EVT_MENU, self.ajudaGUI, ajudaMenuItem)
         self.SetMenuBar(menuBar)

         '''Botao Novo Ensaio'''
         self.button = wx.Button(self.panel, -1, '', (326, 60), (48,48))
         self.button.SetBitmap(wx.Bitmap('icons\icons-adicionar-48px.png'))
         self.Bind(wx.EVT_BUTTON, self.NovoEnsaio, self.button)

         '''Lista dos Ensaios'''
         self.list_ctrl = EditableListCtrl(self.panel, size=(655,250), pos=(20,160) )
         self.list_ctrl.InsertColumn(0, 'IDENTIFICADOR', wx.LIST_FORMAT_CENTRE)
         self.list_ctrl.InsertColumn(1, 'INICIO DO ENSAIO', wx.LIST_FORMAT_CENTRE, width=115)
         self.list_ctrl.InsertColumn(2, 'TERMINO DO ENSAIO', wx.LIST_FORMAT_CENTRE, width=135)
         self.list_ctrl.InsertColumn(3, 'ESTAGIOS', wx.LIST_FORMAT_CENTRE, width=70)
         self.list_ctrl.InsertColumn(4, 'EDT', wx.LIST_FORMAT_CENTRE, width=40)
         self.list_ctrl.InsertColumn(5, 'GRF', wx.LIST_FORMAT_CENTRE, width=40)
         self.list_ctrl.InsertColumn(6, 'PDF', wx.LIST_FORMAT_CENTRE, width=40)
         self.list_ctrl.InsertColumn(7, 'CSV', wx.LIST_FORMAT_CENTRE, width=40)
         self.list_ctrl.InsertColumn(8, 'DEL', wx.LIST_FORMAT_CENTRE, width=40)
         self.list_ctrl.setResizeColumn(0)

         lista = bancodedados.ListaVisualizacao()
         index = 0

         for key, row in lista:
             pos = self.list_ctrl.InsertStringItem(index, row[0])
             self.list_ctrl.SetStringItem(index, 1, row[1])
             self.list_ctrl.SetStringItem(index, 2, row[2])
             self.list_ctrl.SetStringItem(index, 3, row[3])
             buttonEDT = wx.Button(self.list_ctrl, id = key, label="")
             buttonGRF = wx.Button(self.list_ctrl, id = 4000+key, label="")
             buttonPDF = wx.Button(self.list_ctrl, id = 10000+key, label="")
             buttonCSV = wx.Button(self.list_ctrl, id = 15000+key, label="")
             buttonDEL = wx.Button(self.list_ctrl, id = 20000+key, label="")
             buttonEDT.SetBitmap(wx.Bitmap('icons\icons-editar-arquivo-24px.png'))
             buttonGRF.SetBitmap(wx.Bitmap('icons\icons-grafico-24px.png'))
             buttonPDF.SetBitmap(wx.Bitmap('icons\icons-exportar-pdf-24px.png'))
             buttonCSV.SetBitmap(wx.Bitmap('icons\icons-exportar-csv-24px.png'))
             buttonDEL.SetBitmap(wx.Bitmap('icons\icons-lixo-24px.png'))
             self.list_ctrl.SetItemWindow(pos, col=4, wnd=buttonEDT, expand=True)
             self.list_ctrl.SetItemWindow(pos, col=5, wnd=buttonGRF, expand=True)
             self.list_ctrl.SetItemWindow(pos, col=6, wnd=buttonPDF, expand=True)
             self.list_ctrl.SetItemWindow(pos, col=7, wnd=buttonCSV, expand=True)
             self.list_ctrl.SetItemWindow(pos, col=8, wnd=buttonDEL, expand=True)
             self.Bind(wx.EVT_BUTTON, self.Editar, buttonEDT)
             self.Bind(wx.EVT_BUTTON, self.Graficos, buttonGRF)
             self.Bind(wx.EVT_BUTTON, self.exportPDF, buttonPDF)
             self.Bind(wx.EVT_BUTTON, self.exportCSV, buttonCSV)
             self.Bind(wx.EVT_BUTTON, self.Deletar, buttonDEL)
             self.list_ctrl.SetItemData(index, key)
             index += 1

         self.Bind(wx.EVT_LIST_COL_DRAGGING, self.ColumAdapter, self.list_ctrl)
         self.Bind(wx.EVT_LIST_COL_RIGHT_CLICK, self.ColumAdapter2, self.list_ctrl)
         self.Bind(wx.EVT_LIST_COL_CLICK, self.ColumAdapter3, self.list_ctrl)
         self.vBox = wx.BoxSizer(wx.VERTICAL)
         self.vBox.Add ((- 1, 140))
         self.vBox.Add(self.list_ctrl, 1, wx.ALL | wx.EXPAND, 20)
         self.SetSizer(self.vBox)

#---------------------------------------------------------------------------------------------------------------------------------
     def Editar(self, event):
         id = event.GetId()
         dialogo = Editar(id)
         resultado = dialogo.ShowModal()

#---------------------------------------------------------------------------------------------------------------------------------
     def Graficos(self, event):
         id = event.GetId()
         id = id - 4000
         print(id)
         print('Graficos')

#---------------------------------------------------------------------------------------------------------------------------------
     def exportPDF(self, event):
         id = event.GetId()
         id = id - 10000
         print(id)
         print('PDF')

#---------------------------------------------------------------------------------------------------------------------------------
     def exportCSV(self, event):
         id = event.GetId()
         id = id - 15000
         print(id)
         print('CSV')

#---------------------------------------------------------------------------------------------------------------------------------
     def Deletar(self, event):
         id = event.GetId()
         id = id - 20000

         '''Diálogo se deseja realmente excluir o Ensaio'''
         dlg = wx.MessageDialog(None, 'Deseja mesmo excluir esse Ensaio?', 'EAU', wx.YES_NO | wx .CENTRE| wx.NO_DEFAULT )
         result = dlg.ShowModal()

         if result == wx.ID_YES:
             bancodedados.delete(id)
             dlg.Destroy()
         else:
             dlg.Destroy()

         self.list_ctrl.DeleteAllItems()
         lista = bancodedados.ListaVisualizacao()
         index = 0

         for key, row in lista:
                pos = self.list_ctrl.InsertStringItem(index, row[0])
                self.list_ctrl.SetStringItem(index, 1, row[1])
                self.list_ctrl.SetStringItem(index, 2, row[2])
                self.list_ctrl.SetStringItem(index, 3, row[3])
                buttonEDT = wx.Button(self.list_ctrl, id = key, label="")
                buttonGRF = wx.Button(self.list_ctrl, id = 4000+key, label="")
                buttonPDF = wx.Button(self.list_ctrl, id = 10000+key, label="")
                buttonCSV = wx.Button(self.list_ctrl, id = 15000+key, label="")
                buttonDEL = wx.Button(self.list_ctrl, id = 20000+key, label="")
                buttonEDT.SetBitmap(wx.Bitmap('icons\icons-editar-arquivo-24px.png'))
                buttonGRF.SetBitmap(wx.Bitmap('icons\icons-grafico-24px.png'))
                buttonPDF.SetBitmap(wx.Bitmap('icons\icons-exportar-pdf-24px.png'))
                buttonCSV.SetBitmap(wx.Bitmap('icons\icons-exportar-csv-24px.png'))
                buttonDEL.SetBitmap(wx.Bitmap('icons\icons-lixo-24px.png'))
                self.list_ctrl.SetItemWindow(pos, col=4, wnd=buttonEDT, expand=True)
                self.list_ctrl.SetItemWindow(pos, col=5, wnd=buttonGRF, expand=True)
                self.list_ctrl.SetItemWindow(pos, col=6, wnd=buttonPDF, expand=True)
                self.list_ctrl.SetItemWindow(pos, col=7, wnd=buttonCSV, expand=True)
                self.list_ctrl.SetItemWindow(pos, col=8, wnd=buttonDEL, expand=True)
                self.Bind(wx.EVT_BUTTON, self.Editar, buttonEDT)
                self.Bind(wx.EVT_BUTTON, self.Graficos, buttonGRF)
                self.Bind(wx.EVT_BUTTON, self.exportPDF, buttonPDF)
                self.Bind(wx.EVT_BUTTON, self.exportCSV, buttonCSV)
                self.Bind(wx.EVT_BUTTON, self.Deletar, buttonDEL)
                self.list_ctrl.SetItemData(index, key)
                index += 1

#---------------------------------------------------------------------------------------------------------------------------------
     def NovoEnsaio(self, event):
         quant = bancodedados.quant_ensaios_deletados()
         valor_Logico = bancodedados.ler_quant_ensaios() - 1 - quant
         dialogo = TelaNovo()
         resultado = dialogo.ShowModal()

         lista = bancodedados.ListaVisualizacao()
         index = bancodedados.ler_quant_ensaios() - 1 - quant

         '''For apenas para definir os key's'''
         for key, row in lista:
             pass

         if valor_Logico == index:
             pass

         else:
             pos = self.list_ctrl.InsertStringItem(index, lista[index][1][0])
             self.list_ctrl.SetStringItem(index, 1, lista[index][1][1])
             self.list_ctrl.SetStringItem(index, 2, lista[index][1][2])
             self.list_ctrl.SetStringItem(index, 3, lista[index][1][3])
             buttonEDT = wx.Button(self.list_ctrl, id = key, label="")
             buttonGRF = wx.Button(self.list_ctrl, id = 4000+key, label="")
             buttonPDF = wx.Button(self.list_ctrl, id = 10000+key, label="")
             buttonCSV = wx.Button(self.list_ctrl, id = 15000+key, label="")
             buttonDEL = wx.Button(self.list_ctrl, id = 20000+key, label="")
             buttonEDT.SetBitmap(wx.Bitmap('icons\icons-editar-arquivo-24px.png'))
             buttonGRF.SetBitmap(wx.Bitmap('icons\icons-grafico-24px.png'))
             buttonPDF.SetBitmap(wx.Bitmap('icons\icons-exportar-pdf-24px.png'))
             buttonCSV.SetBitmap(wx.Bitmap('icons\icons-exportar-csv-24px.png'))
             buttonDEL.SetBitmap(wx.Bitmap('icons\icons-lixo-24px.png'))
             self.list_ctrl.SetItemWindow(pos, col=4, wnd=buttonEDT, expand=True)
             self.list_ctrl.SetItemWindow(pos, col=5, wnd=buttonGRF, expand=True)
             self.list_ctrl.SetItemWindow(pos, col=6, wnd=buttonPDF, expand=True)
             self.list_ctrl.SetItemWindow(pos, col=7, wnd=buttonCSV, expand=True)
             self.list_ctrl.SetItemWindow(pos, col=8, wnd=buttonDEL, expand=True)
             self.Bind(wx.EVT_BUTTON, self.Editar, buttonEDT)
             self.Bind(wx.EVT_BUTTON, self.Graficos, buttonGRF)
             self.Bind(wx.EVT_BUTTON, self.exportPDF, buttonPDF)
             self.Bind(wx.EVT_BUTTON, self.exportCSV, buttonCSV)
             self.Bind(wx.EVT_BUTTON, self.Deletar, buttonDEL)
             self.list_ctrl.SetItemData(index, key)
             self.list_ctrl.Update()
             valor_Logico = valor_Logico + 1

#---------------------------------------------------------------------------------------------------------------------------------
     def ajudaGUI(self, event):
          '''Dialogo ajuda'''
          message1 = ('Software EAU - Ensaio de Adensamento Unidimensional\n\n')
          message2 = ('Esse software foi desenvolvido para facilitar o método de ensaio da antiga MB-3336, hoje conhecida pela NBR 12007 - SOLO - ENSAIO DE ADENSAMENTO UNIDIMENSIONAL pela ABNT - Associacão Brasileira de Normas Técnicas. Esta norma prescreve o método de determinação das propriedades de adensamento do solo, caracterizadas pela velocidade e magnitude das deformacões, quando o solo é lateralmente confinado e carregado de forma axial.')
          dlg = wx.MessageDialog(self, message1 + message2, 'EAU', wx.OK|wx.ICON_INFORMATION)
          aboutPanel = wx.TextCtrl(dlg, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
          dlg.ShowModal()
          dlg.Destroy()

#---------------------------------------------------------------------------------------------------------------------------------
     def ColumAdapter(self, event):
          '''Ajusta os tamanhos das colunas ao arrastar'''
          self.list_ctrl.SetColumnWidth(1, width=115)
          self.list_ctrl.SetColumnWidth(2, width=135)
          self.list_ctrl.SetColumnWidth(3, width=70)
          self.list_ctrl.SetColumnWidth(4, width=40)
          self.list_ctrl.SetColumnWidth(5, width=40)
          self.list_ctrl.SetColumnWidth(6, width=40)
          self.list_ctrl.SetColumnWidth(7, width=40)
          self.list_ctrl.SetColumnWidth(8, width=40)
          self.list_ctrl.setResizeColumn(0)

#---------------------------------------------------------------------------------------------------------------------------------
     def ColumAdapter2(self, event):
          '''Ajusta os tamanhos das colunas ao clicar com botão esquerdo sobre a coluna'''
          self.list_ctrl.SetColumnWidth(0, width=115)
          self.list_ctrl.SetColumnWidth(1, width=115)
          self.list_ctrl.SetColumnWidth(2, width=135)
          self.list_ctrl.SetColumnWidth(3, width=70)
          self.list_ctrl.SetColumnWidth(4, width=40)
          self.list_ctrl.SetColumnWidth(5, width=40)
          self.list_ctrl.SetColumnWidth(6, width=40)
          self.list_ctrl.SetColumnWidth(7, width=40)
          self.list_ctrl.SetColumnWidth(8, width=40)
          self.list_ctrl.setResizeColumn(0)

#---------------------------------------------------------------------------------------------------------------------------------
     def ColumAdapter3(self, event):
          '''Ajusta os tamanhos das colunas ao clicar com o botão direito sobre a coluna'''
          self.list_ctrl.SetColumnWidth(0, width=115)
          self.list_ctrl.SetColumnWidth(1, width=115)
          self.list_ctrl.SetColumnWidth(2, width=135)
          self.list_ctrl.SetColumnWidth(3, width=70)
          self.list_ctrl.SetColumnWidth(4, width=40)
          self.list_ctrl.SetColumnWidth(5, width=40)
          self.list_ctrl.SetColumnWidth(6, width=40)
          self.list_ctrl.SetColumnWidth(7, width=40)
          self.list_ctrl.SetColumnWidth(8, width=40)
          self.list_ctrl.setResizeColumn(0)

#---------------------------------------------------------------------------------------------------------------------------------
     def onExit(self, event):
          '''Opcao Sair'''
          self.Close(True)

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
