# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'стол абвал абв кровать аБвес абварка абв абв швабра человекабв насос приабвет АБВадакедавра'
list_text = text.split(' ')
list_text_without_abv = []
for i in range(len(list_text)):
    for j in range(len(list_text[i]) - 2):
        if list_text[i][j:j + 3].lower() == 'абв':
            break
        if j == len(list_text[i]) - 3:
            list_text_without_abv.append(list_text[i])
text = ' '.join(list_text_without_abv)
print(text)
