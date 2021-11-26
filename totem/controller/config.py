import os.path
from dataclasses import dataclass, astuple

import pickle
from pathlib import Path

from controller.utils import get_mac_address

BASE_DIR = Path(__file__).resolve().parent.parent
FILE_NAME = 'data.pickle'


@dataclass
class ConfigModel:
    blur: int = 150
    cam: int = 0
    debug: bool = True
    engine: str = 'tensors'
    mac: str = get_mac_address()
    password: str = '1234'
    register: bool = False
    server: str = 'http://localhost:8000'

    def __iter__(self):
        return iter(astuple(self))


class ConfigController:
    location = os.path.join(BASE_DIR, FILE_NAME)

    def __init__(self, window):
        self.window = window

        try:
            with open(self.location, 'rb+') as file:
                self.config: ConfigModel = pickle.load(file)
        except FileNotFoundError:
            self.config: ConfigModel = ConfigModel()

        self.headers = {
            'x-mac-address': self.config.mac,
            'content-type': 'image/jpeg'
        }

    def load(self):
        self.window['-BLUR SLIDER-'].update(self.config.blur)
        self.window['-CAM INPUT-'].update(self.config.cam)
        self.window['-MAC INPUT-'].update(self.config.mac)
        self.window['-PASSWORD INPUT-'].update(self.config.password)
        self.window['-SERVER INPUT-'].update(self.config.server)

        if self.config.debug:
            self.window['-CHECK DEBUG-'].update(True)

        if self.config.engine == 'tensors':
            self.window['-RADIO TENSORS-'].update(True)
        else:
            self.window['-RADIO CASCADE-'].update(True)

        if self.config.register:
            self.window['-CHECK REGISTER-'].update(True)

    def save(self, values):
        self.config.blur = values['-BLUR SLIDER-']
        self.config.cam = values['-CAM INPUT-']
        self.config.debug = values['-CHECK DEBUG-']
        self.config.engine = 'tensors' if values['-RADIO TENSORS-'] else 'cascade'
        self.config.mac = values['-MAC INPUT-']
        self.config.password = values['-PASSWORD INPUT-']
        self.config.register = values['-CHECK REGISTER-']
        self.config.server = values['-SERVER INPUT-']

        self.dump()

    def dump(self):
        with open(self.location, 'wb+') as file:
            pickle.dump(self.config, file, protocol=pickle.HIGHEST_PROTOCOL)
