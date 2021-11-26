from . import sg, FONT_FAMILY

layout = sg.Column(
    [
        # [sg.Image(GIF_LOADING, key='-LOADING GIF-')],
        [sg.Text('Carregando...', font=f'{FONT_FAMILY} 16 bold', key='-LOADING TEXT-')],
        [sg.Column([
            [sg.Text('Endereço do servidor:')],
            [sg.Input(key='-LOADING INPUT-')],
            [sg.Button('Tentar de novo', expand_x=True, key='-TRY AGAIN-')],
            [sg.Button('Desligar', expand_x=True, key='-EXIT-')]
        ], visible=False, key='-LOADING ERROR-')]
    ], element_justification='center', expand_y=True, expand_x=True, visible=True, key='-LOADING SCREEN-'
)
