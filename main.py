'''Bibliotecas'''

import wx
import PySimpleGUI27

########################################################################

'''Tela Inicial'''
class Tela(wx.Frame):

#----------------------------------------------------------------------
     def __init__(self, *args, **kwargs):
          super(Tela, self).__init__(style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION, *args, **kwargs)

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
          self.button = wx.Button(panel, -1, 'Novo Ensaio')
          self.button.Centre()
          self.Bind(wx.EVT_BUTTON, self.NovoEnsaio, self.button)
          
          
#----------------------------------------------------------------------
     def NovoEnsaio(self, event):
          '''Tela Novo ensaio'''
          win = wx.Frame(self, -1, 'EAU - Novo Ensaio', style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION)

          panel = wx.Panel(win)
          win.SetSize((500,600))
          win.Centre()
          win.Show(True)

          '''StatusBar'''
          win.CreateStatusBar()
          win.SetStatusText('Novo Ensaio')
          
          FontTitle =wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
          FontCorpo =wx.Font(9 , wx.SWISS, wx.NORMAL, wx.NORMAL)
          title = wx.StaticText(panel, -1, 'Dados do Ensaio', (10,10), (480,-1), wx.ALIGN_CENTER)
          title.SetFont(FontTitle)

          texto01 = wx.StaticText(panel, -1, 'CELULA DE ADENSAMENTO:',(10,40), (480,-1), wx.LIGHT)


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
     def onExit(self, event):
          '''Opcao Sair'''
          self.Close(True)

#----------------------------------------------------------------------

'''Inicializacao do programa'''

def main():
     app = wx.App()
     Tela(None)
     app.MainLoop()

main()



########################################################################
