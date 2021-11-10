from . import sg, FONT_FAMILY, IMAGE_BLANK_PROFILE

__title = [[sg.Text('DEBUG', font=f'{FONT_FAMILY} 16 bold')]]

__video_capture = [[sg.Image(IMAGE_BLANK_PROFILE, key='-VIDEO CAPTURE DEBUG-')]]

layout = sg.Column(
    [
        [sg.Frame('', __title, expand_x=True, element_justification='center')],
        [sg.Column(__video_capture)],
        [sg.Button('Menu', size=(999, 20), expand_x=True, key='-ROUTE-', metadata='-PASSWORD SCREEN-')]
    ], element_justification='center', expand_y=True, expand_x=True, visible=False, key='-DEBUG SCREEN-'
)
