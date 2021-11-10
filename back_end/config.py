import os.path
from configparser import ConfigParser
from pathlib import Path
from typing import Union


def config(option: str = None, section: str = None) -> Union[str, dict]:
    parser = ConfigParser()
    parser.read(os.path.join(Path(__file__).resolve().parent, 'config.ini'))
    default_section = 'DEFAULT'

    if section is None:
        if parser.has_option(default_section, option):
            return parser[default_section][option]
        else:
            raise Exception(f'Opção {option} não encontrada na seção {default_section}.')

    if option is None:
        data = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                data[param[0]] = param[1]

            return data
        else:
            raise Exception(f'Seção {section} não encontrada.')

    if parser.has_option(section, option):
        return parser[section][option]

    raise Exception(f'Opção {option} não encontrada.')
