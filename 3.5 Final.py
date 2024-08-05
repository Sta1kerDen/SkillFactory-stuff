T = int(input('Введите Температуру на улице: '))
Rain = bool(input('Есть ли осадки? '))
Rain_strong = bool(input('Осадки сильные? '))
if 30 > T > 20:
    if Rain == True:
        print('Футболку, шорты и дожевик')
    if Rain == False:
        print('Футболку и шорты')
if T < 20 or T > 30:
    if T < 0:
        print('Пуховик')
    if T > 0:
        if Rain == False:
            print('Пальто')
        if Rain == True:
            if Rain_strong == False:
                print('Пальто и дождевик')
            if Rain_strong == True:
                print('Пальто, резиновые сапоги и зонт')