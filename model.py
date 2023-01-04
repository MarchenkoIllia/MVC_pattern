from random import randint

def get_random_value(end=6):
    return randint(1, end)

def get_scores(user_scores, value):
    if value == 6:
        user_scores += 3
        return user_scores
    else:
        user_scores -= 1
        return user_scores
    