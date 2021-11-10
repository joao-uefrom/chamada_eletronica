import requests

from ui.screen import sg


class LoadingController:
    def __init__(self, window, config_controller):
        while True:
            window.read(timeout=100)

            try:
                headers = {
                    'x-mac-address': config_controller.config.mac,
                    'content-type': 'image/jpeg'
                }

                r = requests.post(config_controller.config.server + '/api/ping', headers=headers)
                if r.status_code > 202:
                    raise requests.exceptions.ConnectionError

                break
            except requests.exceptions.ConnectionError:
                window['-LOADING TEXT-'].update('Algo deu errado.')
                window['-LOADING INPUT-'].update(config_controller.config.server)
                window['-LOADING ERROR-'].update(visible=True)

            event, values = window.read()
            if event == '-EXIT-' or event == sg.WIN_CLOSED:
                exit(0)

            window['-LOADING TEXT-'].update('Carregando...')
            window['-LOADING ERROR-'].update(visible=False)

            config_controller.config.server = values['-LOADING INPUT-']
            config_controller.save(values)
