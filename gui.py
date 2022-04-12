import PySimpleGUI as sg

sg.theme('BluePurple')

layout = [[sg.Text('Escreva abaixo um numero entre 0 e 999:'),
           sg.Text(size=(15, 1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Escrever'), sg.Button('Sair ')]]

