print("Введите названия двух цветов для смешивания: ")
first_color = str(input("Первый цвет: "))
second_color = str(input("Второй цвет: "))

if first_color == 'жёлтый' and second_color == 'красный':
    print('оранжевый')
elif first_color == 'красный' and second_color == 'жёлтый':
    print('оранжевый')

elif first_color == 'синий' and second_color == 'красный':
    print('фиолетовый')
elif first_color == 'красный' and second_color == 'синий':
    print('фиолетовый')

elif first_color == 'жёлтый' and second_color == 'синий':
    print('зелёный')
elif first_color == 'синий' and second_color == 'жёлтый':
    print('зелёный')

else:
    print('Ошибка')