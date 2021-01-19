import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [ [sg.Text('Operação de soma')],
           [sg.Text('Digite o primeiro número:',size=(25,0)), sg.InputText('0',size=(10,0))],
           [sg.Text('Digite o segundo número:',size=(25,0)), sg.InputText('0',size=(10,0))],
           [sg.Button('Ok'), sg.Input(size=(10,0))] ]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

print('You entered ', values[0])
window.close()

