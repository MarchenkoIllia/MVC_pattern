import model
import view as v

def controllerLoop():
    user_choise = v.get_choise()
    user_scores = 10
    if user_choise == 1:
        value = model.get_random_value()
        score = model.get_scores(user_scores, value)
        message = model.check_scores(score)
        v.view_message(message)

def main():
    v.view_message('Сыграем в кости? (1): ')
    f = v.get_loop()
    f()

if __name__ == '__main__':
    main()