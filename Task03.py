# Создайте программу для игры в ""Крестики-нолики"".

import random


def choice_of_move(x):
    if x == 1:
        while True:
            print('Куда вы хотите поставить крестик?')
            choise_line = input('Введите номер строки (1-3): ')
            choise_column = input('Введите номер стобца (1-3): ')
            if choise_line.isdigit() and choise_column.isdigit():
                if 1 <= int(choise_line) <= 3 and 1 <= int(choise_column) <= 3:
                    if playing_field[int(choise_line)-1][int(choise_column)-1] == ' ':
                        playing_field[int(choise_line) - 1][int(choise_column) - 1] = 'X'
                        break
                    elif playing_field[int(choise_line)-1][int(choise_column)-1] == 'X':
                        print('Здесь уже стоит крестик')
                    else:
                        print('Здесь уже стоит нолик')
                else:
                    print('Числа не находится в диапазоне от 1 до 3')
            else:
                print('Вы ввели не числа')
    else:
        while True:
            print('Куда вы хотите поставить нолик?')
            choise_line = input('Введите номер строки (1-3): ')
            choise_column = input('Введите номер стобца (1-3): ')
            if choise_line.isdigit() and choise_column.isdigit():
                if 1 <= int(choise_line) <= 3 and 1 <= int(choise_column) <= 3:
                    if playing_field[int(choise_line) - 1][int(choise_column) - 1] == ' ':
                        playing_field[int(choise_line) - 1][int(choise_column) - 1] = '0'
                        break
                    elif playing_field[int(choise_line) - 1][int(choise_column) - 1] == '0':
                        print('Здесь уже стоит нолик')
                    else:
                        print('Здесь уже стоит крестик')
                else:
                    print('Числа не находится в диапазоне от 1 до 3')
            else:
                print('Вы ввели не числа')


print('Перед вами примитивная игра в крестики-нолики')
playing_field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print(playing_field[0])
print(playing_field[1])
print(playing_field[2])
name_first_player = input('Введите имя первого игрока: ')
name_second_player = input('Введите имя второго игрока: ')
lottery = random.randint(1, 2)
if lottery == 1:
    print(f'{name_first_player}, ваш ход первый. Вы будете ходить крестиками.')
    choice_of_move(lottery)
    print(playing_field[0])
    print(playing_field[1])
    print(playing_field[2])
    lottery = 2
else:
    print(f'{name_second_player}, ваш ход первый. Вы будете ходить ноликами.')
    choice_of_move(lottery)
    print(playing_field[0])
    print(playing_field[1])
    print(playing_field[2])
    lottery = 1
for i in range(9):
    if lottery == 2:
        print(f'{name_second_player}, теперь ваш ход')
        choice_of_move(lottery)
        lottery = 1
        print(playing_field[0])
        print(playing_field[1])
        print(playing_field[2])
        if playing_field[0][0] == '0' and playing_field[0][1] == '0' and playing_field[0][2] == '0':
            print(f'{name_second_player} Победитель!')
            break
        elif playing_field[1][0] == '0' and playing_field[1][1] == '0' and playing_field[1][2] == '0':
            print(f'{name_second_player} Победитель!')
            break
        elif playing_field[2][0] == '0' and playing_field[2][1] == '0' and playing_field[2][2] == '0':
            print(f'{name_second_player} Победитель!')
            break
        elif playing_field[0][0] == '0' and playing_field[1][0] == '0' and playing_field[2][0] == '0':
            print(f'{name_second_player} Победитель!')
            break
        elif playing_field[0][1] == '0' and playing_field[1][1] == '0' and playing_field[2][1] == '0':
            print(f'{name_second_player} Победитель!')
            break
        elif playing_field[0][2] == '0' and playing_field[1][2] == '0' and playing_field[2][2] == '0':
            print(f'{name_second_player} Победитель!')
            break
        elif playing_field[0][0] == '0' and playing_field[1][1] == '0' and playing_field[2][2] == '0':
            print(f'{name_second_player} Победитель!')
            break
        elif playing_field[0][2] == '0' and playing_field[1][1] == '0' and playing_field[2][0] == '0':
            print(f'{name_second_player} Победитель!')
            break
    else:
        print(f'{name_first_player}, теперь ваш ход')
        choice_of_move(lottery)
        lottery = 2
        print(playing_field[0])
        print(playing_field[1])
        print(playing_field[2])
        if playing_field[0][0] == 'X' and playing_field[0][1] == 'X' and playing_field[0][2] == 'X':
            print(f'{name_first_player} Победитель!')
            break
        elif playing_field[1][0] == 'X' and playing_field[1][1] == 'X' and playing_field[1][2] == 'X':
            print(f'{name_first_player} Победитель!')
            break
        elif playing_field[2][0] == 'X' and playing_field[2][1] == 'X' and playing_field[2][2] == 'X':
            print(f'{name_first_player} Победитель!')
            break
        elif playing_field[0][0] == 'X' and playing_field[1][0] == 'X' and playing_field[2][0] == 'X':
            print(f'{name_first_player} Победитель!')
            break
        elif playing_field[0][1] == 'X' and playing_field[1][1] == 'X' and playing_field[2][1] == 'X':
            print(f'{name_first_player} Победитель!')
            break
        elif playing_field[0][2] == 'X' and playing_field[1][2] == 'X' and playing_field[2][2] == 'X':
            print(f'{name_first_player} Победитель!')
            break
        elif playing_field[0][0] == 'X' and playing_field[1][1] == 'X' and playing_field[2][2] == 'X':
            print(f'{name_first_player} Победитель!')
            break
        elif playing_field[0][2] == 'X' and playing_field[1][1] == 'X' and playing_field[2][0] == 'X':
            print(f'{name_first_player} Победитель!')
            break
