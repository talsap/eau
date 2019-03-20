# -*- coding: utf-8 -*-

'''Bibliotecas'''

import wx
import bancodedados
from novoensaio import TelaNovoEnsaio

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

'''Tela Inicial'''
class Tela(wx.Frame):

#---------------------------------------------------------------------------------------------------------------------------------
     def __init__(self, *args, **kwargs):
          super(Tela, self).__init__(title = 'EAU - Beta' ,style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION, *args, **kwargs)

          self.basic_gui()

     def basic_gui(self):
          panel = wx.Panel(self)

          self.SetSize((650,500))
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

          novoEnsaioMenuItem = arquivoMenu.Append(wx.NewId(),'Novo Ensaio', 'Novo Ensaio')
          exitMenuItem = arquivoMenu.Append(wx.NewId(), 'Sair','Sair')
          ajudaMenuItem = ajudaMenu.Append(wx.NewId(),'Ajuda','Ajuda')

          self.Bind(wx.EVT_MENU, self.NovoEnsaio, novoEnsaioMenuItem)
          self.Bind(wx.EVT_MENU, self.onExit, exitMenuItem)
          self.Bind(wx.EVT_MENU, self.ajudaGUI, ajudaMenuItem)
          self.SetMenuBar(menuBar)

          '''Botao Novo Ensaio'''
          self.button = wx.Button(panel, -1, 'Novo Ensaio', (275, 60), (100,-1))
          self.Bind(wx.EVT_BUTTON, self.NovoEnsaio, self.button)


          '''Lista dos Ensaios'''
          self.list_ctrl = wx.ListCtrl(panel, size=(605,250), pos=(20,160), style=wx.LC_REPORT | wx.BORDER_SUNKEN | wx.LC_HRULES | wx.LC_VRULES)

          self.list_ctrl.InsertColumn(0, 'DATA DO ENSAIO', wx.LIST_FORMAT_LEFT, width=110)


#---------------------------------------------------------------------------------------------------------------------------------
     def NovoEnsaio(self, event):
         dialogo = TelaNovoEnsaio()
         resultado = dialogo.ShowModal()

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
     def onExit(self, event):
          '''Opcao Sair'''
          self.Close(True)

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
