# Задача 5. Вариант 22.

# Напишите программу, которая бы при запуске случайным образом отображала имя одного из двух сооснователей компании Google.


# Falina A. O.

# 15.09.2016

import random
WORDS = ("Пейдж", "Брин")
word = random.choice(WORDS)
print (word)
input ("\n\nНажмите enter, чтобы выйти")