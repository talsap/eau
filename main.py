'''Bibliotecas'''

import wx
import PySimpleGUI27

########################################################################

'''Tela Inicial'''
class Tela(wx.Frame):

#----------------------------------------------------------------------
     def __init__(self, *args, **kwargs):
          wx.Frame.__init__(self, None, -1, 'EAU - Beta', size=(650,500), *args, **kwargs)

          self.panel = wx.Panel(self, wx.ID_ANY)
          self.basic_gui()
          self.Centre()

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
          self.button = wx.Button(self.panel, -1, 'Novo Ensaio')
          self.button.Centre()
          self.Bind(wx.EVT_BUTTON, self.NovoEnsaio, self.button)
          
          
#----------------------------------------------------------------------
     def NovoEnsaio(self, event):
          '''Tela Novo ensaio'''
          win = wx.Frame(self, -1, 'EAU - Novo Ensaio', size=(450,300))
          win.Centre()
          win.Show(True)

          


#----------------------------------------------------------------------
     def ajudaGUI(self, event):
          '''Dialogo ajuda'''
          message1 = ('Software EAU - Ensaio de Adensamento Unidimensional\n\n')
          message2 = ('Esse software foi desenvolvido para facilitar o método de ensaio da antiga MB-3336, hoje conhecida pela NBR 12007 - SOLO - ENSAIO DE ADENSAMENTO UNIDIMENSIONAL pela ABNT - Associação Brasileira de Normas Técnicas. Esta norma prescreve o método de determinação das propriedades de adensamento do solo, caracterizadas pela velocidade e magnitude das deformações, quando o solo é lateralmente confinado e carregado de forma axial.')
          dlg = wx.MessageDialog(self, message1 + message2, 'EAU', wx.OK|wx.ICON_INFORMATION)
          aboutPanel = wx.TextCtrl(dlg, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
          dlg.ShowModal()
          dlg.Destroy()
          
#----------------------------------------------------------------------
     def basic_gui(self):
          '''StatusBar'''
          self.CreateStatusBar()
          self.SetStatusText('Ensaio de Andesamento Unidimensional')

#----------------------------------------------------------------------
     def onExit(self, event):
          '''Opcao Sair'''
          self.Close(True)

#----------------------------------------------------------------------

'''Inicializacao do programa'''

app = wx.App()
frame = Tela()
frame.Show()
app.MainLoop()



########################################################################
