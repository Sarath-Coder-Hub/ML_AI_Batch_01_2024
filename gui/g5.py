import PySimpleGUI as psg

file_path = psg.popup_get_file('Select a file', title='File Selector')
file = open(file_path)
data = file.read()
psg.popup_scrolled(
    data,
    title='File Content',
    font = ('Calibre', 16),
    size=(50,20)
)
psg.Print(data)
import time
time.sleep(3)