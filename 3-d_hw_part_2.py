x = [i for i in range(1, 10)]
y = [i for i in range(1, 10)]

for i in range(9):
    print()
    for j in range(9):
        print(x[i], '*', y[j], '=', x[i] * y[j])
