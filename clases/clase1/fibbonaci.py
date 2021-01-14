def fibbonaci(n):
    if n == 0 or n == 1:
        return 1
    return fibbonaci(n-1) + fibbonaci(n-2)
# Esta función repite muchos procesos.


def f_o(n):  # Fibonacci optimizado
    lista = [1, 1]
    for i in range(2, n+1):
        lista.append(lista[-1] + lista[-2])
    return lista[-1]


print(f_o(1000))
