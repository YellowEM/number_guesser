# Программа угадай число.
import random as r
secretNumber = r.randint(1, 100)
print('Добро пожаловать в числовую угадайку! \nПопробуй угадать целое число от 1 до 100, которое я загадал!:\n')

def is_valid(s): #Проверка на "дурака".
    return s.isdigit() and 1 <= int(s) <= 100
total = 0
while True:
    your_num = input()
    if is_valid(your_num) == True:
        your_num = int(your_num)
        if your_num < secretNumber:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            total += 1
        elif your_num > secretNumber:
            print('Ваше число больше загаданного, попробуйте еще разок')
            total += 1
        else:
            total += 1
            print('Вы угадали, поздравляем! \nЧисло попыток: ' + str(total))
            break
print('Спасибо, что играли в числовую угадайку. Для рестарта нажми ...')
#Создать функцию для реиграбельности
#Попробовать задать количество попыток заранее (7 попыток максимум)
#print('Давайте решим в каком диапозоне будем угадывать')
