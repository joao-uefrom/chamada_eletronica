class PasswordController:
    __password = ''

    def __init__(self, window, config_controller):
        self.window = window
        self.config_controller = config_controller

    def clean(self):
        self.__password = ''
        self.window['-PASSWORD DISPLAY-'].update('')

    def digit(self, x):
        if len(self.__password) < 4:
            self.__password += x

        display = ''
        for _ in self.__password:
            display += '*'

        self.window['-PASSWORD DISPLAY-'].update(display)

    def valid(self) -> bool:
        return self.config_controller.config.password == self.__password
