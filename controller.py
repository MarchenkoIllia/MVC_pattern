import model
import view2 as v

score = 10
def controller_loop():
    global score
    user_choise = v.get_choise()
    if user_choise == '1':
        value = model.get_random_value()
        score = model.get_scores(score, value)
        message, result = model.check_scores(score)
        v.view_message(message)
    else:
        v.view_message('Введено неверное значение')

def main():
    v.view_message('Сыграем в кости?')
    result = False
    f = v.get_loop()
    f()

if __name__ == '__main__':
    main()