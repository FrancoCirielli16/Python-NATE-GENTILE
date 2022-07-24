import random


def string_mas_larga(lista):
    max = ""
    for string in lista:
        if len(string) > len(max):
            max = string
    return max

def sumar_numeros_de_lista(lista):
    suma = 0
    for n in lista:
        suma += n
    return suma

def es_impar(numero):
    if numero % 2 == 0:
        return False
    else:
        return True

def seguridad():
    quiz = input("Esta seguro? (S/N): ")
    if quiz == 'S':
        return True
    else:
        return False

def convertidor_de_mayusuclas(texto):
    texto2 = ""
    for char in texto:
        if char.islower():
            char = char.swapcase()
            texto2 += char
        else:
            texto2 += char
    return texto2


def adivinaza(numero):
    num = int(input("Adivina el numero que estoy pensado: "))
    while num != numero:
        num = int(input("ese no es intentalo devuelta: "))
    return True




if __name__ == "__main__":
    lista = ["putos", "negros", "anasheee"]
    print(string_mas_larga(lista))
    lista_de_numeros = [10,10,50,25,105]
    print(sumar_numeros_de_lista(lista_de_numeros))
    print(es_impar(101))
    print(seguridad())
    print(convertidor_de_mayusuclas("Hola putos de mierda"))
    num = random.randint(1,100)
    print(num)
    adivinaza(num)