import PySimpleGUI as psg

txtName = psg.Text('Name')
txtAddr = psg.Text('Address')
txtContact = psg.Text('Contact')
inName = psg.Input()
inAddr = psg.Input()
inContact = psg.Input()
btOk = psg.OK()
btCancel = psg.Cancel()

layout = [
    [txtName, inName],
    [txtAddr, inAddr],
    [txtContact, inContact],
    [btOk,btCancel]
]
window = psg.Window(title='Form', layout=layout, size=(450,150))
event,values = window.read()
print(event,values)
window.close()