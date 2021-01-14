def consulta(n):
    numero = 9457183
    if n >= numero:
        return True
    else:
        return False


def sol_nb():  # Solución no bacán
    for i in range(100000000):
        if consulta(i):
            return i


def sol_bb():  # Consulta busqueda binaria
    izq = 0
    der = 100000000
    while izq != der:
        med = (izq + der) // 2
        if consulta(med):
            der = med
        else:
            izq = med + 1
    return izq


# print(sol_nb())
print(sol_bb())
