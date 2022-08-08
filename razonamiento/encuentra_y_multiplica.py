def encuentra_y_multiplica(lista, target):
    for i, el in enumerate(lista):
        complement = target - el
        if complement in lista[i + 1:]:
            return el * complement

lista = [1,5, 1010, 1012]
target = 2022
print(encuentra_y_multiplica(lista, target))