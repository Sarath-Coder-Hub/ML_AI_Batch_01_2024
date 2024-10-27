import PySimpleGUI as psg

#psg.popup('Welcome All')

txt_name = psg.popup_get_text('Enter your Name',
                              title='Name Popup' )

txt_pwd = psg.popup_get_text('Enter your password',
                              title='Password Popup',
                              default_text='',
                              password_char='*')
print(txt_name, txt_pwd)