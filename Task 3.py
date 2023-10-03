n = int(input())

def change_type(n, sp): #функция для перевода списка в int
    for i in range(n):
        sp[i] = int(sp[i])
    return sp

k = input().split()
p = input().split()

k = change_type(len(k), k)
p = change_type(len(p), p)

def l_range(): #функция определение отрезка [l,r]
    s = []
    for i in range(n):
        if k[i] != p[i]:
            s.append(i)
    return s

s = l_range()

def change_sp(): #функция изменение последовательности выбранного отрезка [l,r]
    d = []
    sp = []
    if len(s) > 1:
        l = min(s)
        r = max(s)
        d += k[l:r+1:]
        d.sort()
        sp += k[:l:] + d + k[r+1::]
    else:
        sp += k
    return sp

sp = change_sp()

if sp == p: #сравнение с выигрышной комбинацией
    print('YES')
else:
    print('NO')