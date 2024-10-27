import PySimpleGUI as psg
import time
#while True:
ch = psg.popup_yes_no('Do you wish to continue ?',title='YesNo')
print(ch)
#    if ch != None:break
ch = psg.popup_ok_cancel('Do you wish to continue ?',title='OkCancel')
print(ch)
time.sleep(2)
psg.popup_no_buttons('You Pressed', ch, non_blocking=False)
psg.popup_auto_close('You Pressed', ch)