﻿#Задача 5. Вариант 24.

#Напишите программу, которая бы при запуске случайным образом отображала название одной из шести шахматных фигур.

#Cheraneva A.S.
#25.03.16

print('\n Программа случайным образом отображает название одной из шести шахматных фигур.')

import random
edin=('Король','Ферзь','Слон','Ладья','Конь','Пешка')
A=random.randint(0,6)
print(edin[A])

input('\n Нажмите enter, чтобы закрыть')