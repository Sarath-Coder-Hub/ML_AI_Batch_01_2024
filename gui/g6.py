import PySimpleGUI as psg

layout = [
    [psg.Text(
            text='Hello World',
            font=('Calibre', 14),
            justification='center',
            expand_x=True
        )],
    [psg.Button('OK')]
]
window = psg.Window(title='Sample Window', layout=layout, size=(500,200),resizable=True)
while True:
    event,values = window.read()
    print(event, values)
    if event in (None,'Exit'): break
    if event == 'OK': psg.popup('OK')
window.close()