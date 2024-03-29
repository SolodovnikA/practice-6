k = int(input('Введите количество суши: '))

if k % 5 == 0 or k % 7 == 0 or ((k - 5) % 7 == 0) or ((k - 7) % 5 == 0):
    print('да')
else:
    print('нет')
