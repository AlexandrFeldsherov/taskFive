# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая
# ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать
# не более чем 28 конфет(или сколько вы зададите). Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import randint
from re import X
import math


def input_int_numbers(number) -> int:
    """
    Проверка целого числа
    """
    index = True
    while index:
        try:
            number = int(number)
            index = False
        except ValueError:
            print("Таким число конфет быть не может.")
            number = input("Попрубуйте ввести число конфет еще раз : ")
            input_int_numbers(number)
    return int(number)


def game_candies(number_candies, queue_players):
    if queue_players == 1:
        number_candies = first_player_go(number_candies)
        queue_players = 0
    else:
        number_candies = second_player_go(number_candies)
        queue_players = 1
    if number_candies <= 0:
        if queue_players==1:
            print("you win")
        else :
            print("you lose")
    else:
            game_candies(number_candies,queue_players)


def first_player_go(number_candies):
    take_you = input("Сколько вы конфет возьмете?\n")
    take_you=input_int_numbers(take_you)
    take_you = control_taken_sweets(take_you,number_candies)
    number_candies = number_candies-take_you
    return number_candies


def second_player_go(number_candies):
    take_second=number_candies%28-1
    if math.trunc(number_candies/28)>0:
        take_second=number_candies%28-2
    if take_second==0:
        take_second=1
    number_candies -= int(take_second)
    print(
        f"Второй игрок взял {take_second}, осталось {number_candies} конфет.")
    return number_candies


def control_taken_sweets(taken_num, number_candies):
    if 0 < taken_num < 29 and taken_num <= number_candies:
        return int(taken_num)
    else:
        taken_num=input("Такое количество конфет вы не можете взять.\n\
        Сколько вы конфет возьмете?\n")
        taken_num=input_int_numbers(taken_num)
        taken_num=control_taken_sweets(taken_num, number_candies)
    return int(taken_num)


number_candies = input("\
            На столе лежат конфеты.\n\
            За один ход можно забрать не более чем 28 конфет.\n\
            Тот, кто берет последнюю конфету - проиграл.\n\
Введите начальное количество конфет : ")
input_int_numbers(number_candies)
game_candies(int(number_candies), queue_players=randint(0,2))

