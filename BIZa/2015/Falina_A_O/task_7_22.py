# Задача 7. Вариант 22.

# Создайте игру, в которой компьютер загадывает имена двух братьев, легендарных основателей Рима, а игрок должен его угадать.

# Falina A. O.

# 15.09.2016

import random
NAME = ("Рем","Ромул")
clas = random.choice(NAME)
print("Угадайте имя одного из братьев")
nam = input("\nВведите имя")
ochko = 2000
while nam != clas:
	if nam == clas:
		print(ochko)
	else:
		print("Неверный ответ.")
		nam = input("Попробуйте еще раз ")
		ochko = ochko/2
print("Поздравляем, вы угадали. Вы получаете",ochko , "очков")
input("\nНажмите Enter, чтобы выйти")