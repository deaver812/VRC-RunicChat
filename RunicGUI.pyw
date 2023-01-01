import PySimpleGUI as sg
from pythonosc.udp_client import SimpleUDPClient
import time
import runicChat
sg.theme("Dark Blue 3")
layout = [[sg.Text('Previously Typed:'), sg.Text(size=(12,1), key='-Prev-')],
          [sg.Text('Previous Runes:'), sg.Text(size=(12,1), key='-PrevRunes-')],
          [sg.Input(key='-IN-')],
          [sg.Radio("Greek Letters", "RADIO1", default=True, key="greek")],
          [sg.Radio("Runic Letters", "RADIO1", default=False)],
          [sg.Button('Send'), sg.Button('Exit')]]
alphabet = "abcdefghijklmnopqrstuvwxyz.!?"
number="0123456789"

window = sg.Window("RunicGUI", layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    event, values=window.read()
    if (values["greek"])==True:
        runes="ᚨᛒᛍᛞᛖᚬᚵᚺᛁᛃᚴᛚᛗᚾᛟᛕᛩᚱᛋᛏᛝᛡᚧᛪᛨᛄ᛫᛭᛭"
    else:
        runes="ᚨᛒᛍᛞᛖᚬᚵᚺᛁᛃᚴᛚᛗᚾᛟᛕᛩᚱᛋᛏᛝᛡᚧᛪᛨᛄ᛫᛭᛭"
    if event == 'Send':
        
        window['-Prev-'].update(values['-IN-'])
        string, userInput=window["-IN-"]#this is not a string causing an error
        runeTable = userInput.maketrans(alphabet, runes, number)
        runicInput = userInput.translate(runeTable)
        window["-PrevRunes-"].update(values[runicInput])
window.close()
