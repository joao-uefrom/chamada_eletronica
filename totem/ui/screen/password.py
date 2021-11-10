from . import sg, FONT_FAMILY


def __button(placeholder: str): return sg.Button(
    placeholder,
    font=f'{FONT_FAMILY} 14',
    expand_x=True,
    key=f'-PASSWORD DIGIT {placeholder}-',
    metadata=placeholder
)


__title = [[sg.Text('Digite a senha de acesso', font=f'{FONT_FAMILY} 16 bold')]]

__display_keyboard = [
    [sg.Text('', size=(1, 3))],
    [sg.Text('', size=(18, 1), justification='right', background_color='black', text_color='red',
             font=('Digital-7', 48), relief='sunken', key="-PASSWORD DISPLAY-")],
    [__button('1'), __button('2'), __button('3')],
    [__button('4'), __button('5'), __button('6')],
    [__button('7'), __button('8'), __button('9')],
    [__button('0')],
    [sg.Text('', size=(1, 3))]
]

layout = sg.Column(
    [
        [sg.Frame('', __title, element_justification='center', expand_x=True)],
        [sg.Column(__display_keyboard, expand_x=True, pad=(0, 0))],
        [
            sg.Button('Cancelar', expand_x=True, font=f'{FONT_FAMILY} 16 bold',
                      key='-ROUTE-', metadata='-HOME SCREEN-'),
            sg.Button('Confirmar', expand_x=True, font=f'{FONT_FAMILY} 16 bold',
                      key='-ROUTE-', metadata='-CONFIG SCREEN-')
        ]
    ],
    element_justification='center', expand_x=True, visible=False,
    key='-PASSWORD SCREEN-'
)
