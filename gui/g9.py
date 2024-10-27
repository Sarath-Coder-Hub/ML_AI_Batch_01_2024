import PySimpleGUI as psg
txtTile = psg.Text('User Details', font=('Calibre', 20),
                   expand_x=True, justification='center')
txtName = psg.Text('Name', size=(15,1))
txtAddr = psg.Text('Address',  size=(15,1))
txtContact = psg.Text('Contact',  size=(15,1))
inName = psg.Input(expand_x=True)
inAddr = psg.Input(expand_x=True)
inContact = psg.Input(expand_x=True)
btOk = psg.OK()
btCancel = psg.Cancel()

layout = [
    [txtTile],
    [txtName, inName],
    [txtAddr, inAddr],
    [txtContact, inContact],
    [btOk,btCancel]
]
window = psg.Window(title='Form', layout=layout, size=(450,210), resizable=True)
while True:
    event,values = window.read()
    print(event,values)
    if event in (None, 'Cancel', psg.WIN_CLOSED):
        break
    if event == 'OK':
        msg = f'{values[0]}, {values[1]}, {values[2]}'
        psg.popup(msg)
window.close()