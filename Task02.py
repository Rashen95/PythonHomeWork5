# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random


def game_mode_f():
    while True:
        game_mode_input = input('Введите 1 если вы хотите играть с '
                                'другом или 2 если хотите играть с ботом: ')
        if game_mode_input == '1' or game_mode_input == '2':
            return int(game_mode_input)
        else:
            print('Вы ввели неверное значение')


def number_of_candies_f():
    while True:
        number_of_candies_input = input('Сколько будет конфет? : ')
        if number_of_candies_input.isdigit():
            if int(number_of_candies_input) > 0:
                return int(number_of_candies_input)
            else:
                print('Вы ввели неверное значение')
        else:
            print('Вы ввели неверное значение')


def amount_of_candy_used_f(x, name):
    while True:
        amount_of_candy_used_input = input(f'{name}, осталось {x} конфет. Сколько конфет возьмете? (не больше 28) : ')
        if amount_of_candy_used_input.isdigit():
            if 28 >= int(amount_of_candy_used_input) > 0:
                if int(amount_of_candy_used_input) <= x:
                    return int(amount_of_candy_used_input)
                else:
                    print(f'Я не могу взять больше чем осталось')
            else:
                print('Вы ввели неверное значение')
        else:
            print('Вы ввели неверное значение')


print('Против кого вы хотите играть?')
game_mode = game_mode_f()
if game_mode == 1:
    print('Вы выбрали режим игры с другом')
    name_first_player = input('Введите имя первого игрока: ')
    name_second_player = input('Введите имя второго игрока: ')
    number_of_candies = number_of_candies_f()
    lottery = random.randint(1, 2)
    if lottery == 1:
        print(f'По результатам жеребьевки первый ход достается игроку с именем {name_first_player}')
    else:
        print(f'По результатам жеребьевки первый ход достается игроку с именем {name_second_player}')
    while number_of_candies > 0:
        if lottery == 1:
            amount_of_candy_used = amount_of_candy_used_f(number_of_candies, name_first_player)
            number_of_candies -= amount_of_candy_used
            lottery = 2
        else:
            amount_of_candy_used = amount_of_candy_used_f(number_of_candies, name_second_player)
            number_of_candies -= amount_of_candy_used
            lottery = 1
    if lottery == 1:
        print(f'Победителем стал игрок c именем {name_second_player}')
    else:
        print(f'Победителем стал игрок c именем {name_first_player}')
else:
    print('Вы выбрали режим игры с ботом')
    name_first_player = input('Введите имя игрока: ')
    number_of_candies = number_of_candies_f()
    lottery = random.randint(1, 2)
    if lottery == 1:
        print(f'По результатам жеребьевки первый ход достается игроку с именем {name_first_player}')
    else:
        print(f'По результатам жеребьевки первый ход достается боту')
    while number_of_candies > 0:
        if lottery == 1:
            amount_of_candy_used = amount_of_candy_used_f(number_of_candies, name_first_player)
            number_of_candies -= amount_of_candy_used
            print(f'Осталось {number_of_candies} конфет')
            lottery = 2
        else:
            if number_of_candies > 28 and number_of_candies % 29 > 0:
                subtrahend = number_of_candies % 29
                number_of_candies -= subtrahend
                print(f'Бот взял {subtrahend} конфет')
            elif number_of_candies > 28 and number_of_candies % 29 == 0:
                number_of_candies -= 1
                print('Бот взял 1 конфет')
            else:
                print(f'Бот взял {number_of_candies} конфет')
                number_of_candies -= number_of_candies
            lottery = 1
    if lottery == 1:
        print(f'Победителем стал бот')
    else:
        print(f'Победителем стал игрок c именем {name_first_player}')
