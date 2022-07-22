def fibonacci(n):
    #Opcion 1#
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    return n


def fibonacci_iter(n):
    a = 1
    b = 1
    if n == 1:
        print('0')
    elif n == 2:
        print('0', '1')
    else:
        print('0')
        print(a)
        print(b)
        for i in range(n - 3):
            total = a + b
            b = a
            a = total
            print(total)


if __name__ == "__main__":
    terminos = int(input("Cuantos terminos desea ver de la secuencia fibonacci: "))
    for i in range(terminos):
        print(fibonacci(i))
    fibonacci_iter(terminos)