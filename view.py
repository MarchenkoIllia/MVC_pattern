import controller

def get_choise():
    return input('Нажмите для продоожения (1): ')

def view_message(mes):
    print(mes)

def get_loop():
    return mainloop

def mainloop():
    while True:
        controller.controller_loop()