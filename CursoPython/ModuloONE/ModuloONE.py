#PRIMER EJERCICIO#

#conversor fahrenheint a celcius#
fahrenheint = float(input("Cuantos grados en fahrenheit? "))
print("En celsius serian {}".format((fahrenheint-32)*5/9))

#conversor libra a euro#
Libras = float(input("Cantidad de Libras? "))
converter_euro_to_libra = float(input("¿Cuanto es la conversión de euro a libra? "))
print("Esta son las libras {} ".format(converter_euro_to_libra*Libras))

#SEGUNDO EJERICIO#

#adivina el numero#

numeroPremio = random.randint(1, 10)

print("Si adivinas en que numero estoy pensando del 1 al 10 te doy 5 euros")
respuesta = int(input("Cual es el numero?"))

if respuesta == numeroPremio:
    print("Felicidades!! aqui tienes los 5 euros")

if respuesta != numeroPremio:
    if respuesta > 10:
        print("Lo siento, el numero era el {} , dije que el numero maximo era el 10, atiendeme la proxima vez".format(numeroPremio))
    if respuesta <= 10:
        print("Oh... lo siento, el numero era el {}".format(numeroPremio))
