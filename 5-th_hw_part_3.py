with open('test.txt', encoding='utf8') as file:
    a = 0
    cnt_var = []
    for line in file.readlines():
        for word in line.split():
            if word == 'кошка':
                cnt_var.append(line)
                a += 1
for i in range(len(cnt_var)):
    if len(cnt_var[i]) != len(cnt_var[i - 1]):
        print(cnt_var[i])
print('Слово "Кошка" встречается в тексте', a)
