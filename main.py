# Программа угадай число.
import random as r
secretNumber = r.randint(1, 100)
print('Добро пожаловать в числовую угадайку! \nПопробуй угадать целое число от 1 до 100, которое я загадал!:\n')

def is_valid(s): #Проверка на "дурака".
    return s.isdigit() and 1 <= int(s) <= 100

while True:
    your_num = input()
    if is_valid(your_num) == True:
        your_num = int(your_num)
        if your_num < secretNumber:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif your_num > secretNumber:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')