def bs(lista, numero):
    izq = 0
    der = len(lista) - 1
    while izq != der:
        med = (izq + der) // 2
        if lista[med] >= numero:
            der = med
        else:
            izq = med + 1
    return izq


lenght = input()
worms = input().split()
worms = [int(x) for x in worms]
len_marmot = input()
guess = [int(x) for x in input().split()]

sum_worms = [worms[0]]
for i in range(1, len(worms)):
    sum_worms.append(sum_worms[i-1] + worms[i])

print(sum_worms)
for number in guess:
    print(bs(sum_worms, number) + 1)
