def calculate_price(price, discount_percent=0, is_VIP=False):
    '''
    price - цена
    discount_percent - процент скидки (по умолчанию 0)
    is_VIP - является ли покупатель vip-клиентом (по умолчанию - нет)
    '''
    if is_VIP is True:
        result = (price / 100) * (100 - (discount_percent + 5))
    else:
        result = (price / 100) * (100 - discount_percent)
    
    return result

price1 = calculate_price(100, 10, True)
price2 = calculate_price(120, 12)
price3 = calculate_price(150, is_VIP=True)
print(price1)
print(price2)
print(price3)