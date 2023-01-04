import controller

def get_choise():
    return input('Играем? 1/2:')

def view_message(mes):
    print(mes)

def get_loop():
    return mainloop

def mainloop():
    while True:
        controller.controllerLoop()