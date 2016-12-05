# Задача 8. Вариант 22. 
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

# Falina A. O. 
# 10.11.2016

import random
slova = ("груша", "яблоко", "картофель", "помидор", "капуста", "банан")
word = random.choice(slova)
verno = word
nz = "?"
podskazka = word[:3]

ann = ""
while word:
    poz = random.randrange(len(word))
    ann = ann + word[poz]
    word = word[:poz] + word[(poz + 1):]

score = 10
print("Добро пожаловать в игру 'Анаграммы!'")
print("Надо переставить буквы так, чтобы получилось осмысленное слово.")
print("Если вам нужна подсказка, то просто напишите: '?' ")
print("За использование подсказки вы потеряйте 5 очков.")
print("Для выхода нажмите Enter, не вводя своей версии.")

print("\nВот анаграмма: ",ann)
variant = input("\nПопробуйте отгадать исходое слово: ")
while variant != "" and variant != verno:
    if variant == "":
        print("ujdyj")
    if variant != verno and variant != nz:
        print("Вы не угадали. ")
        variant = input("\nПопробуйте еще раз: ")
    if variant == nz:
        score -= 5
        print("\nПервые три буквы слова: ",podskazka)
        variant = input("Попробуйте еще раз: ")
    if variant == verno:
        print("\n Поздравляю! Вы отгадали")

print("Спасибо за игру! У вас", score, "очков")
input("\nДля выхода нажмите Enter") 

