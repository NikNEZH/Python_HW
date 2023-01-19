# Создайте программу для игры в ""Крестики-нолики"".

border = list(range(1,10))

def coub (border):
    print('-' * 13)
    for i in range(3):
        print('|', border[0+i*3],'|', border[1+i*3],'|', border[2+i*3],'|')
        print('-' * 13)

def take(player_token):
    valid = False
    while not  valid:
        player_answer = input("Выбери куда поставить" + player_token)
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректные данные")
            continue
        if player_answer >=1 and player_answer <=9:
            if (str(border[player_answer-1]) not in "XO"):
                border[player_answer-1] = player_token
                valid = True
            else:print('Занята клетка')
        else:print("введите число от 1 до 9")

def check_victory(border):
    vic_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in vic_coord:
        if border[i[0]] == border[i[1]] == border[i[2]]:
            return border[i[0]]
    return False

def main (border):
    counter = 0
    vic = False
    while not vic:
        coub(border)
        if counter % 2 ==0:
            take("X")
        else: take("O")
        counter += 1
        if counter > 4:
            tmp = check_victory(border)
            if tmp:
                print(tmp, "Ты выиграл")
                vic = True
                break
        if counter == 9:
            print("Ничья")
            break
    coub(border)
main(border)