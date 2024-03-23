a, b = map(int, input('Введите размер отверстия: ').split('x'))
c, d, e = map(int, input('Введите размер кирпича: ').split('x'))

brick_v = [c, d, e]
brick_v.remove(max(brick_v))

brick_s = brick_v[0]*brick_v[1]

if (a * b) > brick_s:
    print('Да')
else:
    print('Нет')