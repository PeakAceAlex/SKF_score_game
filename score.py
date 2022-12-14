import numpy as np

def random_predict(number:int=1) -> int:
    """Угадываем число, проверяя, больше ли искомое число, чем предложенное, или меньше.
     
    Если искомое меньше предложенного, значит 

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    n_min = 0
    n_max = 101
    while True:
        count += 1
        predict_number = n_min + (n_max - n_min)//2 #числа не угадываем случайно, а берем середину диапазона, в котором находится число.
        if number == predict_number:
            break # если угадали, выход из цикла
        elif number > predict_number:
            n_min = predict_number # если искомое число больше предсказания, устанавливаем предсказание, как нижнюю границу диапазона поиска, сужая его таким образом вдвое
        else:
            n_max = predict_number # если искомое число меньше предсказания, устанавливаем предсказание, как верхнюю границу диапазона поиска                
    return(count)

def score_game() -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__=='__main__':
    print (score_game())