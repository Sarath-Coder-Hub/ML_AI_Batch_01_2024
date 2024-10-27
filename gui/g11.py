#Elements combo
import PySimpleGUI as psg
dataset = ['Apple', 'Mango']
nameCB = psg.Combo(dataset, expand_x=True, enable_events=True, readonly=False, key='-NAMECB-')
addBT = psg.Button('Add')
removeBT = psg.Button('Remove')
txtInfo = psg.Text("", key='-INFO-', justification='left', expand_x=True)
layout = [
    [nameCB, addBT, removeBT],
    [txtInfo]
]
window = psg.Window(title='Combo Test', layout=layout, size=(700,200))
while True:
    event,values = window.read()
    if event in (None, psg.WIN_CLOSED):
        break
    if event == 'Add':
        v = values['-NAMECB-']
        dataset.append(v)
        window['-NAMECB-'].update(values=dataset, value='')
        window['-INFO-'].update(f'A new item added {v}')
    if event == 'Remove':
        v = values['-NAMECB-']
        try:
            dataset.remove(v)
            window['-NAMECB-'].update(values=dataset, value='')
            window['-INFO-'].update(f'An item removed {v}')
        except:
            window['-INFO-'].update(f'Item not removed {v}')

window.close()