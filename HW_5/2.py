# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""

import random

cons = 100
player_one =lambda:int(input("Введите число от 1 до 28 => "))
bot = lambda: random.randint(1, 28)
voice_you = int(input("Сделайте свой выбор юный герой Орёл или Решка где Орёл это - 1, а Решка это - 2 => "))
voice_destiny = lambda: random.randint(1, 2)

reshka = 'Решка'
orel = 'Орёл'
def gud_luck (random_voice,voice_you):
    a = random_voice()
    if a == voice_you:
        if voice_you == 1:
            return orel
        elif voice_you == 2:
            return reshka
    elif a == 1:
        return orel
    elif a == 2:
        return reshka
a = gud_luck(voice_destiny, voice_you)
print(a)
def player ():
    av = player_one()
    if av <= 28 and av >= 1 :
        return av
    else:
        print('Мошенник')
        return player ()

def game (cons,player):

    print("По правилам игры ход первым за тем у кого выпал Орел")
    if cons > 28:
        while cons >= 28:
            cons -= player()
            player_you = cons
            print(f'{player_you} Ход игрока')
            cons -= bot()
            bot_player = cons
            print(f'{bot_player} Ход бота')
    return cons

def victory (x,luck):
    if x < 28 and luck =='Решка':
        x -= x
        print("Победил бот")
    elif x < 28 and luck =='Орёл':
        print("Победил игрок")
        x -= x
    return x

result = game(cons,player)
print(result)
print(victory (result,a))


