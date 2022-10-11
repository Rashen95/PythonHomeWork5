# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

text1 = 'aaaaab33333eeeeeeeeeeeeeeeeeeeeeeeeeeeeeekkkkwwwwweeee'
text2 = ''
text3 = ''
count = 1
for i in range(len(text1)):
    if i + 1 == len(text1):
        text2 += f'{count}{text1[i]}'
        count += 1
    elif text1[i] == text1[i+1]:
        count += 1
    else:
        while count > 9:
            text2 += f'9{text1[i]}'
            count -= 9
        text2 += f'{count}{text1[i]}'
        count = 1
print('Исходные данные')
print(text1)
print()
print('Сжатые данные')
print(text2)
print()
print('Восстановленные данные')
for i in range(0, len(text2), 2):
    text3 += f'{int(text2[i]) * text2[i+1]}'
print(text3)
