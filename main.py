# -*- coding: utf-8 -*-

'''Bibliotecas'''

import wx
import json

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

'''Tela Cadastrar Cápsula'''
class Coleta(wx.Dialog):

#----------------------------------------------------------------------
        def __init__(self, *args, **kwargs):
            wx.Dialog.__init__(self, None, -1, 'EAU')

            self.panel = wx.Panel(self)
            self.SetSize((500,600))
            self.Centre()
            self.Show()

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

'''Tela Cadastrar Cápsula'''
class cadCapsula(wx.Dialog):

#----------------------------------------------------------------------
        def __init__(self, *args, **kwargs):
            wx.Dialog.__init__(self, None, -1, 'EAU')

            self.panel = wx.Panel(self)
            self.SetSize((200,175))
            self.Centre()
            self.Show()

            self.nomeCap = wx.TextCtrl(self.panel, -1, '', (60,20), (120,-1), wx.TE_RIGHT)
            self.text12 = wx.StaticText(self.panel, -1, 'Nome:', (15,25), (35,-1), wx.ALIGN_LEFT)
            self.massaCap = wx.TextCtrl(self.panel, -1, '', (105,60), (75,-1), wx.TE_RIGHT)
            self.text12 = wx.StaticText(self.panel, -1, 'Massa (g):', (45,65), (60,-1), wx.ALIGN_LEFT)
            self.Cadastrar = wx.Button(self.panel, -1, 'Cadastrar', pos = (60, 100))
            self.Bind(wx.EVT_BUTTON, self.CadCapOk, self.Cadastrar)

#----------------------------------------------------------------------
        def CadCapOk(self, event):
            a = self.nomeCap.GetValue()
            b = self.massaCap.GetValue()
            b = format(b).replace(',','.')
            try:
                b = float(b)
            except ValueError:
                print('O valor digitado nao e o esperado')
                menssagError = wx.MessageDialog(self, 'Preencha os campos corretamente', 'EAU', wx.OK|wx.ICON_INFORMATION)
                aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                menssagError.ShowModal()
                menssagError.Destroy()

            capsula = open('capsulas.json', 'r')
            self.capCadastradas = json.load(capsula)

            if a!= '' and  b!= '' and b>0:
                if a in self.capCadastradas:
                    print('Ja existe essa capsula')
                    menssagError = wx.MessageDialog(self, 'Já existe uma capsula com esse nome', 'EAU', wx.OK|wx.ICON_INFORMATION)
                    aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                    menssagError.ShowModal()
                    menssagError.Destroy()
                else:
                    capsula.close()
                    capsula = open('capsulas.json', 'w')
                    self.capCadastradas.append(a)
                    self.capCadastradas.append(b)
                    json.dump(self.capCadastradas, capsula)
                    capsula.close()
                    self.Close(True)
                    
            else:
                print('O valor digitado nao e o esperado')

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

'''Tela Novo Ensaio'''
class TelaNovoEnsaio(wx.Dialog):

#---------------------------------------------------------------------------------------------------------------------------------
        def __init__(self, *args, **kwargs):
            wx.Dialog.__init__(self, None, -1, 'EAU - Novo Ensaio')

            self.panel = wx.Panel(self)
            self.SetSize((500,600))
            self.Centre()
            a = self.Show()

            FontTitle = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
            FontCorpo = wx.Font(9 , wx.SWISS, wx.NORMAL, wx.NORMAL)
            title = wx.StaticText(self.panel, -1, 'Dados do Ensaio', (20,20), (460,-1), wx.ALIGN_CENTER)
            title.SetFont(FontTitle)

            '''Criar arquivo capsulas no acesso inicial'''
            try:
                capsula = open('capsulas.json', 'r')
            except:
                capsula = open('capsulas.json', 'w')
                self.capCadastradas = [' ']
                json.dump(self.capCadastradas, capsula)
                capsula.close()

            capsula = open('capsulas.json', 'r')
            self.capCadastradas = json.load(capsula)
            self.capCadastradas = [str(x) for x in self.capCadastradas]
            print(self.capCadastradas)

            self.FontTitle =wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
            self.title = wx.StaticText(self.panel, -1, 'Dados do Ensaio', (20,20), (460,-1), wx.ALIGN_CENTER)
            self.title.SetFont(self.FontTitle)
            self.texto01 = wx.StaticText(self.panel, -1, 'CELULA DE ADENSAMENTO:',(20,50), (460,-1), wx.ALIGN_LEFT)
            self.texto02 = wx.StaticText(self.panel, -1, 'Tipo de Anel',(240,60), (230,-1), wx.ALIGN_LEFT)
            self.tipoAnel = wx.ComboBox(self.panel, -1, 'Selecione um item da lista', (240,80), (230, -1), choices = ('Anel fixo', 'Anel flutuante'))
            self.texto03 = wx.StaticText(self.panel, -1, 'ANEL:',(20,110), (40,-1), wx.ALIGN_LEFT)
            self.diamtroInterno = wx.TextCtrl(self.panel, -1, '', (170,130),(100,-1), wx.TE_RIGHT)
            self.texto05 = wx.StaticText(self.panel, -1, 'Diâmetro Interno (mm)',(40,135), (125,-1), wx.ALIGN_LEFT)
            self.alturaAnel = wx.TextCtrl(self.panel, -1, '', (370,130),(100,-1), wx.TE_RIGHT)
            self.texto04 = wx.StaticText(self.panel, -1, 'Altura (mm)',(297,135), (70,-1), wx.ALIGN_LEFT)
            self.massaAnel = wx.TextCtrl(self.panel, -1, '', (370,160),(100,-1), wx.TE_RIGHT)
            self.texto06 = wx.StaticText(self.panel, -1, 'Massa do Anel (g)',(267,165), (95,-1), wx.ALIGN_LEFT)
            self.massaConjunto = wx.TextCtrl(self.panel, -1, '', (370,190),(100,-1), wx.TE_RIGHT)
            self.texto07 = wx.StaticText(self.panel, -1, 'Massa do conjunto corpo de prova e anel de adensamento (g)',(35,195), (330,-1), wx.ALIGN_LEFT)
            self.texto08 = wx.StaticText(self.panel, -1, 'CORPO-DE-PROVA:',(20,230), (460,-1), wx.ALIGN_LEFT)
            self.check = wx.CheckBox(self.panel, -1, 'Altura do corpo de prova diferente da do anel', (210,240),(260,-1), wx.ALIGN_RIGHT)
            self.alturaCorpoProva = wx.TextCtrl(self.panel, -1, '', (370,260),(100,-1), style = wx.TE_READONLY | wx.TE_RIGHT)
            self.text09 = wx.StaticText(self.panel, -1, 'Altura do corpo de prova (mm)', (197,265),(170,-1), wx.ALIGN_LEFT)
            self.text09.SetForegroundColour((119,118,114))
            self.Bind(wx.EVT_CHECKBOX, self.onCheck, self.check)
            self.text10 = wx.StaticText(self.panel, -1, 'Massa específica dos grãos de solo (g/cm³)', (135,295), (230,-1), wx.ALIGN_LEFT)
            self.massaEspeciciaGraosSolo = wx.TextCtrl(self.panel, -1, '', (370,290),(100,-1), wx.TE_RIGHT)
            self.text11 = wx.StaticText(self.panel, -1, 'TEOR DE UMIDADE INICIAL:', (20,330), (150,-1), wx.ALIGN_LEFT)
            self.CadastrarCapsulaButton = wx.Button(self.panel, -1, 'Cadastrar Cápsula', pos = (20, 350))
            self.Bind(wx.EVT_BUTTON, self.CadastrarCapsula, self.CadastrarCapsulaButton)
            self.text12 = wx.StaticText(self.panel, -1, '1', (272,373), (5,-1), wx.ALIGN_LEFT)
            self.capsulaComboBox01 = wx.ComboBox(self.panel, -1, '', (240,390), (70, -1), self.capCadastradas[1::2])
            self.text13 = wx.StaticText(self.panel, -1, '2', (352,373), (5,-1), wx.ALIGN_LEFT)
            self.capsulaComboBox02 = wx.ComboBox(self.panel, -1, '', (320,390), (70, -1), self.capCadastradas[1::2])
            self.text14 = wx.StaticText(self.panel, -1, '3', (432,373), (5,-1), wx.ALIGN_LEFT)
            self.capsulaComboBox03 = wx.ComboBox(self.panel, -1, '', (400,390), (70, -1), self.capCadastradas[1::2])
            self.text15 = wx.StaticText(self.panel, -1, 'Cápsula', (191,395), (45,-1), wx.ALIGN_LEFT)
            self.massaUmida01 = wx.TextCtrl(self.panel, -1, '', (240,420), (70, -1), wx.TE_RIGHT)
            self.massaUmida02 = wx.TextCtrl(self.panel, -1, '', (320,420), (70, -1), wx.TE_RIGHT)
            self.massaUmida03 = wx.TextCtrl(self.panel, -1, '', (400,420), (70, -1), wx.TE_RIGHT)
            self.text16 = wx.StaticText(self.panel, -1, 'Massa Úmida (g)', (143,425), (95,-1), wx.ALIGN_LEFT)
            self.massaSeca01 = wx.TextCtrl(self.panel, -1, '', (240,450), (70, -1), wx.TE_RIGHT)
            self.massaSeca02 = wx.TextCtrl(self.panel, -1, '', (320,450), (70, -1), wx.TE_RIGHT)
            self.massaSeca03 = wx.TextCtrl(self.panel, -1, '', (400,450), (70, -1), wx.TE_RIGHT)
            self.text17 = wx.StaticText(self.panel, -1, 'Massa Seca (g)', (154,455), (85,-1), wx.ALIGN_LEFT)
            self.continuar = wx.Button(self.panel, -1, 'Continuar', (20, 500), (450,-1), wx.ALIGN_LEFT)
            self.Bind(wx.EVT_BUTTON, self.Prosseguir, self.continuar)
            capsula.close()

#---------------------------------------------------------------------------------------------------------------------------------
        def CadastrarCapsula(self, event):
            dialogo = cadCapsula()
            resultado = dialogo.ShowModal()

#---------------------------------------------------------------------------------------------------------------------------------
        def Prosseguir(self, event):
            a = self.tipoAnel.GetValue()
            b = self.diamtroInterno.GetValue()
            b = format(b).replace(',','.')
            c = self.alturaAnel.GetValue()
            c = format(c).replace(',','.')
            d = self.massaAnel.GetValue()
            d = format(d).replace(',','.')
            e = self.massaConjunto.GetValue()
            e = format(e).replace(',','.')
            f = self.massaEspeciciaGraosSolo.GetValue()
            f = format(f).replace(',','.')
            g = self.capsulaComboBox01.GetValue()
            h = self.capsulaComboBox02.GetValue()
            i = self.capsulaComboBox03.GetValue()
            j = self.massaUmida01.GetValue()
            j = format(j).replace(',','.')
            k = self.massaUmida02.GetValue()
            k = format(k).replace(',','.')
            l = self.massaUmida03.GetValue()
            l = format(l).replace(',','.')
            m = self.massaSeca01.GetValue()
            m = format(m).replace(',','.')
            n = self.massaSeca02.GetValue()
            n = format(n).replace(',','.')
            o = self.massaSeca03.GetValue()
            o = format(o).replace(',','.')
            capsula = open('capsulas.json', 'r')
            self.capCadastradas = json.load(capsula)
            self.capCadastradas = [str(x) for x in self.capCadastradas]

        #---------------------------------------------------------------
            if self.check.GetValue() == True:
                print('entrou')
                p = self.alturaCorpoProva.GetValue()
                p = format(p).replace(',','.')

                try:
                    p = float(p)
                except ValueError:
                    print('O valor altura do corpo de prova nao e um numero esperdo')
                    menssagError = wx.MessageDialog(self, 'O valor altura do corpo de prova nao e um número esperdo', 'EAU', wx.OK|wx.ICON_INFORMATION)
                    aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                    menssagError.ShowModal()
                    menssagError.Destroy()
            else:
                p = 1
        #---------------------------------------------------------------
            try:
                b = float(b)
                c = float(c)
                d = float(d)
                e = float(e)
                f = float(f)
                j = float(j)
                k = float(k)
                l = float(l)
                m = float(m)
                n = float(n)
                o = float(o)
            except ValueError:
                print('Os valores digitados em algum dos campos nao esta da maneira esperada')
                menssagError = wx.MessageDialog(self, 'Os valores digitados em algum dos campos não está da maneira esperada', 'EAU', wx.OK|wx.ICON_INFORMATION)
                aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                menssagError.ShowModal()
                menssagError.Destroy()
        #---------------------------------------------------------------
            if  a == 'Anel fixo' or  a == 'Anel flutuante'   and b>0 and c>0 and d>0 and e>0 and f>0 and j>0 and k>0 and l>0 and m>0 and n>0 and o>0 and p>0:
                if b!= '' and c!= '' and d!= '' and e!= '' and f!= '' and g!= '' and h!= '' and i!= '' and  j!= '' and k!= '' and l!= '' and m!= '' and n!= '' and o!= '' and p!= '':
                    if g in self.capCadastradas and h in self.capCadastradas and i in self.capCadastradas:
                        self.Close(True)
                        con = Coleta()
                        resultado = con.ShowModal()
                        capsula.close()

                    else:
                        print('O nome de uma das cápsulas ou não está cadastrada ou não foi informada')
                        menssagError = wx.MessageDialog(self, 'O nome de uma das cápsulas ou não está cadastrada ou não foi informado corretamente', 'EAU', wx.OK|wx.ICON_INFORMATION)
                        aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                        menssagError.ShowModal()
                        menssagError.Destroy()

                else:
                    print('Algum dos campos está vazio')
                    capsula.close()
            else:
                print('Veja se todos os dados foram preenchidos corretamente')
                capsula.close()

#---------------------------------------------------------------------------------------------------------------------------------
        def onCheck(self, event):
            '''Ativar e desativar caixa de texto (Altura do corpo de Prova)'''
            if  self.check.GetValue() == False:

                self.alturaCorpoProva.Destroy()
                self.alturaCorpoProva = wx.TextCtrl(self.panel, -1, '', (370,260),(100,-1), style = wx.TE_READONLY | wx.TE_RIGHT)
                self.text09.SetForegroundColour((119,118,114))
                self.Refresh()

            else:
                self.alturaCorpoProva.Destroy()
                self.alturaCorpoProva = wx.TextCtrl(self.panel, -1, '', (370,260), (100,-1), wx.TE_RIGHT)
                self.text09.SetForegroundColour((0,0,0))
                self.Refresh()

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
          self.button = wx.Button(panel, -1, 'Novo Ensaio')
          self.button.Centre()
          self.Bind(wx.EVT_BUTTON, self.NovoEnsaio, self.button)

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

#---------------------------------------------------------------------------------------------------------------------------------
'''Inicializacao do programa'''
def main():
     app = wx.App()
     Tela(None)
     app.MainLoop()

main()

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
