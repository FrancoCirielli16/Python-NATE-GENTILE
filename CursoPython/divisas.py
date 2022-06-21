
dolar_euro = 0.95
libra_euro = 1.17

opcion = input("Que deseas hacer?\n"
               "A: Dolar a Euro\n"
               "B: Libra a Euro\n"
               "C: Euro a Dolar\n"
               "D: Euro a Libra\n")
if opcion == "A":
    opcion_A = int(input("Dime una cantidad de Dolars: "))
    print("Son {}" .format(opcion_A * dolar_euro) + " Euros")
elif opcion == "B":
    opcion_B = int(input("Dime una cantidad de Libras: "))
    print("Son {}" .format(opcion_B * libra_euro) + " Euros")
elif opcion == "C":
    opcion_C = int(input("Dime una cantidad de Euros: "))
    print("Son {}" .format(opcion_C / dolar_euro) + " Dolars")
elif opcion == "D":
    opcion_D = int(input("Dime una cantidad de Euros: "))
    print("Son {}" .format(opcion_D / libra_euro) + " Libras")
else:
    print("Solo puedes escojer entre las opciones A, B, C, D")
    exit()




dolar_euro = 0.95
libra_euro = 1.17

opcion = input("Que deseas hacer?\n"
               "A: Dolar a Euro\n"
               "B: Libra a Euro\n"
               "C: Euro a Dolar\n"
               "D: Euro a Libra\n")
if opcion == "A":
    opcion_A = int(input("Dime una cantidad de Dolars: "))
    print("Son {}" .format(opcion_A * dolar_euro) + " Euros")
elif opcion == "B":
    opcion_B = int(input("Dime una cantidad de Libras: "))
    print("Son {}" .format(opcion_B * libra_euro) + " Euros")
elif opcion == "C":
    opcion_C = int(input("Dime una cantidad de Euros: "))
    print("Son {}" .format(opcion_C / dolar_euro) + " Dolars")
elif opcion == "D":
    opcion_D = int(input("Dime una cantidad de Euros: "))
    print("Son {}" .format(opcion_D / libra_euro) + " Libras")
else:
    print("Solo puedes escojer entre las opciones A, B, C, D")
    exit()