from . import sg, FONT_FAMILY, IMAGE_BLANK_PROFILE

__title = [[sg.Text('CADASTRO', font=f'{FONT_FAMILY} 16 bold')]]

__video_capture = [[sg.Image(IMAGE_BLANK_PROFILE, key='-VIDEO CAPTURE REGISTER-')]]

layout = sg.Column(
    [
        [sg.Frame('', __title, expand_x=True, element_justification='center')],
        [sg.Column(__video_capture)],
        [
            sg.Button('Pular', expand_x=True, font=f'{FONT_FAMILY} 16 bold', disabled=True, key='-BUTTON SKIP-'),
            sg.Button('Adicionar', expand_x=True, font=f'{FONT_FAMILY} 16 bold', disabled=True, key='-BUTTON ADD-')
        ],
        [sg.Button('Finalizar', expand_x=True, font=f'{FONT_FAMILY} 16 bold', key='-REGISTER COMPLETED-')]
    ], element_justification='center', expand_y=True, expand_x=True, visible=False, key='-REGISTER SCREEN-'
)
