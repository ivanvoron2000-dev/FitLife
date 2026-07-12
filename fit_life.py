# вводим переменные
water_per_kg = 30
mil_in_liter = 1000
# запрашиваем данные у пользователя с проверкой,где необходимо
username = input("Как вас зовут?:")
username_in = username

while True:
    try:
        userage = int(input("Сколько вам лет?:"))
        break
    except ValueError:
        print("Ошибка,пожалуйста,попробуйте еще раз в формате: 11 без точек")


while True:
    try:
        user_weight = float(input("Какой у вас вес(кг)?:"))
        break
    except ValueError:
        print("Ошибка,пожалуйста,попробуйте еще раз в формате: 11.1")

while True:
    try:
        user_height = float(input("Какой у вас рост?(в метрах прим:1.75):"))
        break
    except ValueError:
        print("Ошибка,пожалуйста,попробуйте еще раз в формате: 11.1")

# проводим вычисления
bmi = (user_weight / (user_height ** 2))
water_l = (user_weight * water_per_kg) / mil_in_liter
# результат
print(f"\nОтчет для пользователя: {username}, {userage} лет")
print(f"Ваш индекс массы тела состовляет: {round(bmi, 1)}")
print(f"Ваша норма воды в день составляет: {round(water_l, 2)} л. в день\n")
print("Результат готов. Хорошего дня!")
