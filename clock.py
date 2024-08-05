def calc_time(*args): 
    all = sum(args)
    hours = all // 60
    minutes = all % 60
    time = (hours, minutes)
    return time

print(calc_time(15, 20, 25, 10))
