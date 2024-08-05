def calculate_total(**kwargs):
    '''Рассчитывает форму чека'''
    total = 0
    for item, price in kwargs.items():
        total += price
    return total

order_total = calculate_total(apple = 2.3, bananas = 30, pineapple = 27.1)
print('Общая сумма заказа: ', order_total)