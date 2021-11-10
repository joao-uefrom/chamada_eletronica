from . import sg, FONT_FAMILY

__title = [[sg.Text('Configurações', font=f'{FONT_FAMILY} 16 bold')]]

layout = sg.Column(
    [
        [sg.Frame('', __title, expand_x=True, element_justification='center')],
        [sg.Text('Endereço MAC:', size=(14, 1)), sg.Input(key='-MAC INPUT-', disabled=True)],
        [sg.Text('Índice da Câmera:', size=(14, 1)), sg.Input(key='-CAM INPUT-')],
        [sg.Text('Senha:', size=(14, 1)), sg.Input(key='-PASSWORD INPUT-')],
        [sg.Text('End. do servidor:', size=(14, 1)), sg.Input(key='-SERVER INPUT-')],
        [
            sg.Text('Sens. ao blur:', size=(14, 1)),
            sg.Slider(range=(50, 500), orientation='h', key='-BLUR SLIDER-')
        ],
        [sg.Frame('', [
            [sg.Text('Motor de processamento:')],
            [sg.Radio('Classificador em Cascata', 'engine', key='-RADIO CASCADE-')],
            [sg.Radio('Tensores', 'engine', key='-RADIO TENSORS-')],
        ], expand_x=True)],
        [sg.Frame('', [[
            sg.Text('Modo de Cadastro:'), sg.Checkbox('Ativado?', tooltip='Marque para Ativar', key='-CHECK REGISTER-')
        ]], expand_x=True)],
        [sg.Frame('', [[
            sg.Text('Modo de Debug:'), sg.Checkbox('Ativado?', tooltip='Marque para Ativar', key='-CHECK DEBUG-')
        ]], expand_x=True)],
        [sg.Text('', expand_y=True)],
        [
            sg.Button('Desligar', expand_x=True, font=f'{FONT_FAMILY} 16 bold', key='-EXIT-'),
            sg.Button('Salvar', expand_x=True, font=f'{FONT_FAMILY} 16 bold', key='-SAVE CONFIG-')
        ]
    ], expand_y=True, expand_x=True, visible=False, key='-CONFIG SCREEN-'
)
