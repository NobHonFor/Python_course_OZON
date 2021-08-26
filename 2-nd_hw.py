import random

player_deposit = int(10000)
player_choice = int(0)

print('Viva Las Vegas! Ваш депозит составляет', player_deposit, '. Приятной игры!')
while player_deposit != int(0):
    random_number = random.randint(2, 12)
    print(random_number)
    while True:
        try:
            player_choice = int(input('Введите число: '))
            break
        except ValueError:
            print('Для продолжения игры необходимо ввести число от 1 до 12')
            continue
    if player_choice != random_number:
        player_deposit -= 1000
        print('Выпало число', random_number,
              '. К сожалению вы угадали не верно. Попробуйте еще, вам обязательно повезет')
        print('Ваш депозит составляет', player_deposit)
    else:
        player_deposit += 1000
        print('Выпало число', random_number, '. Вы угадали верно. Удача на вашей стороне')
        print('Ваш депозит составляет', player_deposit)
print('Отличная игра!')
