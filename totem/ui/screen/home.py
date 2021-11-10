from . import sg, FONT_FAMILY, IMAGE_BLANK_PROFILE

__title = [[sg.Text('Chamada Eletrônica', font=f'{FONT_FAMILY} 16 bold', key='-STATUS TEXT-')]]

__information = [
    [sg.Text('Aluno: ', size=(7,)), sg.Text('', size=(999,), key='-STUDENT NAME-')],
    [sg.Text('Matrícula: ', size=(7,)), sg.Text('', size=(999,), key='-STUDENT ENROLMENT-')],
    [sg.Text('Turma: ', size=(7,)), sg.Text('', size=(999,), key='-STUDENT CLASS-')],
]

layout = sg.Column(
    [
        [sg.Frame('', __title, expand_x=True, element_justification='center')],
        [sg.Image(IMAGE_BLANK_PROFILE, size=(250, 250), key='-VIDEO CAPTURE-')],
        [sg.Frame('Informações', __information, expand_x=True, expand_y=True)],
        [sg.Button('Menu', size=(999, 48), expand_x=True, key='-ROUTE-', metadata='-PASSWORD SCREEN-')]
    ], element_justification='center', expand_y=True, expand_x=True, visible=False, key='-HOME SCREEN-'
)
