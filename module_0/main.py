import numpy as np
count = 0  # счетчик попыток
number = np.random.randint(1, 101)  # загадали число
print("Загадано число от 1 до 100")


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = 50
    min_predicted_value = 0
    max_predicted_value = 100
    def get_correction_for_predict_value(max_predicted_value, min_predicted_value):
        correction = round((max_predicted_value - min_predicted_value) / 2)
        if correction == 0:
            return 1
        else:
            return correction


    while number != predict:
        count+=1

        if number > predict:
            min_predicted_value = predict + 1
            predict += get_correction_for_predict_value(max_predicted_value, min_predicted_value)
        elif number < predict:
            max_predicted_value = predict - 1
            predict -= get_correction_for_predict_value(max_predicted_value, min_predicted_value)
    return(count) # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


# запускаем
score_game(game_core_v2)