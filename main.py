print("Первый вариант")
hour = int(input("Введите время: "))
if (hour >= 8 and hour < 10) or (hour >= 12 and hour < 14) or (hour >= 15 and hour < 18) or (hour >= 20 and hour < 22):
    print("Можно получить посылку")
else:
    print("Посылку получить нельзя")


print("Второй вариант")
hour1 = int(input("Введите время: "))
if (hour1 >= 0 and hour < 8) or (hour1 >= 10 and hour <= 12) or (hour1 >= 14 and hour <= 15) or (
        hour1 >= 18 and hour <= 20) or (hour1 >= 22 and hour1 <= 24):
    print('Посылку получить нельзя')
else:
    print("Можно получить посылку")
