#OPERADORES#

#bool#

# and #
# or #
# != distinto#
# == igual #
# < menor #
# <= menor o igual #
# > mayor #
# >= mayor o igual #
# True #
# False #

a = 4
if a == 3 or a > 3 or a < 3 or a != 3:
    print("puede pasar algo")

#aritmeticos#
# + sumar #
# - restar #
# / dividir #
# % resto #
# * multiplicacion #

b = 3
b = b * 2
b = b / 2
b -= 1
b += 1
print(b % b)

#TIPOS DE VARIABLES#

a = "HOLA " #string#
a = 10 #entero#
a = 10.5 #flotante#
a = 'A' #caracteres#
a = [] #vector#
#INTRUCCIONES#

#OUTPUT#
print("HOLA") #para imprimir#
print("Hola numero {}".format(4)) #para imprimir junto a un numero#
print("Hola"*3) #multiplico el texto 3 veces#

#INPUT#
variable = 3 #asignaciones#
variable = input("Ingrese un valor") #Carga la varible con caracteres#
variable = int(input("ingrese un numero entero")) #el numero que ingreses va a ser de tipo entero#
variable = float(input("ingrese un numero flotante")) #el numero que ingrese va a ser de tipo flotante#
variable = str(input("ingrese su nombre"))
variable = None
#ESTRUCTURAS DE CONTROL#

if a<10:
   print ("Es menor de 10")
elif a<20: #elif remplaza el else-if es un else con una condicion#
   print ("Es menor de 20")
else:
    print ("Es mayor de 20")


while variable != 1 and variable != 2 and variable != 3: #mientras estas condiciones no se cumplan#
    variable = int(input("numero: 1,2,3")) #volvemos al inicio de la linea de while #

#ITERADOR#

for a in vector:
    print(a)

for a in range(5):
    print(a)

for letra in frase:
    print(letra)

#METODOS Y FUNCIONES#
int() #Convierte lo que le pasemos a entero#
max(1,2,3) #Devuelve el maximo entre la cantidad que numeros que le pases#
min(1,2,3) #Devuelve el minimo entre la cantidad de numeros que le pases#
type(variable) # Te enseña que tipo de variables es #
float(variable) # convierte a numero con coma o flotante#
int(variable) # convierte a numero entero#
len("HOLA") #devuelve la cantidad de caracteres que tiene un string#
vector.append() #Agrega al vector algo#
vector.pop() #Saca del vector el ultimo elemento#
variable = numeros.split(",") #Rompe una cadena de string en el caracter que le pasemos#
variable in vector #Esto devuelve si esa variable se encuentra o no en el vector o string#
range(1, 5) or range(15) or range(cantidad_de_veces) #Esta funcion convierte el input otorgado en un vector para iterar [1,2,3,4] or [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]#

#Maneras de trabajar con un vector#

#En ves de hacer esto#

numeros_introducidos = input("Ingrese la lista de numeros que desea agregar separados por una coma")
numeros_de_usuario = numeros_introducidos.split(",")
lista_de_numeros = []

for numero in numeros_de_usuario:
    lista_de_numeros.append(int(numero))

#Mejor hacer esto#

numeros_introducidos = input("Ingrese la lista de numeros que desea agregar separados por una coma")
numeros_de_usuario = [int(numero) for numero in numeros_introducidos.split(",")]
