from PySimpleGUI import PySimpleGUI as tema

tema.theme('Default')
layout = [
    [tema.Text('Usuário'), tema.Input(key='usuario',size=(20,1))],
    [tema.Text('Senha  '), tema.Input(key='senha', password_char='*',size=(20,1))],
    [tema.Checkbox('Salvar o usuário?')],
    [tema.Button('Entrar')]
    ]
janela = tema.Window('Login', layout)

while True:
    eventos, valores = janela.read()
    if eventos == tema.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores ['usuario'] == 'Davys' and valores['senha'] == '123456':
            print (f'Bem vindo!')
        else: 
            layout = [
                [tema.Text('Senha ou Login errado')],
                [tema.Text('Usuário'), tema.Input(key='usuario',size=(20,1))],
                [tema.Text('Senha  '), tema.Input(key='senha', password_char='*',size=(20,1))],
                [tema.Checkbox('Salvar o usuário?')],
                [tema.Button('Entrar')]
                ]
            janela = tema.Window('Login', layout)