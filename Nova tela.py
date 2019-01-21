# -*- coding: utf-8 -*-
'''Bibliotecas'''

import wx

########################################################################
'''Tela Novo Ensaio'''
class NovoEnsaio(wx.Frame):

#----------------------------------------------------------------------
        def __init__(self, parent, *args, **kwargs):
            super(NovoEnsaio, self).__init__(parent, style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION, *args, **kwargs)

            self.basic_gui()

        def basic_gui(self):
            '''Tela Novo ensaio'''
            self.panel = wx.Panel(self)

            self.SetSize((500,600))
            self.Centre()
            self.Show()

            '''StatusBar'''
            self.CreateStatusBar()
            self.SetStatusText('Novo Ensaio')

            FontTitle = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
            FontCorpo = wx.Font(9 , wx.SWISS, wx.NORMAL, wx.NORMAL)
            title = wx.StaticText(self.panel, -1, 'Dados do Ensaio', (20,20), (460,-1), wx.ALIGN_CENTER)
            title.SetFont(FontTitle)

            self.FontTitle =wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
            self.FontCorpo =wx.Font(9 , wx.SWISS, wx.NORMAL, wx.NORMAL)
            self.title = wx.StaticText(self.panel, -1, 'Dados do Ensaio', (20,20), (460,-1), wx.ALIGN_CENTER)
            self.title.SetFont(self.FontTitle)
            self.texto01 = wx.StaticText(self.panel, -1, 'CELULA DE ADENSAMENTO:',(20,50), (460,-1), wx.ALIGN_LEFT)
            self.texto02 = wx.StaticText(self.panel, -1, 'Tipo de Anel',(240,60), (230,-1), wx.ALIGN_LEFT)
            self.tipoAnel = wx.ComboBox(self.panel, -1, 'Selecione um item da lista', (240,80), (230, -1), choices = ('Anel fixo', 'Anel flutuante'))
            self.texto03 = wx.StaticText(self.panel, -1, 'ANEL:',(20,110), (40,-1), wx.ALIGN_LEFT)
            self.diamtroInterno = wx.TextCtrl(self.panel, -1, '', (170,130),(100,-1))
            self.texto05 = wx.StaticText(self.panel, -1, 'Diâmetro Interno (mm)',(40,135), (125,-1), wx.ALIGN_LEFT)
            self.alturaAnel = wx.TextCtrl(self.panel, -1, '', (370,130),(100,-1))
            self.texto04 = wx.StaticText(self.panel, -1, 'Altura (mm)',(297,135), (70,-1), wx.ALIGN_LEFT)
            self.massaConjunto = wx.TextCtrl(self.panel, -1, '', (370,160),(100,-1))
            self.texto06 = wx.StaticText(self.panel, -1, 'Massa do Anel (g)',(267,165), (95,-1), wx.ALIGN_LEFT)
            self.massaConjunto = wx.TextCtrl(self.panel, -1, '', (370,190),(100,-1))
            self.texto07 = wx.StaticText(self.panel, -1, 'Massa do conjunto corpo de prova e anel de adensamento (g)',(35,195), (330,-1), wx.ALIGN_LEFT)
            self.texto08 = wx.StaticText(self.panel, -1, 'CORPO-DE-PROVA:',(20,230), (460,-1), wx.ALIGN_LEFT)
            self.check = wx.CheckBox(self.panel, -1, 'Altura do corpo de prova diferente da do anel', (210,240),(260,-1), wx.ALIGN_RIGHT)
            self.alturaCorpoProva = wx.TextCtrl(self.panel, -1, '', (370,260),(100,-1), style = wx.TE_READONLY)
            self.text09 = wx.StaticText(self.panel, -1, 'Altura do corpo de prova (mm)', (197,265),(170,-1), wx.ALIGN_LEFT)
            self.text09.SetForegroundColour((119,118,114))
            self.Bind(wx.EVT_CHECKBOX, self.onCheck, self.check)
            self.text10 = wx.StaticText(self.panel, -1, 'Massa específica dos grãos de solo (g/cm³)', (135,295), (230,-1), wx.ALIGN_LEFT)
            self.massaEspeciciaGraosSolo = wx.TextCtrl(self.panel, -1, '', (370,290),(100,-1))
            self.text11 = wx.StaticText(self.panel, -1, 'TEOR DE UMIDADE INICIAL:', (20,330), (150,-1), wx.ALIGN_LEFT)
            self.CadastrarCapsula = wx.Button(self.panel, -1, 'Cadastrar Cápsula', pos = (20, 350))





#----------------------------------------------------------------------
        def onCheck(self, event):
            '''Ativar e desativar caixa de texto (Altura do corpo de Prova)'''
            if  self.check.GetValue() == False:

                self.alturaCorpoProva.Destroy()
                self.alturaCorpoProva = wx.TextCtrl(self.panel, -1, '', (370,260),(100,-1), style = wx.TE_READONLY)
                self.text09.SetForegroundColour((119,118,114))
                self.Refresh()

            else:
                self.alturaCorpoProva.Destroy()
                self.alturaCorpoProva = wx.TextCtrl(self.panel, -1, '', (370,260), (100,-1) )
                self.text09.SetForegroundColour((0,0,0))
                self.Refresh()

#----------------------------------------------------------------------
'''Inicializacao do programa'''
def main():
    app = wx.App()
    NovoEnsaio(None)
    app.MainLoop()

main()

########################################################################
