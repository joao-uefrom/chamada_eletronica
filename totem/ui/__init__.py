import controller
from .screen import sg
from .screen.config import layout as config
from .screen.debug import layout as debug
from .screen.home import layout as home
from .screen.loading import layout as loading
from .screen.password import layout as password
from .screen.register import layout as register

_layout = [[
    config,
    debug,
    home,
    loading,
    password,
    register
]]

_screens = [
    '-CONFIG SCREEN-',
    '-DEBUG SCREEN-',
    '-HOME SCREEN-',
    '-LOADING SCREEN-',
    '-PASSWORD SCREEN-',
    '-REGISTER SCREEN-'
]

window = sg.Window(
    'Chamada Eletrônica',
    _layout,
    finalize=True,
    grab_anywhere=True,
    # location=(0, 0),
    # margins=(2, 2),
    no_titlebar=True,
    size=(320, 480)
)


def go2(route):
    for _screen in _screens:
        window[_screen].update(visible=False)

    if route == '-HOME SCREEN-':
        controller.detector.start()

    if controller.config.config.debug and route == '-HOME SCREEN-':
        window['-DEBUG SCREEN-'].update(visible=True)

    elif controller.config.config.register and route == '-HOME SCREEN-':
        window['-REGISTER SCREEN-'].update(visible=True)

    else:
        window[route].update(visible=True)
