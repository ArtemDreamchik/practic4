number = int(input("Введите номер места: "))
if 1 <= number <= 36:
    if number % 2 == 0:
        print("Верхнее в купе")
    else:
        print("Нижнее в купе")
elif 37 <= number <= 52:
    if number % 2 == 0:
        print("Верхнее сбоку")
    else:
        print("Нижнее сбоку")
else:
    print("Такого места нет в вагоне")