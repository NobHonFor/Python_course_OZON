while True:
    with open('hw_5.4.txt', 'a', encoding='utf-8') as file:
        file.write(input('Введите число:') + '\n')
        file.write(input('Введите запись:') + '\n')
        file.close()
    desc = input('Продолжить работу с журналом да\нет:')
    if desc == 'нет':
        break
with open('hw_5.4.txt', 'r', encoding='utf-8') as file:
    print('Личный журнал:')
    for line in file:
        print(line)
file.close()