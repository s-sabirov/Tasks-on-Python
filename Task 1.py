def change_type(n, sp): #перевод списка в int
    for i in range(n):
        sp[i] = int(sp[i])
    return sp

s = input().split() #ввод данных
price = input().split()

s = change_type(len(s), s) #вызов функции перевода в int
price = change_type(len(price), price)

price.sort() #сортировка списка по возрастанию

def budget(max): #определение самого дорогого револьвера
    for i in range(len(price)):
        if s[1] > max and s[1] >= price[i]:
            max = price[i]
    return max

max = 0

print(budget(max))


