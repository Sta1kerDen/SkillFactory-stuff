def xwin(n):
    '''Проверяет соблюдены ли условия для победы x'''
    first = n[10], n[12], n[14]
    second = n[18], n[20], n[22]
    third = n[26], n[28], n[30]
    forth = n[10], n[20], n[30]
    fifth = n[14], n[20], n[26]
    sixth = n[10], n[18], n[26]
    seventh = n[12], n[20], n[28]
    eighth = n[14], n[22], n[30]

    list_of_cond = (first, second, third, forth, fifth, sixth, seventh, eighth)
    for i in list_of_cond:
        if ''.join(i) == 'xxx':
            return True