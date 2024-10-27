import PySimpleGUI as psg

file_path = psg.popup_get_file('Select a file', title='File Selector')
print(file_path)

folder_path = psg.popup_get_folder('Select a folder', title='Folder Selector')
print(folder_path)
