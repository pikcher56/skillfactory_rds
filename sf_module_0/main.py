import numpy as np


def game_score_v2(number):
    count = 0
    # нижняя граница диапазона преполагаемых значений
    min_range_bound = 0
    # верхняя граница диапазона преполагаемых значений
    max_range_bound = 100

    while True:
        # счетчик попыток
        count += 1
        # преполагаемое число
        # изменение медианы диапазона
        # присваиваем преполагаемому числу значение равное середине диапазона
        # сам диапазон каждую итерацию делится пополам
        # и становится в 2 раза меньше
        predict = middle_value = (max_range_bound + min_range_bound) // 2
        if number < middle_value:
            # Если угадываемое число меньше
            # верхня граница диапазона изменяется на значение середины текущего диапазона
            max_range_bound = middle_value
        else:
            # если угадываемое число больше
            # нижняя граница диапазона изменяется на значение середины текущего диапазона
            min_range_bound = middle_value

        # защита от зацикливания
        if count == 20:
            break
        # Если угадали, то выход из цикла while
        if number == predict:
            break
    return count


def score_game(game_score):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 100, size=1000)
    for number in random_array:
        count_ls.append(game_score(number))
    score = int(np.mean(count_ls))
    print(f"Average score = {score}")
    return score


number = np.random.randint(1, 100)
score_game(game_score_v2)


#
#
# Для проверки и отладки
#
# number = 27
# game_score_v2(number)


# count = 0
# number = np.random.randint(1, 100)
#
# while True:
#     predict = int(input("Введите число: "))
#     count += 1
#     if number == predict:
#         break
#     elif number > predict:
#         print(f"Угадываемое число больше {predict}")
#     elif number < predict:
#         print(f"Угадываемое число меньше {predict}")
#
# print(f"Вы угадали число {number} за {count} поппыток.")
