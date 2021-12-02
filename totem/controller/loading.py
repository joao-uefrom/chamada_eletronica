import requests

from ui.screen import sg


class LoadingController:
    def __init__(self, window, config_controller):
        while True:
            window.read(timeout=100)

            try:
                r = requests.post(config_controller.config.server + '/api/ping', headers=config_controller.headers)
                if r.status_code > 202:
                    raise requests.exceptions.ConnectionError

                break
            except requests.exceptions.ConnectionError:
                window['-LOADING TEXT-'].update('Algo deu errado.')
                window['-LOADING INPUT-'].update(config_controller.config.server)
                window['-LOADING ERROR-'].update(visible=True)

            event, values = window.read()
            if '-EXIT-' in event or event == sg.WIN_CLOSED:
                exit(0)

            window['-LOADING TEXT-'].update('Carregando...')
            window['-LOADING ERROR-'].update(visible=False)

            values['-SERVER INPUT-'] = values['-LOADING INPUT-']
            config_controller.save(values)
