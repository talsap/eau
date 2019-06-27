# -*- coding: utf-8 -*-

'''Bibliotecas'''

import wx
import re
import wx.adv
import bancodedados
import datetime
import wx.lib.mixins.listctrl  as  listmix
from coleta02 import Coleta02

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
'''Classe da Lista editável'''
class EditableListCtrl(wx.ListCtrl, listmix.TextEditMixin):

    #----------------------------------------------------------------------
        def __init__(self, parent, ID=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):
            wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
            listmix.TextEditMixin.__init__(self)

##################################################################################################################################
'''Tela Inicial'''
class Editar(wx.Dialog):

#---------------------------------------------------------------------------------------------------------------------------------
     def __init__(self, id, *args, **kwargs):
         wx.Dialog.__init__(self, None, -1, 'EAU - Editar')

         # Aqui criamos um painel e um Notebook representado as guias
         panel = wx.Panel(self)
         nb = wx.Notebook(panel)

         # crie as janelas da página como filhas do Notebook
         page01 = Page01(nb, id)
         page02 = Page02(nb, id)
         page03 = Page03(nb, id)

         # adicione as páginas ao caderno com o rótulo para mostrar na guia
         nb.AddPage(page01, "Dados do Ensaio")
         nb.AddPage(page02, "Dados Coletados")
         nb.AddPage(page03, "Dados Calculados")

         sizer = wx.BoxSizer()
         sizer.Add(nb, 1, wx.EXPAND)
         panel.SetSizer(sizer)
         self.SetSize((500,630))
         self.Centre()
         self.Show()

#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
class Page01(wx.Panel):

#---------------------------------------------------------------------------------------------------------------------------------
     def __init__(self, parent, id):
         super(Page01, self).__init__(parent)
         self.id = id

         caps = bancodedados.caps(id)
         massaSeca = bancodedados.mSeca(id)
         massaUmida = bancodedados.mUmida(id)
         dadosIniciais = bancodedados.DadosIniciaisParaEdit(id)

         self.FontTitle =wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
         self.title = wx.StaticText(self, -1, 'DADOS DO ENSAIO', (20,20), (460,-1), wx.ALIGN_CENTER)
         self.title.SetFont(self.FontTitle)
         self.texto1 = wx.StaticText(self, -1, 'Identificador do Ensaio', (198,53), (125,-1), wx.ALIGN_LEFT)
         self.identificador = wx.TextCtrl(self, -1, dadosIniciais[11], (324,50),(141,-1), wx.TE_READONLY | wx.TE_RIGHT)
         self.texto01 = wx.StaticText(self, -1, 'DADOS DA COLETA:',(20,80), (120,-1), wx.ALIGN_LEFT)
         self.texto02 = wx.StaticText(self, -1, 'Data da coleta', (300,83), (75,-1), wx.ALIGN_LEFT)
         self.date = wx.TextCtrl(self, -1, dadosIniciais[10], (380,80),(85,-1), wx.TE_READONLY | wx.TE_LEFT)
         self.texto03 = wx.StaticText(self, -1, 'Local',(130,115), (35,-1), wx.ALIGN_LEFT)
         self.localColeta = wx.TextCtrl(self, -1, dadosIniciais[7], (165,110),(300,-1), wx.TE_READONLY | wx.TE_RIGHT)
         self.texto04 = wx.StaticText(self, -1, 'Operador',(156,143), (55,-1), wx.ALIGN_LEFT)
         self.operador = wx.TextCtrl(self, -1, dadosIniciais[8], (213,140), (252,-1), wx.TE_READONLY | wx.TE_RIGHT)
         self.texto05 = wx.StaticText(self, -1, 'Profundidade (m)',(295,175), (100,-1), wx.ALIGN_LEFT)
         self.profundidade = wx.TextCtrl(self, -1, dadosIniciais[9], (395,170),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
         self.texto06 = wx.StaticText(self, -1, 'DADOS DO ANEL:',(20,200), (100,-1), wx.ALIGN_LEFT)
         self.tipoAnel = wx.TextCtrl(self, -1, dadosIniciais[0], (265,215),(200,-1), wx.TE_READONLY | wx.TE_LEFT)
         self.texto07 = wx.StaticText(self, -1, 'Tipo de Anel',(190,220), (75,-1), wx.ALIGN_LEFT)
         self.diametro = wx.TextCtrl(self, -1, dadosIniciais[1], (395,245),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
         self.texto08 = wx.StaticText(self, -1, 'Diametro Interno (mm)',(265,250), (130,-1), wx.ALIGN_LEFT)
         self.alturaAnel = wx.TextCtrl(self, -1, dadosIniciais[2], (176,245),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
         self.texto09 = wx.StaticText(self, -1, 'Altura (mm)',(105,250), (70,-1), wx.ALIGN_LEFT)
         self.massaAnel = wx.TextCtrl(self, -1, dadosIniciais[3], (395,275),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
         self.texto10 = wx.StaticText(self, -1, 'Massa do Anel (g)',(293,280), (100,-1), wx.ALIGN_LEFT)
         self.texto11 = wx.StaticText(self, -1, 'DADOS DO CORPO-DE-PROVA:',(20,310), (170,-1), wx.ALIGN_LEFT)
         self.alturaCP = wx.TextCtrl(self, -1, dadosIniciais[4], (395,320),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
         self.texto12 = wx.StaticText(self, -1, 'Altura do corpo-de-prova (mm)',(220,325), (170,-1), wx.ALIGN_LEFT)
         self.massaCP = wx.TextCtrl(self, -1, dadosIniciais[6], (395,350),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
         self.texto13 = wx.StaticText(self, -1, 'Massa do corpo-de-prova (g)',(233,355), (155,-1), wx.ALIGN_LEFT)
         self.massaEspecifica = wx.TextCtrl(self, -1, dadosIniciais[5], (395,380),(70,-1),  wx.TE_READONLY | wx.TE_RIGHT)
         self.texto14 = wx.StaticText(self, -1, 'Massa específica dos grãos de solo (g/cm³)',(161,385), (230,-1), wx.ALIGN_LEFT)
         self.texto15 = wx.StaticText(self, -1, 'DADOS DO TEOR DE UMIDADE INICIAL:',(20,415), (230,-1), wx.ALIGN_LEFT)
         self.cap01 = wx.TextCtrl(self, -1, caps[0], (235,435),(70,-1), style = wx.TE_READONLY | wx.TE_LEFT)
         self.cap02 = wx.TextCtrl(self, -1, caps[1], (315,435),(70,-1), style = wx.TE_READONLY | wx.TE_LEFT)
         self.cap03 = wx.TextCtrl(self, -1, caps[2], (395,435),(70,-1), style = wx.TE_READONLY | wx.TE_LEFT)
         self.texto16 = wx.StaticText(self, -1, 'Capsulas',(180,438), (50,-1), wx.ALIGN_LEFT)
         self.massaUmida01 = wx.TextCtrl(self, -1, massaUmida[0], (235,465),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
         self.massaUmida02 = wx.TextCtrl(self, -1, massaUmida[1], (315,465),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
         self.massaUmida03 = wx.TextCtrl(self, -1, massaUmida[2], (395,465),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
         self.texto17 = wx.StaticText(self, -1, 'Massa Úmida (g)',(138,468), (90,-1), wx.ALIGN_LEFT)
         self.massaSeca01 = wx.TextCtrl(self, -1, massaSeca[0], (235,495),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
         self.massaSeca02 = wx.TextCtrl(self, -1, massaSeca[1], (315,495),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
         self.massaSeca03 = wx.TextCtrl(self, -1, massaSeca[2], (395,495),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
         self.texto18 = wx.StaticText(self, -1, 'Massa Seca (g)',(148,495), (80,-1), wx.ALIGN_LEFT)
         self.Editar = wx.Button(self, -1, 'Editar', (188, 534), (112,-1), wx.ALIGN_LEFT)
         self.identificador.SetForegroundColour((119,118,114))
         self.date.SetForegroundColour((119,118,114))
         self.localColeta.SetForegroundColour((119,118,114))
         self.operador.SetForegroundColour((119,118,114))
         self.profundidade.SetForegroundColour((119,118,114))
         self.tipoAnel.SetForegroundColour((119,118,114))
         self.diametro.SetForegroundColour((119,118,114))
         self.alturaAnel.SetForegroundColour((119,118,114))
         self.massaAnel.SetForegroundColour((119,118,114))
         self.alturaCP.SetForegroundColour((119,118,114))
         self.massaCP.SetForegroundColour((119,118,114))
         self.massaEspecifica.SetForegroundColour((119,118,114))
         self.cap01.SetForegroundColour((119,118,114))
         self.cap02.SetForegroundColour((119,118,114))
         self.cap03.SetForegroundColour((119,118,114))
         self.massaUmida01.SetForegroundColour((119,118,114))
         self.massaUmida02.SetForegroundColour((119,118,114))
         self.massaUmida03.SetForegroundColour((119,118,114))
         self.massaSeca01.SetForegroundColour((119,118,114))
         self.massaSeca02.SetForegroundColour((119,118,114))
         self.massaSeca03.SetForegroundColour((119,118,114))
         self.texto1.SetForegroundColour((119,118,114))
         self.texto02.SetForegroundColour((119,118,114))
         self.texto03.SetForegroundColour((119,118,114))
         self.texto04.SetForegroundColour((119,118,114))
         self.texto05.SetForegroundColour((119,118,114))
         self.texto07.SetForegroundColour((119,118,114))
         self.texto08.SetForegroundColour((119,118,114))
         self.texto09.SetForegroundColour((119,118,114))
         self.texto10.SetForegroundColour((119,118,114))
         self.texto12.SetForegroundColour((119,118,114))
         self.texto13.SetForegroundColour((119,118,114))
         self.texto14.SetForegroundColour((119,118,114))
         self.texto16.SetForegroundColour((119,118,114))
         self.texto17.SetForegroundColour((119,118,114))
         self.texto18.SetForegroundColour((119,118,114))
         self.Bind(wx.EVT_BUTTON, self.editarDados, self.Editar)

#---------------------------------------------------------------------------------------------------------------------------------
     def editarDados(self, event):
         id = self.id

         caps = bancodedados.caps(id)
         massaSeca = bancodedados.mSeca(id)
         massaUmida = bancodedados.mUmida(id)
         dadosIniciais = bancodedados.DadosIniciaisParaEdit(id)
         capCadastradas = bancodedados.ler_cap()
         data = datetime.datetime.strptime(dadosIniciais[10], '%d/%m/%Y')
         self.identificador.Destroy()
         self.date.Destroy()
         self.localColeta.Destroy()
         self.operador.Destroy()
         self.profundidade.Destroy()
         self.tipoAnel.Destroy()
         self.diametro.Destroy()
         self.alturaAnel.Destroy()
         self.massaAnel.Destroy()
         self.alturaCP.Destroy()
         self.massaCP.Destroy()
         self.massaEspecifica.Destroy()
         self.cap01.Destroy()
         self.cap02.Destroy()
         self.cap03.Destroy()
         self.massaUmida01.Destroy()
         self.massaUmida02.Destroy()
         self.massaUmida03.Destroy()
         self.massaSeca01.Destroy()
         self.massaSeca02.Destroy()
         self.massaSeca03.Destroy()
         self.Editar.Destroy()
         self.identificador = wx.TextCtrl(self, -1, dadosIniciais[11], (324,50),(141,-1), wx.TE_RIGHT)
         self.identificador.SetMaxLength(10)
         self.date = wx.adv.DatePickerCtrl(self, -1, data, (380,80), size=wx.DefaultSize, style = wx.adv.DP_SHOWCENTURY | wx.adv.DP_DROPDOWN, validator=wx.DefaultValidator, name="datectrl")
         self.localColeta = wx.TextCtrl(self, -1, dadosIniciais[7], (165,110),(300,-1), wx.TE_RIGHT)
         self.localColeta.SetMaxLength(40)
         self.operador = wx.TextCtrl(self, -1, dadosIniciais[8], (213,140), (252,-1), wx.TE_RIGHT)
         self.operador.SetMaxLength(40)
         self.profundidade = wx.TextCtrl(self, -1, dadosIniciais[9], (395,170),(70,-1), wx.TE_RIGHT)
         self.tipoAnel = wx.ComboBox(self, -1, dadosIniciais[0], (265,215),(200,-1), choices = ('Anel fixo', 'Anel flutuante'))
         self.diametro = wx.TextCtrl(self, -1, dadosIniciais[1], (395,245),(70,-1), wx.TE_RIGHT)
         self.alturaAnel = wx.TextCtrl(self, -1, dadosIniciais[2], (176,245),(70,-1), wx.TE_RIGHT)
         self.massaAnel = wx.TextCtrl(self, -1, dadosIniciais[3], (395,275),(70,-1), wx.TE_RIGHT)
         self.alturaCP = wx.TextCtrl(self, -1, dadosIniciais[4], (395,320),(70,-1), wx.TE_RIGHT)
         self.massaCP = wx.TextCtrl(self, -1, dadosIniciais[6], (395,350),(70,-1), wx.TE_RIGHT)
         self.massaEspecifica = wx.TextCtrl(self, -1, dadosIniciais[5], (395,380),(70,-1), wx.TE_RIGHT)
         self.capsulaComboBox01 = wx.ComboBox(self, -1, caps[0], (235,435),(70,-1), capCadastradas)
         self.capsulaComboBox02 = wx.ComboBox(self, -1, caps[1], (315,435),(70,-1), capCadastradas)
         self.capsulaComboBox03 = wx.ComboBox(self, -1, caps[2], (395,435),(70,-1), capCadastradas)
         self.massaUmida01 = wx.TextCtrl(self, -1, massaUmida[0], (235,465),(70,-1), wx.TE_RIGHT)
         self.massaUmida02 = wx.TextCtrl(self, -1, massaUmida[1], (315,465),(70,-1), wx.TE_RIGHT)
         self.massaUmida03 = wx.TextCtrl(self, -1, massaUmida[2], (395,465),(70,-1), wx.TE_RIGHT)
         self.massaSeca01 = wx.TextCtrl(self, -1, massaSeca[0], (235,495),(70,-1), wx.TE_RIGHT)
         self.massaSeca02 = wx.TextCtrl(self, -1, massaSeca[1], (315,495),(70,-1), wx.TE_RIGHT)
         self.massaSeca03 = wx.TextCtrl(self, -1, massaSeca[2], (395,495),(70,-1), wx.TE_RIGHT)
         self.Salvar = wx.Button(self, -1, 'Salvar', (188, 534), (112,-1), wx.ALIGN_LEFT)
         self.identificador.SetForegroundColour((0,0,0))
         self.localColeta.SetForegroundColour((0,0,0))
         self.operador.SetForegroundColour((0,0,0))
         self.profundidade.SetForegroundColour((0,0,0))
         self.massaEspecifica.SetForegroundColour((0,0,0))
         self.massaUmida01.SetForegroundColour((0,0,0))
         self.massaUmida02.SetForegroundColour((0,0,0))
         self.massaUmida03.SetForegroundColour((0,0,0))
         self.massaSeca01.SetForegroundColour((0,0,0))
         self.massaSeca02.SetForegroundColour((0,0,0))
         self.massaSeca03.SetForegroundColour((0,0,0))
         self.texto1.SetForegroundColour((0,0,0))
         self.texto02.SetForegroundColour((0,0,0))
         self.texto03.SetForegroundColour((0,0,0))
         self.texto04.SetForegroundColour((0,0,0))
         self.texto05.SetForegroundColour((0,0,0))
         self.texto07.SetForegroundColour((0,0,0))
         self.texto08.SetForegroundColour((0,0,0))
         self.texto09.SetForegroundColour((0,0,0))
         self.texto10.SetForegroundColour((0,0,0))
         self.texto12.SetForegroundColour((0,0,0))
         self.texto13.SetForegroundColour((0,0,0))
         self.texto14.SetForegroundColour((0,0,0))
         self.texto16.SetForegroundColour((0,0,0))
         self.texto17.SetForegroundColour((0,0,0))
         self.texto18.SetForegroundColour((0,0,0))
         self.Bind(wx.EVT_BUTTON, self.salvarDados, self.Salvar)
         self.Update()
         self.Refresh()

#---------------------------------------------------------------------------------------------------------------------------------
     def salvarDados(self, event):
         id = self.id
         capCadastradas = bancodedados.ler_cap()
         identificadoresCaddastrados = bancodedados.ler_IDE()
         identificadorDoEnsaio = bancodedados.ler_DO_IDE(id)
         a = self.date.GetValue()
         b = self.localColeta.GetValue()
         c = self.operador.GetValue()
         d = self.profundidade.GetValue()
         d = format(d).replace(',','.')
         e = self.tipoAnel.GetValue()
         f = self.diametro.GetValue()
         f = format(f).replace(',','.')
         g = self.alturaAnel.GetValue()
         g = format(g).replace(',','.')
         h = self.massaAnel.GetValue()
         h = format(h).replace(',','.')
         i = self.alturaCP.GetValue()
         i = format(i).replace(',','.')
         j = self.massaCP.GetValue()
         j = format(j).replace(',','.')
         k = self.massaEspecifica.GetValue()
         k = format(k).replace(',','.')
         l = self.capsulaComboBox01.GetValue()
         m = self.capsulaComboBox02.GetValue()
         n = self.capsulaComboBox03.GetValue()
         o = self.massaUmida01.GetValue()
         o = format(o).replace(',','.')
         p = self.massaUmida02.GetValue()
         p = format(p).replace(',','.')
         q = self.massaUmida03.GetValue()
         q = format(q).replace(',','.')
         r = self.massaSeca01.GetValue()
         r = format(r).replace(',','.')
         s = self.massaSeca02.GetValue()
         s = format(s).replace(',','.')
         t = self.massaSeca03.GetValue()
         t = format(t).replace(',','.')
         u1 = self.identificador.GetValue()

         try:
             if d!= '':
                 d = float(d)

         except ValueError:
             menssagError = wx.MessageDialog(self, 'O valor digitado para profundidade deve ser um valor real', 'EAU', wx.OK|wx.ICON_INFORMATION)
             aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
             menssagError.ShowModal()
             menssagError.Destroy()
             d = -1

         try:
             f = float(f)
             g = float(g)
             h = float(h)
             i = float(i)
             j = float(j)
             k = float(k)
             o = float(o)
             p = float(p)
             q = float(q)
             r = float(r)
             s = float(s)
             t = float(t)

         except ValueError:
             print('Algum valor nao e esparado')
             f = -1

         if  e == 'Anel fixo' or  e == 'Anel flutuante':
            if d>=0 and f>0 and g>0 and h>0 and i>0 and j>0 and k>0 and o>0 and p>0 and q>0 and r>0 and s>0 and t>0:
                if f!= '' and g!= '' and h!= '' and i!= '' and j!= '' and k!= '' and o!= '' and p!= '' and q!= '' and r!= '' and  s!= '' and t!= '' and l!= ''  and m!= '' and n!= '':
                    if l in capCadastradas and m in capCadastradas and n in capCadastradas and l!= m and l!= n and m!= n:
                        if u1 in identificadoresCaddastrados and u1!= identificadorDoEnsaio[0]:
                            print('Ja existe esse identificador')
                            menssagError = wx.MessageDialog(self, 'Já existe um ensaio com esse identificador', 'EAU', wx.OK|wx.ICON_INFORMATION)
                            aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                            menssagError.ShowModal()
                            menssagError.Destroy()
                        else:
                            massaC = h + j
                            dateCol = str(datetime.datetime.strptime(str(a), '%m/%d/%y %H:%M:%S').strftime('%d-%m-%Y'))
                            bancodedados.UpdateDadosEnsaio(id, e, f, g, h, massaC, i, k, dateCol, b, c, d, l, m, n, r, s, t, o, p, q, u1)

                            caps = bancodedados.caps(id)
                            massaSeca = bancodedados.mSeca(id)
                            massaUmida = bancodedados.mUmida(id)
                            dadosIniciais = bancodedados.DadosIniciaisParaEdit(id)
                            self.identificador.Destroy()
                            self.date.Destroy()
                            self.localColeta.Destroy()
                            self.operador.Destroy()
                            self.profundidade.Destroy()
                            self.tipoAnel.Destroy()
                            self.diametro.Destroy()
                            self.alturaAnel.Destroy()
                            self.massaAnel.Destroy()
                            self.alturaCP.Destroy()
                            self.massaCP.Destroy()
                            self.massaEspecifica.Destroy()
                            self.capsulaComboBox01.Destroy()
                            self.capsulaComboBox02.Destroy()
                            self.capsulaComboBox03.Destroy()
                            self.massaUmida01.Destroy()
                            self.massaUmida02.Destroy()
                            self.massaUmida03.Destroy()
                            self.massaSeca01.Destroy()
                            self.massaSeca02.Destroy()
                            self.massaSeca03.Destroy()
                            self.Salvar.Destroy()
                            self.identificador = wx.TextCtrl(self, -1, dadosIniciais[11], (324,50),(141,-1), wx.TE_READONLY | wx.TE_RIGHT)
                            self.date = wx.TextCtrl(self, -1, dadosIniciais[10], (380,80),(85,-1), wx.TE_READONLY | wx.TE_LEFT)
                            self.localColeta = wx.TextCtrl(self, -1, dadosIniciais[7], (165,110),(300,-1), wx.TE_READONLY | wx.TE_RIGHT)
                            self.operador = wx.TextCtrl(self, -1, dadosIniciais[8], (213,140), (252,-1), wx.TE_READONLY | wx.TE_RIGHT)
                            self.profundidade = wx.TextCtrl(self, -1, dadosIniciais[9], (395,170),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
                            self.tipoAnel = wx.TextCtrl(self, -1, dadosIniciais[0], (265,215),(200,-1), wx.TE_READONLY | wx.TE_LEFT)
                            self.diametro = wx.TextCtrl(self, -1, dadosIniciais[1], (395,245),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
                            self.alturaAnel = wx.TextCtrl(self, -1, dadosIniciais[2], (176,245),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
                            self.massaAnel = wx.TextCtrl(self, -1, dadosIniciais[3], (395,275),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
                            self.alturaCP = wx.TextCtrl(self, -1, dadosIniciais[4], (395,320),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
                            self.massaCP = wx.TextCtrl(self, -1, dadosIniciais[6], (395,350),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
                            self.massaEspecifica = wx.TextCtrl(self, -1, dadosIniciais[5], (395,380),(70,-1),  wx.TE_READONLY | wx.TE_RIGHT)
                            self.cap01 = wx.TextCtrl(self, -1, caps[0], (235,435),(70,-1), style = wx.TE_READONLY | wx.TE_LEFT)
                            self.cap02 = wx.TextCtrl(self, -1, caps[1], (315,435),(70,-1), style = wx.TE_READONLY | wx.TE_LEFT)
                            self.cap03 = wx.TextCtrl(self, -1, caps[2], (395,435),(70,-1), style = wx.TE_READONLY | wx.TE_LEFT)
                            self.massaUmida01 = wx.TextCtrl(self, -1, massaUmida[0], (235,465),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
                            self.massaUmida02 = wx.TextCtrl(self, -1, massaUmida[1], (315,465),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
                            self.massaUmida03 = wx.TextCtrl(self, -1, massaUmida[2], (395,465),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
                            self.massaSeca01 = wx.TextCtrl(self, -1, massaSeca[0], (235,495),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
                            self.massaSeca02 = wx.TextCtrl(self, -1, massaSeca[1], (315,495),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
                            self.massaSeca03 = wx.TextCtrl(self, -1, massaSeca[2], (395,495),(70,-1), wx.TE_READONLY | wx.TE_RIGHT)
                            self.Editar = wx.Button(self, -1, 'Editar', (188, 534), (112,-1), wx.ALIGN_LEFT)
                            self.identificador.SetForegroundColour((119,118,114))
                            self.date.SetForegroundColour((119,118,114))
                            self.localColeta.SetForegroundColour((119,118,114))
                            self.operador.SetForegroundColour((119,118,114))
                            self.profundidade.SetForegroundColour((119,118,114))
                            self.tipoAnel.SetForegroundColour((119,118,114))
                            self.diametro.SetForegroundColour((119,118,114))
                            self.alturaAnel.SetForegroundColour((119,118,114))
                            self.massaAnel.SetForegroundColour((119,118,114))
                            self.alturaCP.SetForegroundColour((119,118,114))
                            self.massaCP.SetForegroundColour((119,118,114))
                            self.massaEspecifica.SetForegroundColour((119,118,114))
                            self.cap01.SetForegroundColour((119,118,114))
                            self.cap02.SetForegroundColour((119,118,114))
                            self.cap03.SetForegroundColour((119,118,114))
                            self.massaUmida01.SetForegroundColour((119,118,114))
                            self.massaUmida02.SetForegroundColour((119,118,114))
                            self.massaUmida03.SetForegroundColour((119,118,114))
                            self.massaSeca01.SetForegroundColour((119,118,114))
                            self.massaSeca02.SetForegroundColour((119,118,114))
                            self.massaSeca03.SetForegroundColour((119,118,114))
                            self.texto1.SetForegroundColour((119,118,114))
                            self.texto02.SetForegroundColour((119,118,114))
                            self.texto03.SetForegroundColour((119,118,114))
                            self.texto04.SetForegroundColour((119,118,114))
                            self.texto05.SetForegroundColour((119,118,114))
                            self.texto07.SetForegroundColour((119,118,114))
                            self.texto08.SetForegroundColour((119,118,114))
                            self.texto09.SetForegroundColour((119,118,114))
                            self.texto10.SetForegroundColour((119,118,114))
                            self.texto12.SetForegroundColour((119,118,114))
                            self.texto13.SetForegroundColour((119,118,114))
                            self.texto14.SetForegroundColour((119,118,114))
                            self.texto16.SetForegroundColour((119,118,114))
                            self.texto17.SetForegroundColour((119,118,114))
                            self.texto18.SetForegroundColour((119,118,114))
                            self.Update()
                            self.Refresh()
                            self.Bind(wx.EVT_BUTTON, self.editarDados, self.Editar)
                    else:
                        print('O nome de uma das capsulas ou nao esta cadastrada ou nao foi informada ou e identica a outra')
                        menssagError = wx.MessageDialog(self, 'O nome de uma das cápsulas ou não está cadastrada ou não foi informada corretamente ou pode ter duas cápsulas idênticas', 'EAU', wx.OK|wx.ICON_INFORMATION)
                        aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                        menssagError.ShowModal()
                        menssagError.Destroy()
                else:
                    print('Algum dos campos esta vazio')
                    menssagError = wx.MessageDialog(self, 'Algum dos campos prioritários pode não ter sido preenchido', 'EAU', wx.OK|wx.ICON_INFORMATION)
                    aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                    menssagError.ShowModal()
                    menssagError.Destroy()
            else:
                print('Algum dos campos esta digitado errado')
                menssagError = wx.MessageDialog(self, 'Algum dos campos têm a prioridade de salvar valores maiores do que zero', 'EAU', wx.OK|wx.ICON_INFORMATION)
                aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
                menssagError.ShowModal()
                menssagError.Destroy()
         else:
            print('Veja se voce prencheu o tipo de de anel')

#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
class Page02(wx.Panel):

#---------------------------------------------------------------------------------------------------------------------------------
     def __init__(self, parent, id):
         super(Page02, self).__init__(parent)
         self.id = id


         try:
             id_Estagio = bancodedados.ler_quant_estagios_no_ensaio(id)
             list_estagios = bancodedados.ComboEstagios(id)
             rows = bancodedados.TabelaEstagio(id, id_Estagio)
             pre = bancodedados.Pressao(id, id_Estagio)
             statusEst = bancodedados.StatuStagio(id, id_Estagio)

             self.FontTitle =wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
             self.title = wx.StaticText(self, -1, 'DADOS COLETADOS', (20,20), (460,-1), wx.ALIGN_CENTER)
             self.title.SetFont(self.FontTitle)
             self.text00 = wx.StaticText(self, -1, "STATUS ESTÁGIO:", (255,94), (100,-1), wx.ALIGN_LEFT)
             self.ComboEstagios = wx.ComboBox(self, -1, list_estagios[id_Estagio-1], (20,50),(220,-1), list_estagios)
             self.Coletar = wx.Button(self, -1, 'Coletar', (255, 160), (215,-1), wx.ALIGN_LEFT)
             self.texto01 = wx.StaticText(self, -1, 'Pressão Aplicada (kPa)',(255,124), (125,-1), wx.ALIGN_LEFT)
             self.pressaoA = wx.TextCtrl(self, -1, pre[0], (380,120),(90,-1), wx.TE_READONLY | wx.TE_RIGHT)

             self.list_ctrl = wx.ListCtrl(self, size = (220,460), pos = (20,90), style =  wx.LC_REPORT | wx.BORDER_SUNKEN | wx.LC_HRULES | wx.LC_VRULES)
             self.list_ctrl.InsertColumn(0, "Tempo (s)", width=100)
             self.list_ctrl.InsertColumn(1, "Altura (mm)", width=110)

             self.list_ctrl.SetForegroundColour((119,118,114))
             self.pressaoA.SetForegroundColour((119,118,114))
             self.texto01.SetForegroundColour((119,118,114))
             self.Bind(wx.EVT_COMBOBOX, self.EstagioVisualizacao, self.ComboEstagios)

             if statusEst == 0:
                 self.text02 = wx.StaticText(self, -1, "Concluído", (355,94), (80,-1), wx.ALIGN_LEFT)
                 self.text02.SetForegroundColour('green')
                 self.Coletar.SetForegroundColour((119,118,114))

             else:
                 self.text02 = wx.StaticText(self, -1, "Incompleto", (355,94), (80,-1), wx.ALIGN_LEFT)
                 self.text02.SetForegroundColour('red')
                 self.Coletar.SetForegroundColour((0,0,0))
                 self.list_ctrl.SetForegroundColour((0,0,0))
                 self.pressaoA.SetForegroundColour((0,0,0))
                 self.texto01.SetForegroundColour((0,0,0))
                 self.Bind(wx.EVT_BUTTON, self.Coleta, self.Coletar)

             index = 0
             for row in rows:
                 self.list_ctrl.InsertItem(index, row[0])
                 self.list_ctrl.SetItem(index, 1, row[1])
                 index += 1
         except:
             self.text = wx.StaticText(self, -1, "Nenhum coleta foi realizada ainda.", (0,20), (500,-1), wx.ALIGN_CENTER)
             self.Coletar1 = wx.Button(self, -1, 'Coletar', (205, 40), (90,-1), wx.ALIGN_LEFT)
             self.Bind(wx.EVT_BUTTON, self.ColetaDados, self.Coletar1)
#---------------------------------------------------------------------------------------------------------------------------------
     def EstagioVisualizacao(self, event):
         id = self.id
         id_Estagio = self.ComboEstagios.GetValue()
         id_Estagio = int(re.sub('[^0-9]', '', id_Estagio))

         rows = bancodedados.TabelaEstagio(id, id_Estagio)
         pre = bancodedados.Pressao(id, id_Estagio)
         statusEst = bancodedados.StatuStagio(id, id_Estagio)

         self.list_ctrl.Destroy()
         self.pressaoA.Destroy()
         self.pressaoA = wx.TextCtrl(self, -1, pre[0], (380,120),(90,-1), wx.TE_READONLY | wx.TE_RIGHT)
         self.pressaoA.SetForegroundColour((119,118,114))
         self.list_ctrl = wx.ListCtrl(self, size = (220,460), pos = (20,90), style =  wx.LC_REPORT | wx.BORDER_SUNKEN | wx.LC_HRULES | wx.LC_VRULES)
         self.list_ctrl.InsertColumn(0, "Tempo (s)", width=100)
         self.list_ctrl.InsertColumn(1, "Altura (mm)", width=110)
         self.list_ctrl.SetForegroundColour((119,118,114))
         self.list_ctrl.Update()

         if statusEst == 0:
            self.text02.Destroy()
            self.Coletar.Destroy()
            self.Coletar = wx.Button(self, -1, 'Coletar', (255, 160), (215,-1), wx.ALIGN_LEFT)
            self.text02 = wx.StaticText(self, -1, "Concluído", (355,94), (80,-1), wx.ALIGN_LEFT)
            self.text02.SetForegroundColour('green')
            self.Coletar.SetForegroundColour((119,118,114))

         else:
            self.text02.Destroy()
            self.Coletar.Destroy()
            self.text02 = wx.StaticText(self, -1, "Incompleto", (355,94), (80,-1), wx.ALIGN_LEFT)
            self.text02.SetForegroundColour('red')
            self.Coletar = wx.Button(self, -1, 'Coletar', (255, 160), (215,-1), wx.ALIGN_LEFT)
            self.Coletar.SetForegroundColour((0,0,0))
            self.list_ctrl.SetForegroundColour((0,0,0))
            self.pressaoA.SetForegroundColour((0,0,0))
            self.texto01.SetForegroundColour((0,0,0))
            self.Bind(wx.EVT_BUTTON, self.Coleta, self.Coletar)

         index = 0
         for row in rows:
             self.list_ctrl.InsertItem(index, row[0])
             self.list_ctrl.SetItem(index, 1, row[1])
             index += 1

#---------------------------------------------------------------------------------------------------------------------------------
     def Coleta(self, event):
         id = self.id
         print("OLA")


#---------------------------------------------------------------------------------------------------------------------------------
     def ColetaDados(self, event):
         id = self.id
         con = Coleta02(id)
         resultado = con.Show()
#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------
class Page03(wx.Panel):

#---------------------------------------------------------------------------------------------------------------------------------
     def __init__(self, parent, id):
         super(Page03, self).__init__(parent)
         self.id = id

##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
