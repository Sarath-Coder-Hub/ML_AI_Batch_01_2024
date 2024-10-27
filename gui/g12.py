#checkbox and radio
import PySimpleGUI as psg

txtName = psg.Text('Enter Name')
inName = psg.Input("", key='-INNAME-')

txtCompany = psg.Text('Company', expand_x=True, font=('Arial Bold', 12))
rbCompany = []
rbCompany.append(psg.Radio('Company1', 'company', key='-C1-',default=True))
rbCompany.append(psg.Radio('Company2', 'company', key='-C2-'))
rbCompany.append(psg.Radio('Company3', 'company', key='-C3-'))

txtQualification = psg.Text('Qualification', expand_x=True, font=('Arial Bold', 12))
cbQualification = []
cbQualification.append(psg.Checkbox('+2', key='-Q1-'))
cbQualification.append(psg.Checkbox('UG', key='-Q2-'))
cbQualification.append(psg.Checkbox('PG', key='-Q3-'))

opIn = psg.Multiline("", expand_x=True, key = '-OUT-', expand_y=True, justification='left')
btOk = psg.Ok()
layout = [
    [txtName, inName],
    [txtCompany],
    [ rbCompany],
    [txtQualification],
    [cbQualification],
    [btOk],
    [opIn]
]
window = psg.Window(title='Test', layout=layout, size=(700,200), resizable=True )
while True:
    event, values = window.read()
    if event in (None, psg.WIN_CLOSED):
        break
    if event == 'Ok':
        name = values['-INNAME-']
        cmp =[x.Text for x in rbCompany if x.get()==True][0]
        qlf = [x.Text for x in cbQualification if x.get() == True]

        msg = f"""Name:{name}\nCompany:{cmp}\nQualification:{','.join(qlf)}"""
        window['-OUT-'].update(msg)

window.close()
