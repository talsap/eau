# -*- coding: utf-8 -*-

'''Bibliotecas'''

import sys
import wx

import front.tela as tela

'''Inicializacao do programa'''
class main():
     app = wx.App()
     tela.Tela(None)
     app.MainLoop()

main()
