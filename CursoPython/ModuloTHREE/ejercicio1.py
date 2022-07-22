def main(opcion):
    if opcion == "1":
        #Opcion1#
        numeros = []
        suma = 0
        for n in range(1, 20):
            numeros.append(str(n))
            suma += n
        cadena = " + ".join(numeros)
        cadena += " = " + str(suma)
        return cadena
    elif opcion == "2":
        #Opcion 2#
        numeros = ""
        suma = 0
        for n in range(1, 20):
            numeros += str(n) +" + "
            suma += n
        numeros += "="+str(suma)
        return numeros


if __name__ == "__main__":

    print(main(input("Que opcion desea? 1/2: ")))