# -*- coding: utf-8 -*-
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
          win.Show()

          '''StatusBar'''
          win.CreateStatusBar()
          win.SetStatusText('Novo Ensaio')

          win.FontTitle =wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
          win.FontCorpo =wx.Font(9 , wx.SWISS, wx.NORMAL, wx.NORMAL)
          win.title = wx.StaticText(panel, -1, 'Dados do Ensaio', (20,20), (460,-1), wx.ALIGN_CENTER)
          win.title.SetFont(win.FontTitle)
          win.texto01 = wx.StaticText(panel, -1, 'CELULA DE ADENSAMENTO:',(20,50), (460,-1), wx.ALIGN_LEFT)
          win.texto02 = wx.StaticText(panel, -1, 'Tipo de Anel',(240,60), (230,-1), wx.ALIGN_LEFT)
          win.tipoAnel = wx.ComboBox(panel, -1, 'Selecione um item da lista', (240,80), (230, -1), choices = ('Anel fixo', 'Anel flutuante'))
          win.texto03 = wx.StaticText(panel, -1, 'ANEL:',(20,110), (40,-1), wx.ALIGN_LEFT)
          win.alturaAnel = wx.TextCtrl(panel, -1, '', (370,130),(100,-1))
          win.texto04 = wx.StaticText(panel, -1, 'Altura (mm)',(297,135), (70,-1), wx.ALIGN_LEFT)
          win.diamtroInterno = wx.TextCtrl(panel, -1, '', (170,130),(100,-1))
          win.texto05 = wx.StaticText(panel, -1, 'Diâmetro Interno (mm)',(40,135), (125,-1), wx.ALIGN_LEFT)
          win.massaConjunto = wx.TextCtrl(panel, -1, '', (370,160),(100,-1))
          win.texto06 = wx.StaticText(panel, -1, 'Massa do Anel (g)',(267,165), (95,-1), wx.ALIGN_LEFT)
          win.massaConjunto = wx.TextCtrl(panel, -1, '', (370,190),(100,-1))
          win.texto07 = wx.StaticText(panel, -1, 'Massa do conjunto corpo de prova e anel de adensamento (g)',(35,195), (330,-1), wx.ALIGN_LEFT)
          win.texto08 = wx.StaticText(panel, -1, 'CORPO-DE-PROVA:',(20,230), (460,-1), wx.ALIGN_LEFT)
          self.check = wx.CheckBox(panel, -1, 'Altura do corpo de prova diferente da do anel', (210,240),(260,-1), wx.ALIGN_RIGHT)
          self.alturaCorpoProva = wx.TextCtrl(panel, -1, '', (370,260),(100,-1), wx.TE_READONLY)
          self.text = wx.StaticText(panel, -1, 'Altura do corpo de prova (mm)', (197,265),(170,-1), wx.ALIGN_LEFT)
          self.text.SetForegroundColour((119,118,114))
          win.Bind(wx.EVT_CHECKBOX, self.onCheck, self.check)


     def onCheck(self, event):
         win = wx.Frame(self, -1, 'EAU - Novo Ensaio', style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION)
         panel = wx.Panel(self)
         a = float(self.check.GetValue())

         if  a == 1:
             self.text.SetForegroundColour((0,0,0))
             self.text.Refresh()


         else:
             self.alturaCorpoProva.Destroy()
             wx.TextCtrl(panel, -1, '', (370,260),(100,-1), wx.TE_READONLY)
             self.text.SetForegroundColour((119,118,114))
             self.text.Refresh()


#----------------------------------------------------------------------
     def ajudaGUI(self, event):
          '''Dialogo ajuda'''
          message1 = ('Software EAU - Ensaio de Adensamento Unidimensional\n\n')
          message2 = ('Esse software foi desenvolvido para facilitar o mÃ©todo de ensaio da antiga MB-3336, hoje conhecida pela NBR 12007 - SOLO - ENSAIO DE ADENSAMENTO UNIDIMENSIONAL pela ABNT - AssociaÃ§Ã£o Brasileira de Normas TÃ©cnicas. Esta norma prescreve o mÃ©todo de determinaÃ§Ã£o das propriedades de adensamento do solo, caracterizadas pela velocidade e magnitude das deformaÃ§Ãµes, quando o solo Ã© lateralmente confinado e carregado de forma axial.')
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
