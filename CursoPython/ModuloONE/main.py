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
b = b - 3
print(b % b)

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
#ESTRUCTURAS DE CONTROL#

if variable == 4: #si se cumple la condicion pasa tal cosa #
    print("algo")
else:
    print("otra cosa")

#METODOS Y FUNCIONES#

max(1,2,3) #Devuelve el maximo entre la cantidad que numeros que le pases#
min(1,2,3) #Devuelve el minimo entre la cantidad de numeros que le pases#
type(variable) # Te enseña que tipo de variables es #
float(variable) # convierte a numero con coma o flotante#
int(variable) # convierte a numero entero#
len("HOLA") #devuelve la cantidad de caracteres que tiene un string#
