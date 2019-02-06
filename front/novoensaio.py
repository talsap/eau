# -*- coding: utf-8 -*-

'''Bibliotecas'''

import wx
from cadastrarcapsula import cadCapsula
from coleta import Coleta
import bancodedados

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
            self.Show()
            self.Refresh()

            FontTitle = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
            FontCorpo = wx.Font(9 , wx.SWISS, wx.NORMAL, wx.NORMAL)
            title = wx.StaticText(self.panel, -1, 'Dados do Ensaio', (20,20), (460,-1), wx.ALIGN_CENTER)
            title.SetFont(FontTitle)

            '''Conecção com o banco, lendo capsula'''
            self.capCadastradas = bancodedados.ler_cap()

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
            self.capsulaComboBox01 = wx.ComboBox(self.panel, -1, '', (240,390), (70, -1), self.capCadastradas)
            self.text13 = wx.StaticText(self.panel, -1, '2', (352,373), (5,-1), wx.ALIGN_LEFT)
            self.capsulaComboBox02 = wx.ComboBox(self.panel, -1, '', (320,390), (70, -1), self.capCadastradas)
            self.text14 = wx.StaticText(self.panel, -1, '3', (432,373), (5,-1), wx.ALIGN_LEFT)
            self.capsulaComboBox03 = wx.ComboBox(self.panel, -1, '', (400,390), (70, -1), self.capCadastradas)
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

#---------------------------------------------------------------------------------------------------------------------------------
        def CadastrarCapsula(self, event):
            dialogo = cadCapsula()
            resultado = dialogo.ShowModal()
            self.capCadastradas = bancodedados.ler_cap()
            self.capsulaComboBox01.Destroy()
            self.capsulaComboBox02.Destroy()
            self.capsulaComboBox03.Destroy()
            self.capsulaComboBox01 = wx.ComboBox(self.panel, -1, '', (240,390), (70, -1), self.capCadastradas)
            self.capsulaComboBox02 = wx.ComboBox(self.panel, -1, '', (320,390), (70, -1), self.capCadastradas)
            self.capsulaComboBox03 = wx.ComboBox(self.panel, -1, '', (400,390), (70, -1), self.capCadastradas)
            self.Refresh()

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
            '''Conecção com o banco, lendo capsula'''
            self.capCadastradas = bancodedados.ler_cap()

        #---------------------------------------------------------------
            if self.check.GetValue() == True:
                p = self.alturaCorpoProva.GetValue()
                p = format(p).replace(',','.')

                try:
                    p = float(p)
                except ValueError:
                    print('O valor altura do corpo de prova nao e um numero esperdo01')
                    menssagError = wx.MessageDialog(self, 'O valor altura do corpo de prova nao e um número esperdo', 'EAU', wx.OK|wx.ICON_INFORMATION)
                    aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                    menssagError.ShowModal()
                    menssagError.Destroy()
                    b = -1

            else:
                p = c
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
                p = float(p)

            except ValueError:
                print('Os valores digitados em algum dos campos nao esta da maneira esperada02')
                menssagError = wx.MessageDialog(self, 'Os valores digitados em algum dos campos não está da maneira esperada', 'EAU', wx.OK|wx.ICON_INFORMATION)
                aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                menssagError.ShowModal()
                menssagError.Destroy()
                b = -1

        #---------------------------------------------------------------
            if  a == 'Anel fixo' or  a == 'Anel flutuante':
                if b>0 and c>0 and d>0 and e>0 and f>0 and j>0 and k>0 and l>0 and m>0 and n>0 and o>0 and p>0:
                    if b!= '' and c!= '' and d!= '' and e!= '' and f!= '' and g!= '' and h!= '' and i!= '' and  j!= '' and k!= '' and l!= '' and m!= '' and n!= '' and o!= '' and p!= '':
                        if g in self.capCadastradas and h in self.capCadastradas and i in self.capCadastradas:
                            bancodedados.data_entry_dados(a, b, c, d, e, p, f)
                            bancodedados.data_entry_umidade(g, h, i, m, n, o, j, k, l)
                            self.Close(True)
                            con = Coleta()
                            resultado = con.ShowModal()

                        else:
                            print('O nome de uma das capsulas ou nao esta cadastrada ou nao foi informada')
                            menssagError = wx.MessageDialog(self, 'O nome de uma das cápsulas ou não está cadastrada ou não foi informado corretamente', 'EAU', wx.OK|wx.ICON_INFORMATION)
                            aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                            menssagError.ShowModal()
                            menssagError.Destroy()

                    else:
                        print('Algum dos campos esta vazio')

                else:
                    print('Algum dos campos esta digitado errado')

            else:
                print('Veja se voce prencheu o tipo de de anel')

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
