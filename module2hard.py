res = []
num = 0

while num < 3 or num > 20:
    num = int(input('Введите число от 3 до 20: '))

for i in range(1, 21):
    for j in range(1, 21):
        k = i + j
        if num % k == 0 and i < j:
            res.append(i)
            res.append(j)

result_st = ''.join(map(str, res))
print('Пароль для числа', num, '=', result_st)