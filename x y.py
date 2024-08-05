x = int(input('Введите значение x: '))
y = int(input('Введите значение y: '))
if x > 0 and y > 0:
    print("Первая четверть")
if x > 0 and y < 0:
    print("Четвертая четверть")
if x < 0 and y < 0:
    print("Третья четверть")
if x < 0 and y > 0:
    print("Вторая четверть")
