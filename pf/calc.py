dep = int(input('Введи начальную сумму'))
decr = round(dep / 360, 8)
sum = 0

for i in range(361):
    vipl = round((dep / 100) * 0.7, 8)
    sum += vipl + decr
    dep -= decr
    print(vipl + decr)

print(sum)