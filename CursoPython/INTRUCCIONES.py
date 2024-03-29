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
import re

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

for item in urls[:10]: #fitral la lista hasta el item 10#

#METODOS Y FUNCIONES#
int() #Convierte lo que le pasemos a entero#
max(1,2,3) #Devuelve el maximo entre la cantidad que numeros que le pases#
min(1,2,3) #Devuelve el minimo entre la cantidad de numeros que le pases#
type(variable) # Te enseña que tipo de variables es #
float(variable) # convierte a numero con coma o flotante#
int(variable) # convierte a numero entero#
len("HOLA") #devuelve la cantidad de caracteres que tiene un string#
sort()#ordena listas de forma acendente o decendente#
vector.append() #Agrega al vector algo#
vector.pop() #Saca del vector el ultimo elemento#
variable = numeros.split(",") #Rompe una cadena de string en el caracter que le pasemos#
variable in vector #Esto devuelve si esa variable se encuentra o no en el vector o string#
range(1, 5) or range(15) or range(cantidad_de_veces) #Esta funcion convierte el input otorgado en un vector para iterar [1,2,3,4] or [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]#
nombre2 = nombre[::-1] #Da vuelta el string#
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


#Funciones#

#Se comienza con def#

def nombredelafuncion():
    return False


#Si se necesita escribir en un archivo txt#
lista =["pan","arroz","etc"]
a = open("Lo que quieras", "w") # w porque es un archivo de escritura r si se quiere leer y a para agregar#
a.write("\n".join(lista)) #se agregaria al txt por enters lo que este en la lista#
a.close()#cierra el txt#

#Manera mas eficiente de abrir y cerrar archivos#

with open("Nombre.txt", "w") as mi_archivo:
    mi_archivo.write("\n".join(lista))#Escribo en mi archivo#
#desde aca ya cierra sin identacion#

#para leer un archivo txt#
with open("Nombre.txt", "r") as mi_archivo:
    lista = mi_archivo.read().split("\n")#read es lectura osea que leo lo que hay en el archivo nombre#
#desde aca ya cierra sin identacion#


#para leer un archivo txt y evitar errores#
try:
    with open("Nombre.txt", "r") as mi_archivo:
        lista = mi_archivo.read().split("\n")#read es lectura osea que leo lo que hay en el archivo nombre#
except FileNotFoundError: #Si colocamos Exception no importa que error va a imprirmir o hacer lo que le indicamos #
    print("El archivo no exite")
#desde aca ya cierra sin identacion#



#Funcionalidades con el if y el for#

if input_usuario.lower() in [a.lower for a in lista]:
    hacer_algo

#EXPRECIONES REGULARES#

#Se utiliza la libreria re#

re.findall() #Lo que hace es filtrar por ejemplo una lista y buscar las coinicidencias que le pasemos
re.findall("https://twitter.com/[A-Za-z0-9]+$") #Me va a devolver las conicidencias que haya con los items que le pase#
re.findall("https://twitter.com/([A-Za-z0-9])+$") #Ponienedo parentesis nos filtra mas aun y nos da esa parte que
                                                                                                    # encerramos()#


steam_phat = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\*"
games_path = glob.glob(steam_phat) #glob retorna las direcciones de las carpetas del directorio que le pase#
games_path.sort(key=os.path.getmtime, reverse=True) #sort nos permite ordenar una lista de forma acendente o decendente#
for games_paths in games_path:
    games.append(games_paths.split("\\")[-1]) #-1 porque tomo el ultimo elemento del path#


#USANDO libreria webdriver y request

USER = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"} #cargo un usuario normal para no levantar capchat#
page = r.get(URL, headers=USER) #me conecto con el servidor de la pagina
buy_zone = page.html.find('#buyNow') #cargo el html de la pagina
#webdriver
driver = webdriver.Firefox() #abro el firefox
driver.get(URLa) #uso la url cargada #
driver.find_element_by_class_name("").click #hago click en la clase que le indique#