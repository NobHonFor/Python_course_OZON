string1 = 'Съешь еще этих мягких французских булок ДА выпей же чаю'

print(string1.split(" ")[3].upper())
print(string1.split(" ")[6].lower())
print(string1.split(" ")[7][2])

for i in range(len(string1.split(" "))):
    print(string1.split(" ")[i])
