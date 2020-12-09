from PySimpleGUI import PySimpleGUI as sg 


# tema
sg.theme('Reddit')
# layout
layout = [
    [sg.Text('Modalidade '),sg.Text('FAST                 '),sg.Text('NORMAL                 ')],
    [sg.Text('MDR Débito '),sg.Input(key='mdr debito fast '),sg.Input(key='mdr debito normal ')],
    [sg.Text('MDR Crédito'),sg.Input(key='mdr credito fast'),sg.Input(key='mdr credito normal')],
    [sg.Text('MDR 2a6X   '),sg.Input(key='mdr 2a6x fast   '),sg.Input(key='mdr 2a6x normal   ')],
    [sg.Text('MDR 7a12X  '),sg.Input(key='mdr 7a12x fast  '),sg.Input(key='mdr 7a12x normal  ')],
    [sg.Text('RAV        '),sg.Input(key='rav fast        '),sg.Input(key='rav normal        ')],
    [sg.Text('Modalidade'), sg.Text('FAST'),                 sg.Text('NORMAL')],
    [sg.Text('Débito'),     sg.Input(key='debito fast'),     sg.Input(key='debito normal')],
    [sg.Text('Crédito'),    sg.Input(key='credito fast'),    sg.Input(key='credito normal')],
    [sg.Text('Parc. 2X'),   sg.Input(key='2x fast'),         sg.Input(key='2x normal')],
    [sg.Text('Parc. 3X'),   sg.Input(key='3x fast'),         sg.Input(key='3x normal')],
    [sg.Text('Parc. 4X'),   sg.Input(key='4x fast'),         sg.Input(key='4x normal')],
    [sg.Text('Parc. 5X'),   sg.Input(key='5x fast'),         sg.Input(key='5x normal')],
    [sg.Text('Parc. 6X'),   sg.Input(key='6x fast'),         sg.Input(key='6x normal')],
    [sg.Text('Parc. 7x'),   sg.Input(key='7x fast'),         sg.Input(key='7x normal')],
    [sg.Text('Parc. 8x'),   sg.Input(key='8x fast'),         sg.Input(key='8x normal')],
    [sg.Text('Parc. 9x'),   sg.Input(key='9x fast'),         sg.Input(key='9x normal')],
    [sg.Text('Parc. 10x'),  sg.Input(key='10x fast'),        sg.Input(key='10x normal')],
    [sg.Text('Parc. 11x'),  sg.Input(key='11x fast'),        sg.Input(key='11x normal')],
    [sg.Text('Parc. 12x'),  sg.Input(key='12x fast'),        sg.Input(key='12x normal')]
]
# window
janela = sg.Window('CALCULADORA FINANCEIRA', layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
