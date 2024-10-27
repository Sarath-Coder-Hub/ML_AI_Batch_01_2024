import PySimpleGUI as psg
txtTile = psg.Text('User Details', font=('Calibre', 20),
                   expand_x=True, justification='center')
txtName = psg.Text('Name', size=(15,1))
txtAddr = psg.Text('Address',  size=(15,1))
txtContact = psg.Text('Contact',  size=(15,1))
txtMsg = psg.Text('MSG:', key='-MSG-', expand_x=True)
inName = psg.Input(key='-NAME-', expand_x=True)
inAddr = psg.Input(key='-ADDR-', expand_x=True)
inContact = psg.Input(key='-CNT-', expand_x=True, enable_events=True)
btOk = psg.OK()
btCancel = psg.Cancel()

layout = [
    [txtTile],
    [txtName, inName],
    [txtAddr, inAddr],
    [txtContact, inContact],
    [txtMsg],
    [btOk,btCancel]
]
window = psg.Window(title='Form', layout=layout, size=(450,210), resizable=True)
while True:
    event,values = window.read()
    print(event,values)
    if event in (None,  psg.WIN_CLOSED):  break
    if event == 'OK':
        msg = f"{values['-NAME-']}, {values['-ADDR-']}, {values['-CNT-']}"
        #psg.popup(msg)
        window['-MSG-'].update(msg)
    if event == 'Cancel':
        window['-NAME-'].update('')
        window['-ADDR-'].update('')
        window['-CNT-'].update('')
    if event == '-CNT-':
        vl = values['-CNT-']
        if vl[-1] not in ('0123456789'):
            window['-CNT-'].update(vl[:-1])
window.close()