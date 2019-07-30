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
        def __init__(self, date, local, operador, profundidade, IDE_E, *args, **kwargs):
            wx.Dialog.__init__(self, None, -1, 'EAU - Novo Ensaio', style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION)

            self.date = date
            self.local = local
            self.operador = operador
            self.profundidade  = profundidade
            self.IDE_E = IDE_E

            self.panel = wx.Panel(self)
            self.SetSize((500,600))
            self.Centre()
            self.Show()

            '''Conecção com o banco, lendo capsula'''
            self.capCadastradas = bancodedados.ler_cap()

            self.FontTitle =wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
            self.title = wx.StaticText(self.panel, -1, 'Dados do Ensaio', (20,20), (460,-1), wx.ALIGN_CENTER)
            self.title.SetFont(self.FontTitle)
            self.texto01 = wx.StaticText(self.panel, -1, 'CELULA DE ADENSAMENTO:',(20,50), (460,-1), wx.ALIGN_LEFT)
            self.texto02 = wx.StaticText(self.panel, -1, 'Tipo de Anel',(240,60), (230,-1), wx.ALIGN_LEFT)
            self.tipoAnel = wx.ComboBox(self.panel, -1, 'Selecione um item da lista', (240,80), (230, -1), choices = ('Anel fixo', 'Anel flutuante'))
            self.texto03 = wx.StaticText(self.panel, -1, 'ANEL:',(20,110), (40,-1), wx.ALIGN_LEFT)
            self.text04_1 = wx.StaticText(self.panel, -1, '1', (272,120), (5,-1), wx.ALIGN_LEFT)
            self.text04_2 = wx.StaticText(self.panel, -1, '2', (352,120), (5,-1), wx.ALIGN_LEFT)
            self.text04_3 = wx.StaticText(self.panel, -1, '3', (432,120), (5,-1), wx.ALIGN_LEFT)
            self.diamtroInterno01 = wx.TextCtrl(self.panel, -1, '', (240,137),(70,-1), wx.TE_RIGHT)
            self.diamtroInterno02 = wx.TextCtrl(self.panel, -1, '', (320,137),(70,-1), wx.TE_RIGHT)
            self.diamtroInterno03 = wx.TextCtrl(self.panel, -1, '', (400,137),(70,-1), wx.TE_RIGHT)
            self.texto05 = wx.StaticText(self.panel, -1, 'Diâmetro Interno (mm)',(111,142), (125,-1), wx.ALIGN_LEFT)
            self.alturaAnel01 = wx.TextCtrl(self.panel, -1, '', (240,167),(70,-1), wx.TE_RIGHT)
            self.alturaAnel02 = wx.TextCtrl(self.panel, -1, '', (320,167),(70,-1), wx.TE_RIGHT)
            self.alturaAnel03 = wx.TextCtrl(self.panel, -1, '', (400,167),(70,-1), wx.TE_RIGHT)
            self.texto04 = wx.StaticText(self.panel, -1, 'Altura (mm)',(168,172), (70,-1), wx.ALIGN_LEFT)
            self.massaAnel = wx.TextCtrl(self.panel, -1, '', (400,197),(70,-1), wx.TE_RIGHT)
            self.texto06 = wx.StaticText(self.panel, -1, 'Massa do Anel (g)',(299,202), (95,-1), wx.ALIGN_LEFT)
            self.massaConjunto = wx.TextCtrl(self.panel, -1, '', (400,227),(70,-1), wx.TE_RIGHT)
            self.texto07 = wx.StaticText(self.panel, -1, 'Massa do conjunto corpo de prova e anel de adensamento (g)',(67,231), (330,-1), wx.ALIGN_LEFT)
            self.texto08 = wx.StaticText(self.panel, -1, 'CORPO-DE-PROVA:',(20,270), (460,-1), wx.ALIGN_LEFT)
            self.check = wx.CheckBox(self.panel, -1, 'Altura do corpo de prova diferente da do anel', (210,280),(260,-1), wx.ALIGN_RIGHT)
            self.alturaCorpoProva = wx.TextCtrl(self.panel, -1, '', (370,300),(100,-1), style = wx.TE_READONLY | wx.TE_RIGHT)
            self.text09 = wx.StaticText(self.panel, -1, 'Altura do corpo de prova (mm)', (197,305),(170,-1), wx.ALIGN_LEFT)
            self.text09.SetForegroundColour((119,118,114))
            self.Bind(wx.EVT_CHECKBOX, self.onCheck, self.check)
            self.adicionar = wx.ComboBox(self.panel, -1, 'Adicionar depois', (20,330), (110, -1), choices = ('Adicionar agora', 'Adicionar depois'))
            self.Bind(wx.EVT_COMBOBOX, self.addDadosDepois, self.adicionar)
            self.text10 = wx.StaticText(self.panel, -1, 'Massa específica dos grãos de solo (g/cm³)', (135,335), (230,-1), wx.ALIGN_LEFT)
            self.text10.SetForegroundColour((119,118,114))
            self.massaEspeciciaGraosSolo = wx.TextCtrl(self.panel, -1, '', (370,330),(100,-1), style = wx.TE_READONLY | wx.TE_RIGHT)
            self.text11 = wx.StaticText(self.panel, -1, 'TEOR DE UMIDADE INICIAL:', (20,370), (150,-1), wx.ALIGN_LEFT)
            self.CadastrarCapsulaButton = wx.Button(self.panel, -1, 'Cadastrar Cápsula', pos = (20, 390))
            self.Bind(wx.EVT_BUTTON, self.CadastrarCapsula, self.CadastrarCapsulaButton)
            self.text12 = wx.StaticText(self.panel, -1, '1', (272,403), (5,-1), wx.ALIGN_LEFT)
            self.capsulaComboBox01 = wx.ComboBox(self.panel, -1, '', (240,425), (70, -1), self.capCadastradas)
            self.text13 = wx.StaticText(self.panel, -1, '2', (352,403), (5,-1), wx.ALIGN_LEFT)
            self.capsulaComboBox02 = wx.ComboBox(self.panel, -1, '', (320,425), (70, -1), self.capCadastradas)
            self.text14 = wx.StaticText(self.panel, -1, '3', (432,403), (5,-1), wx.ALIGN_LEFT)
            self.capsulaComboBox03 = wx.ComboBox(self.panel, -1, '', (400,425), (70, -1), self.capCadastradas)
            self.text15 = wx.StaticText(self.panel, -1, 'Cápsula', (191,430), (45,-1), wx.ALIGN_LEFT)
            self.massaUmida01 = wx.TextCtrl(self.panel, -1, '', (240,455), (70, -1), wx.TE_RIGHT)
            self.massaUmida02 = wx.TextCtrl(self.panel, -1, '', (320,455), (70, -1), wx.TE_RIGHT)
            self.massaUmida03 = wx.TextCtrl(self.panel, -1, '', (400,455), (70, -1), wx.TE_RIGHT)
            self.text16 = wx.StaticText(self.panel, -1, 'Massa Úmida (g)', (143,460), (95,-1), wx.ALIGN_LEFT)
            self.adicionarMS = wx.ComboBox(self.panel, -1, 'Adicionar depois', (20,486), (110, -1), choices = ('Adicionar agora', 'Adicionar depois'))
            self.Bind(wx.EVT_COMBOBOX, self.addDadosDepoisMS, self.adicionarMS)
            self.massaSeca01 = wx.TextCtrl(self.panel, -1, '', (240,485), (70, -1), style = wx.TE_READONLY | wx.TE_RIGHT)
            self.massaSeca02 = wx.TextCtrl(self.panel, -1, '', (320,485), (70, -1), style = wx.TE_READONLY | wx.TE_RIGHT)
            self.massaSeca03 = wx.TextCtrl(self.panel, -1, '', (400,485), (70, -1), style = wx.TE_READONLY | wx.TE_RIGHT)
            self.text17 = wx.StaticText(self.panel, -1, 'Massa Seca (g)', (154,490), (85,-1), wx.ALIGN_LEFT)
            self.text17.SetForegroundColour((119,118,114))
            self.continuar = wx.Button(self.panel, -1, 'Continuar', (20, 530), (450,-1), wx.ALIGN_LEFT)
            self.Bind(wx.EVT_BUTTON, self.Prosseguir, self.continuar)

#---------------------------------------------------------------------------------------------------------------------------------
        def CadastrarCapsula(self, event):
            dialogo = cadCapsula()
            resultado = dialogo.ShowModal()
            self.capCadastradas = bancodedados.ler_cap()
            self.capsulaComboBox01.Destroy()
            self.capsulaComboBox02.Destroy()
            self.capsulaComboBox03.Destroy()
            self.capsulaComboBox01 = wx.ComboBox(self.panel, -1, '', (240,425), (70, -1), self.capCadastradas)
            self.capsulaComboBox02 = wx.ComboBox(self.panel, -1, '', (320,425), (70, -1), self.capCadastradas)
            self.capsulaComboBox03 = wx.ComboBox(self.panel, -1, '', (400,425), (70, -1), self.capCadastradas)
            self.Refresh()

#---------------------------------------------------------------------------------------------------------------------------------
        def Prosseguir(self, event):
            a = self.tipoAnel.GetValue()
            b1 = self.diamtroInterno01.GetValue()
            b1 = format(b1).replace(',','.')
            b2 = self.diamtroInterno02.GetValue()
            b2 = format(b2).replace(',','.')
            b3 = self.diamtroInterno03.GetValue()
            b3 = format(b3).replace(',','.')
            c1 = self.alturaAnel01.GetValue()
            c1 = format(c1).replace(',','.')
            c2 = self.alturaAnel02.GetValue()
            c2 = format(c2).replace(',','.')
            c3 = self.alturaAnel03.GetValue()
            c3 = format(c3).replace(',','.')
            d = self.massaAnel.GetValue()
            d = format(d).replace(',','.')
            e = self.massaConjunto.GetValue()
            e = format(e).replace(',','.')
            g = self.capsulaComboBox01.GetValue()
            h = self.capsulaComboBox02.GetValue()
            i = self.capsulaComboBox03.GetValue()
            j = self.massaUmida01.GetValue()
            j = format(j).replace(',','.')
            k = self.massaUmida02.GetValue()
            k = format(k).replace(',','.')
            l = self.massaUmida03.GetValue()
            l = format(l).replace(',','.')
            q = self.date
            r = self.local
            s = self.operador
            t = self.profundidade
            u1 = self.IDE_E
            '''Conecção com o banco, lendo capsula'''
            self.capCadastradas = bancodedados.ler_cap()

        #---------------------------------------------------------------
            if self.check.GetValue() == True:
                p = self.alturaCorpoProva.GetValue()
                p = format(p).replace(',','.')

                try:
                    p = float(p)
                except ValueError:
                    print('O valor altura do corpo de prova ou altura do anel nao e um numero esperdo')
                    menssagError = wx.MessageDialog(self, 'O valor altura do corpo de prova ou altura do anel nao e um número esperdo', 'EAU', wx.OK|wx.ICON_INFORMATION)
                    aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                    menssagError.ShowModal()
                    menssagError.Destroy()
                    b = -1

            else:
                try:
                    c1 = float(c1)
                    c2 = float(c2)
                    c3 = float(c3)
                except ValueError:
                    print('O valor altura do corpo de prova ou altura do anel nao e um numero esperdo')
                    c1 = -1

                if c1>0 and c2>0 and c3>0 and c1!= '' and c2!= '' and c3!= '':
                    p = (c1+c2+c3)/3
                else:
                    p = -1

        #---------------------------------------------------------------
            if self.adicionar.GetValue() == 'Adicionar agora':
                x = 0
                f = self.massaEspeciciaGraosSolo.GetValue()
                f = format(f).replace(',','.')
                try:
                    f = float(f)
                except ValueError:
                    print('Os valores digitado para massa especifica nao e esperdo')
                    menssagError = wx.MessageDialog(self, 'Os valor para massa especifica não está da maneira esperada', 'EAU', wx.OK|wx.ICON_INFORMATION)
                    aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                    menssagError.ShowModal()
                    menssagError.Destroy()
                    f = -1

            if self.adicionar.GetValue() == 'Adicionar depois':
                x = 1

        #---------------------------------------------------------------
            if self.adicionarMS.GetValue() == 'Adicionar agora':
                '''O y Corresponde aos status de que oa massa seca ja foi preenchida'''
                y = 0
                m = self.massaSeca01.GetValue()
                m = format(m).replace(',','.')
                n = self.massaSeca02.GetValue()
                n = format(n).replace(',','.')
                o = self.massaSeca03.GetValue()
                o = format(o).replace(',','.')
                try:
                    m = float(m)
                    n = float(n)
                    o = float(o)
                except ValueError:
                    print('Os valores digitado para massa especifica nao e esperdo')
                    menssagError = wx.MessageDialog(self, 'Os valor para massa especifica não está da maneira esperada', 'EAU', wx.OK|wx.ICON_INFORMATION)
                    aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                    menssagError.ShowModal()
                    menssagError.Destroy()
                    m = -1
                    n = -1
                    o = -1

            if self.adicionarMS.GetValue() == 'Adicionar depois':
                '''O y Corresponde aos status de que oa massa seca ja foi preenchida'''
                y = 1
        #---------------------------------------------------------------
            try:
                b1 = float(b1)
                b2 = float(b2)
                b3 = float(b3)
                c1 = float(c1)
                c2 = float(c2)
                c3 = float(c3)
                d = float(d)
                e = float(e)
                j = float(j)
                k = float(k)
                l = float(l)
                p = float(p)

            except ValueError:
                print('Os valores digitados em algum dos campos nao esta da maneira esperada')
                menssagError = wx.MessageDialog(self, 'Os valores digitados em algum dos campos não está da maneira esperada', 'EAU', wx.OK|wx.ICON_INFORMATION)
                aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                menssagError.ShowModal()
                menssagError.Destroy()
                b1 = -1

        #---------------------------------------------------------------
            if  a == 'Anel fixo' or  a == 'Anel flutuante':
                if b1>0 and b2>0 and b3>0 and c1>0 and c2>0 and c3>0 and d>0 and e>0 and j>0 and k>0 and l>0 and p>0:
                    if b1!= '' and b2!= '' and b3!= '' and c1!= '' and c2!= '' and c3!= '' and d!= '' and e!= '' and g!= '' and h!= '' and i!= '' and  j!= '' and k!= '' and l!= ''  and p!= '':
                        if g in self.capCadastradas and h in self.capCadastradas and i in self.capCadastradas and g!= h and g!= i and h!= i:
                            b = (b1+b2+b3)/3
                            c = (c1+c2+c3)/3
                            if x == 1 and y == 1:
                                f = ''
                                m = ''
                                n = ''
                                o = ''
                                bancodedados.data_entry_dados(a, b, c, d, e, p, f, q, r, s, t, u1)
                                bancodedados.data_entry_umidade(g, h, i, m, n, o, j, k, l)
                                bancodedados.data_termino()
                                idR = bancodedados.idReturn()
                                '''Diálogo para Pressao de Assentamento'''
                                dlg = wx.MessageDialog(None, 'Deseja Adicionar uma pressão de Assentamento?', 'EAU', wx.YES_NO | wx .CENTRE| wx.YES_DEFAULT | wx.ICON_INFORMATION)
                                result = dlg.ShowModal()
                                if result == wx.ID_YES:
                                    Assentamento = True
                                else:
                                    Assentamento = False

                                con = Coleta(idR, y, Assentamento)
                                resultado = con.Show()
                                self.Close(True)
                            if x == 1 and y == 0 and m>0 and n>0 and o>0:
                                f = ''
                                bancodedados.data_entry_dados(a, b, c, d, e, p, f, q, r, s, t, u1)
                                bancodedados.data_entry_umidade(g, h, i, m, n, o, j, k, l)
                                bancodedados.data_termino()
                                idR = bancodedados.idReturn()
                                '''Diálogo para Pressao de Assentamento'''
                                dlg = wx.MessageDialog(None, 'Deseja Adicionar uma pressão de Assentamento?', style = wx.YES_NO | wx.CENTRE | wx.YES_DEFAULT | wx.ICON_INFORMATION)
                                result = dlg.ShowModal()
                                if result == wx.ID_YES:
                                    Assentamento = True
                                else:
                                    Assentamento = False

                                con = Coleta(idR, y, Assentamento)
                                resultado = con.Show()
                                self.Close(True)
                            if x == 0 and y == 1 and f>0:
                                m = ''
                                n = ''
                                o = ''
                                bancodedados.data_entry_dados(a, b, c, d, e, p, f, q, r, s, t, u1)
                                bancodedados.data_entry_umidade(g, h, i, m, n, o, j, k, l)
                                bancodedados.data_termino()
                                idR = bancodedados.idReturn()
                                '''Diálogo para Pressao de Assentamento'''
                                dlg = wx.MessageDialog(None, 'Deseja Adicionar uma pressão de Assentamento?', 'EAU', wx.YES_NO | wx .CENTRE| wx.YES_DEFAULT | wx.ICON_INFORMATION)
                                result = dlg.ShowModal()
                                if result == wx.ID_YES:
                                    Assentamento = True
                                else:
                                    Assentamento = False

                                con = Coleta(idR, y, Assentamento)
                                resultado = con.Show()
                                self.Close(True)
                            if x == 0 and y == 0 and f>0 and m>0 and n>0 and o>0:
                                bancodedados.data_entry_dados(a, b, c, d, e, p, f, q, r, s, t, u1)
                                bancodedados.data_entry_umidade(g, h, i, m, n, o, j, k, l)
                                bancodedados.data_termino()
                                idR = bancodedados.idReturn()

                                '''Diálogo para Pressao de Assentamento'''
                                dlg = wx.MessageDialog(None, 'Deseja Adicionar uma pressão de Assentamento?', 'EAU', wx.YES_NO | wx .CENTRE| wx.YES_DEFAULT | wx.ICON_INFORMATION)
                                result = dlg.ShowModal()
                                if result == wx.ID_YES:
                                    Assentamento = True
                                else:
                                    Assentamento = False

                                con = Coleta(idR, y, Assentamento)
                                resultado = con.Show()
                                self.Close(True)
                        else:
                            print('O nome de uma das capsulas ou nao esta cadastrada ou nao foi informada ou e identica a outra')
                            menssagError = wx.MessageDialog(self, 'O nome de uma das cápsulas ou não está cadastrada ou não foi informada corretamente ou pode ter duas cápsulas idênticas', 'EAU', wx.OK|wx.ICON_INFORMATION)
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
                self.alturaCorpoProva = wx.TextCtrl(self.panel, -1, '', (370,300),(100,-1), style = wx.TE_READONLY | wx.TE_RIGHT)
                self.text09.SetForegroundColour((119,118,114))
                self.Refresh()

            else:
                self.alturaCorpoProva.Destroy()
                self.alturaCorpoProva = wx.TextCtrl(self.panel, -1, '', (370,300),(100,-1), wx.TE_RIGHT)
                self.text09.SetForegroundColour((0,0,0))
                self.Refresh()

#---------------------------------------------------------------------------------------------------------------------------------
        def addDadosDepois(self, event):
            '''Ativar e desativar caixa de texto (Massa específica dos grãos de solo (g/cm³))'''
            if  self.adicionar.GetValue() == 'Adicionar depois':

                self.massaEspeciciaGraosSolo.Destroy()
                self.massaEspeciciaGraosSolo = wx.TextCtrl(self.panel, -1, '', (370,330),(100,-1), style = wx.TE_READONLY | wx.TE_RIGHT)
                self.text10.SetForegroundColour((119,118,114))
                self.Refresh()

            if  self.adicionar.GetValue() == 'Adicionar agora':
                self.massaEspeciciaGraosSolo.Destroy()
                self.massaEspeciciaGraosSolo = wx.TextCtrl(self.panel, -1, '', (370,330),(100,-1), wx.TE_RIGHT)
                self.text10.SetForegroundColour((0,0,0))
                self.Refresh()

#---------------------------------------------------------------------------------------------------------------------------------
        def addDadosDepoisMS(self, event):
            '''Ativar e desativar caixa de texto (Massa específica dos grãos de solo (g/cm³))'''
            if  self.adicionarMS.GetValue() == 'Adicionar depois':

                self.massaSeca01.Destroy()
                self.massaSeca02.Destroy()
                self.massaSeca03.Destroy()
                self.massaSeca01 = wx.TextCtrl(self.panel, -1, '', (240,485), (70, -1), style = wx.TE_READONLY | wx.TE_RIGHT)
                self.massaSeca02 = wx.TextCtrl(self.panel, -1, '', (320,485), (70, -1), style = wx.TE_READONLY | wx.TE_RIGHT)
                self.massaSeca03 = wx.TextCtrl(self.panel, -1, '', (400,485), (70, -1), style = wx.TE_READONLY | wx.TE_RIGHT)
                self.text17.SetForegroundColour((119,118,114))
                self.Refresh()

            if  self.adicionarMS.GetValue() == 'Adicionar agora':
                self.massaSeca01.Destroy()
                self.massaSeca02.Destroy()
                self.massaSeca03.Destroy()
                self.massaSeca01 = wx.TextCtrl(self.panel, -1, '', (240,485), (70, -1), wx.TE_RIGHT)
                self.massaSeca02 = wx.TextCtrl(self.panel, -1, '', (320,485), (70, -1), wx.TE_RIGHT)
                self.massaSeca03 = wx.TextCtrl(self.panel, -1, '', (400,485), (70, -1), wx.TE_RIGHT)
                self.text17.SetForegroundColour((0,0,0))
                self.Refresh()

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
