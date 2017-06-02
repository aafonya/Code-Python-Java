lista = [1, 1, 2, 3, 5, 8, 13]
print(lista[5])

lista[4] = 5
lista[5] = 8

print(lista[lista[lista[2]] + 2])


def func(x):
    res = 0
    for i in range(x):
        res += i
    return res
print(func(5))
