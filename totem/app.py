import controller
import ui

ui.go2('-HOME SCREEN-')

while True:
    event, values = ui.window.read()

    if '-EXIT-' in event or event == ui.sg.WIN_CLOSED:
        break

    if 'ROUTE' in event:
        controller.detector.release()
        route = ui.window.find_element(event).metadata

        if route == '-HOME SCREEN-':
            controller.password.clean()

        if route == '-CONFIG SCREEN-':
            is_valid = controller.password.valid()
            controller.password.clean()

            if not is_valid:
                continue

        ui.go2(route)

    if 'PASSWORD DIGIT' in event:
        controller.password.digit(ui.window.find_element(event).metadata)

    if event == '-SAVE CONFIG-':
        controller.config.save(values)
        ui.go2('-HOME SCREEN-')

    if event == '-REGISTER COMPLETED-':
        values['-CHECK REGISTER-'] = False
        ui.window['-CHECK REGISTER-'].update(False)
        controller.config.save(values)

        ui.go2('-HOME SCREEN-')

    if event == '-BUTTON ADD-':
        controller.detector.send_register()

    if event == '-BUTTON SKIP-':
        controller.detector.skip_register()

controller.detector.release()
