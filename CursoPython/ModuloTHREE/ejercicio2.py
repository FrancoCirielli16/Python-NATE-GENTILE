def potencia(num,elevar):
    pot = 1
    for n in range(elevar):
        pot *= num
    return pot
if __name__ == "__main__":
    print(potencia(int(input("elija el numero con el que quiere trabajar: ")), int(input("elija la potencia: "))))