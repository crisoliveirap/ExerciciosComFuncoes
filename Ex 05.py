# Sortear e somar
from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='- ')
        sleep(0.3)
    print('FIM!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somandos os valores pares de {lista}, temos um valor total de {soma}.')


numeros = list()
sorteia(numeros)
somapar(numeros)
