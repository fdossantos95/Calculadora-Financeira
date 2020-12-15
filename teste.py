from PySimpleGUI import PySimpleGUI as sg 


# tema
sg.theme('Reddit')
# layout
layout = [
    [sg.Text('Primeiro')],sg.input(key='primeiro')
    [sg.Text('Segundo')],sg.Input(key='segundo')
    []
]
# janela
# ler os eventos