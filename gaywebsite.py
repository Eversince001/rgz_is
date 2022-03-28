from email import message
from tkinter import messagebox
import PySimpleGUI as sg
import re


layout = [
    [sg.Text("Введите утверждение на английском языке: ", text_color='black'), sg.Input(size=(30, 1), key='input')],
    [sg.Button("      Перевести в вопросительную форму     ", key = 'Подтвердить'), sg.MLine(size=(30, 1), key='output')],
    [sg.Exit()]
]

window = sg.Window("Экспертная система", layout)

while True: 
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event in (None, 'Exit'):
        break
    elif event in ('Подтвердить'):
        window['output'].Update('')
        text = values['input']
        if (re.search(r"[a-zA-Z]",text) and not re.search(r"[а-яА-Я0-9]",text)):
            if(len(text) > 0):
                words = text.split() 
                if(words[1].lower() == 'is'):
                    text = 'Is' + " " + words[0].lower() + " "
                    for i in range(2, len(words)):
                        if (i != len(words) - 1):
                            text += words[i] + " " 
                        else:
                            text += words[i]
                    text.strip()
                    window['output'].print(text + "?")

                elif(words[1].lower() == 'am'):
                    text = 'Am' + " " + words[0] + " "
                    for i in range(2, len(words)):
                        if (i != len(words) - 1):
                            text += words[i] + " " 
                        else:
                            text += words[i]
                    text.strip()
                    window['output'].print(text + "?")

                elif(words[1].lower() == 'are'):
                    text = 'Are' + " " + words[0].lower() + " "
                    for i in range(2, len(words)):
                        if (i != len(words) - 1):
                            text += words[i] + " " 
                        else:
                            text += words[i]
                    text.strip()
                    window['output'].print(text + "?")

                
        else:
            messagebox.showerror(title=None, message="Сообщение содержит кириллицу или цифры")

    