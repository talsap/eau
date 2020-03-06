# -*- coding: utf-8 -*-

'''Bibliotecas'''

import wx
from coleta03 import Coleta03
from ColetaStatusManual import ColetaStatusManual

'''Tela De dialogo Se a coleta vai ser MANUAL ou AUTOMATICA'''
class ColetaStatus(wx.Dialog):

    def __init__(self, id, id_Estagio, *args, **kwargs):
        wx.Dialog.__init__(self, None, -1, 'EAU - Coleta de Dados', style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        self.id = id
        self.id_Estagio = id_Estagio

        self.InitUI()
        self.SetSize((350, 300))
        self.Centre()
        self.SetTitle("Estágio " + str(self.id_Estagio))

    def InitUI(self):

        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        sb = wx.StaticBox(pnl, label='')
        sbs = wx.StaticBoxSizer(sb, orient=wx.VERTICAL)
        sbs.Add(wx.StaticText(pnl, label='', style=wx.ALIGN_LEFT))
        sbs.Add(wx.StaticText(pnl, label='PARA COLETAR O ÚLTIMO DADO, EXISTE...', style=wx.ALIGN_LEFT))
        sbs.Add(wx.StaticText(pnl, label='', style=wx.ALIGN_LEFT))
        sbs.Add(wx.StaticText(pnl, label='MODO AUTOMÁTICO:', style=wx.ALIGN_LEFT))
        sbs.Add(wx.StaticText(pnl, label='Coleta o dado automaticamente de acordo com a hora do', style=wx.ALIGN_LEFT))
        sbs.Add(wx.StaticText(pnl, label='sistema.', style=wx.ALIGN_LEFT))
        sbs.Add(wx.StaticText(pnl, label='Atenção com o data/hora do sistema!', style=wx.ALIGN_LEFT))
        sbs.Add(wx.StaticText(pnl, label='', style=wx.ALIGN_LEFT))
        sbs.Add(wx.StaticText(pnl, label='MODO MANUAL:', style=wx.ALIGN_LEFT))
        sbs.Add(wx.StaticText(pnl, label='O dado é preenchido manualmente pelo usuário de acordo', style=wx.ALIGN_LEFT))
        sbs.Add(wx.StaticText(pnl, label='com o horário em que terminou o ensaio.', style=wx.ALIGN_LEFT))
        sbs.Add(wx.StaticText(pnl, label='Atenção com o horário em que foi iniciado o ensaio!', style=wx.ALIGN_LEFT))

        pnl.SetSizer(sbs)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        automaticoButton = wx.Button(self, label='AUTOMÁTICO')
        manualButton = wx.Button(self, label='MANUAL')
        hbox1.Add(automaticoButton)
        hbox1.Add(manualButton, flag=wx.LEFT, border=5)

        vbox.Add(pnl, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)
        vbox.Add(hbox1, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

        self.SetSizer(vbox)

        automaticoButton.Bind(wx.EVT_BUTTON, self.OnAutomatico)
        manualButton.Bind(wx.EVT_BUTTON, self.OnManual)


    def OnAutomatico(self, e):
        id = self.id
        id_Estagio = self.id_Estagio
        menssagError = wx.MessageDialog(self, 'COLETA AUTOMÁTICA SÓ NA PRÓXIMA VERSÃO!', 'EAU', wx.OK|wx.ICON_INFORMATION)
        aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
        menssagError.ShowModal()
        menssagError.Destroy()

        '''con = Coleta03(id, id_Estagio)
        resultado = con.Show()
        self.GetTopLevelParent().Close(True)'''
        #terminar na próxima versão, testar coleta de ultimo dado com o arduino

    def OnManual(self, e):
        id = self.id
        id_Estagio = self.id_Estagio
        menssagError = wx.MessageDialog(self, 'COLETA MANUAL SÓ NA PRÓXIMA VERSÃO!', 'EAU', wx.OK|wx.ICON_INFORMATION)
        aboutPanel = wx.TextCtrl(menssagError, -1, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
        menssagError.ShowModal()
        menssagError.Destroy()

        '''con = ColetaStatusManual(id, id_Estagio)
        resultado = con.Show()
        self.GetTopLevelParent().Close(True)'''
        #terminar na próxima versão, testar o EditableListCtrl
