from PySimpleGUI import PySimpleGUI as sg 

import tkinter

# tema
sg.theme('Reddit')
# layout
layout = [

    [sg.Text('Modalidade',size=(10,0)),sg.Text('FAST',size=(10,0)),sg.Text('NORMAL')],

    [sg.Text('MDR Débito',size=(10,0)),sg.Input(key='mdr_debito_fast',size=(10,0)),sg.Input(key='mdr debito normal',size=(10,0))],
    [sg.Text('MDR Crédito',size=(10,0)),sg.Input(key='mdr credito fast',size=(10,0)),sg.Input(key='mdr_credito_normal',size=(10,0))],
    [sg.Text('MDR 2a6X',size=(10,0)),sg.Input(key='mdr 2a6x fast',size=(10,0)),sg.Input(key='mdr 2a6x normal',size=(10,0))],
    [sg.Text('MDR 7a12X',size=(10,0)),sg.Input(key='mdr 7a12x fast',size=(10,0)),sg.Input(key='mdr 7a12x normal',size=(10,0))],
    [sg.Text('RAV',size=(10,0)),sg.Input(key='rav fast',size=(10,0)),sg.Input(key='rav_normal',size=(10,0))],

    [sg.Text('Modalidade',size=(10,0)),sg.Text('FAST',size=(10,0)),sg.Text('NORMAL')],

    [sg.Text('Débito',size=(10,0)),sg.Input(key='mdr_debito_fast',size=(10,0)),sg.Input(key='debito normal',size=(10,0))],
    [sg.Text('Crédito',size=(10,0)),sg.Input(key='credito fast',size=(10,0)),sg.Input(key='credito normal',size=(10,0))],
    [sg.Text('Parc. 2X',size=(10,0)),sg.Input(key='2x fast',size=(10,0)),sg.Input(key='2x normal',size=(10,0))],
    [sg.Text('Parc. 3X',size=(10,0)),sg.Input(key='3x fast',size=(10,0)),sg.Input(key='3x normal',size=(10,0))],
    [sg.Text('Parc. 4X',size=(10,0)),sg.Input(key='4x fast',size=(10,0)),sg.Input(key='4x normal',size=(10,0))],
    [sg.Text('Parc. 5X',size=(10,0)),sg.Input(key='5x fast',size=(10,0)),sg.Input(key='5x normal',size=(10,0))],
    [sg.Text('Parc. 6X',size=(10,0)),sg.Input(key='6x fast',size=(10,0)),sg.Input(key='6x normal',size=(10,0))],
    [sg.Text('Parc. 7x',size=(10,0)),sg.Input(key='7x fast',size=(10,0)),sg.Input(key='7x normal',size=(10,0))],
    [sg.Text('Parc. 8x',size=(10,0)),sg.Input(key='8x fast',size=(10,0)),sg.Input(key='8x normal',size=(10,0))],
    [sg.Text('Parc. 9x',size=(10,0)),sg.Input(key='9x fast',size=(10,0)),sg.Input(key='9x normal',size=(10,0))],
    [sg.Text('Parc. 10x',size=(10,0)),sg.Input(key='10x fast',size=(10,0)),sg.Input(key='10x normal',size=(10,0))],
    [sg.Text('Parc. 11x',size=(10,0)),sg.Input(key='11x fast',size=(10,0)),sg.Input(key='11x normal',size=(10,0))],
    [sg.Text('Parc. 12x',size=(10,0)),sg.Input(key='12x fast',size=(10,0)),sg.Input(key='12x normal',size=(10,0))]
]
# window
janela = sg.Window('CALCULADORA FINANCEIRA', layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
