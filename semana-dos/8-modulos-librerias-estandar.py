'''
Semana 2 - Python Interactivo y Divertido
Avanzá a tu ritmo, sin abrumarte y divirtiéndote.
📅 Día 8: Módulos y Librerías Estándar
Temas:
- Uso de import y from ... import
- Librerías: math, random, datetime
'''


#Ejercicios con math, random y datetime en Python

#Importamos las librerías que vamos a utilizar el día de hoy.
import math
import random
import datetime

#1️⃣ Calcular raíces cuadradas
#- Pide al usuario que ingrese un número y muestra su raíz cuadrada.

#Creamos una variable para pedir el dato al usuario.
numero = int(input("Ingresá un número para calcular su raíz cuadrada: "))
#Utilizamos la función math.sqrt() para calcular la raíz cuadrada del número ingresado.
raiz_cuadrada = math.sqrt(numero)
#Mostramos el resultado.
print(raiz_cuadrada)

#2️⃣ Simular el lanzamiento de un dado
#- Usa random.randint(1,6) para generar un número aleatorio y simular un dado.

#Creamos una variable que utiliza la función random.randint() para simular el juego.
simular_dado = random.randint(1, 6)
#Mostramos el resultado.
print(simular_dado)

#3️⃣ Mostrar fecha y hora actual
#- Usa datetime.datetime.now() para obtener la fecha y hora actual y mostrarla en formato legible.

#Creamos una variable que utiliza la función datetime.datetime.now() para obtener la fecha y hora actual.
ahora = datetime.datetime.now()
#Mostramos el resultado.
print(ahora)


#4️⃣ Generador de números de la suerte
#- Crea un programa que genere 5 números aleatorios entre 1 y 50 y los muestre como "números de la suerte".

#Creamos una variable con la función random.randint(), le pasamos los argumentos del enunciado.
numero_suerte = random.randint(1, 50)
#Mostramos el resultado.
print(f"El número de la suerte es: {numero_suerte}")


#5️⃣ Calcular la raíz cuadrada de varios números
#- Pide una lista de números al usuario y calcula la raíz cuadrada de cada uno usando un bucle.

#Creamos una variable que almacena el dato ingresado por el usuario.
pedir_numero = input("Ingresá 5 números enteros separados por coma: ")
lista_numeros = pedir_numero.split(",")  # Separa los números
lista_numeros = [float(x) for x in lista_numeros]  # Convierte cada elemento a número

#Utilizamos el bucle for para iterar en cada elemento de la lista.
for i in lista_numeros:
    raiz_cuadrada = math.sqrt(i)  # Calcula raíz cuadrada
    #Mostramos el resultado.
    print(f"La raíz cuadrada de {i} es: {raiz_cuadrada}")

#6️⃣ Juego: Adivina el número
#- Usa random.randint(1,10) para generar un número secreto y permite que el usuario adivine hasta acertar.

#Generamos un número secreto entre 1 y 10.
numero_secreto = random.randint(1, 10)
#Pedimos al usuario que ingrese un número.
adivina_el_numero = input("Adivina un número entre 1 y 10: ")
#Convertimos el número ingresado de texto (str) a un entero(int).
adivina_el_numero = int(adivina_el_numero)
#Mientras el número ingresado no sea igual al número secreto, seguimos pidiendo intentos.
while adivina_el_numero != numero_secreto:
    print("Lo siento, el número ingresado no es correcto, intentá nuevamente.")
    #Pedimos un nuevo número al usuario.
    adivina_el_numero = input("Adivina un número entre 1 y 10: ")
    #Convertimos nuevamente el número ingresado a entero.
    adivina_el_numero = int(adivina_el_numero)
#Cuando el usuario acierta, mostramos un mensaje de éxito!
print("Lo lograste, acertaste el número!")


#7️⃣ Diferencia entre fechas
#- Calcula cuántos días faltan para una fecha futura utilizando datetime.timedelta().

#Creamos una variable que contiene el día de hoy.
hoy = datetime.datetime.now()
#Creamos otra variable que va a contener la fecha futura.
futuro = hoy + datetime.timedelta(days = 6)
#Usamos un f-string para mostrar la fecha de hoy y la fecha futura.
print(f"Hoy es {hoy} y dentro de 6 días será, {futuro}")



#8️⃣ Registro de eventos con marcas de tiempo
#- Cada vez que el usuario presione ENTER, registra la fecha y hora con datetime.now().

#Pedimos el dato al usuario.
entrada = input("\nPresioná ENTER para ver la fecha y hora o cualquier otra tecla para salir: ")
#Creamos un bucle para comparar si la entrada del usuario es lo que estamos buscando.
while entrada == "":
    #Creamos una variable que almacena la fecha actual.
    ahora = datetime.datetime.now()
    #Mostramos en pantalla la fecha actual.
    print(f"\nRegistro de evento. Fecha y hora actual: {ahora}")
    #Preguntamos de nuevo al usuario y verificamos si quiere continuar en el programa.
    entrada = input("\nPresioná ENTER para ver la fecha y hora o cualquier otra tecla para salir: ")
#Mostramos en pantalla un mensaje para que el usuario sepa que salió del programa.
print("\nPrograma finalizado.")


#9️⃣ Mezclar una lista de nombres
#- Usa random.shuffle(lista) para mezclar una lista de nombres y obtener un orden aleatorio.

#Creamos una variable que guarda una lista ordenada de nombres.
lista_nombres = ["juan", "pedro", "sofía", "pamela", "susana"]
#Utilizamos la función random.shuffle para mezclar de forma aleatoria, los nombres de la lista ordenada.
random.shuffle(lista_nombres)
#Mostramos en pantalla la lista mezclada aleatoriamente.
print(lista_nombres)

#🔟 Conversión de formato de fecha
#- Pide al usuario una fecha y usa .strftime("%Y-%m-%d") para convertirla en otro formato.
 
# Pedimos la fecha al usuario (debe ingresarla en formato "dd/mm/yyyy").
fecha = input("\nIngresá una fecha (formato: dd/mm/yyyy): ")  

# Convertimos la fecha de texto a objeto datetime con el formato correcto.
fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y")  

# Formateamos la fecha en el nuevo formato "YYYY-MM-DD".
fecha_formateada = fecha.strftime("%Y-%m-%d")  

# Mostramos la fecha convertida.
print(f"\nFecha formateada: {fecha_formateada}")  


#🔹 Ejercicios de repaso:

#1️⃣ Cálculo de potencias
#- Pide al usuario que ingrese un número y un exponente, y muestra el resultado de elevar el número al exponente utilizando math.pow().

#Creamos las variables para pedir los números al usuario.
a = int(input("\nIngresá un número: "))
b = int(input("\nIngresá un exponente: "))
#Utilizamos la función math.pow() para sacar la potencia de los números ingresados por el usuario.
potencia = math.pow(a, b)
#Mostramos el resultado.
print(f"\nEl resultado de {a} elevado a la {b} es: {potencia}")



#2️⃣ Simulación de dos dados
#- Usa random.randint(1,6) para simular el lanzamiento de dos dados y muestra el resultado de cada uno junto con su suma total.

#Creamos las variables, utilizando la función random.randint()
dado_uno = random.randint(1, 6)
#Resultado del primer dado.
print(f"\n Primer dado: {dado_uno}")
dado_dos = random.randint(1, 6)
#Resultado del segundo dado.
print(f"\n Segundo dado {dado_dos}")
#Creamos una variable que suma los resultados de los dados.
resulado = dado_uno + dado_dos
#Mostramos el resultado final en pantalla.
print(f"\n La suma de los dados es: {resulado}")


#3- Generador de combinaciones aleatorias
#- Usa random.sample() para seleccionar tres números aleatorios de una lista del 1 al 50 y mostrarlo como una posible combinación ganadora.

#Creamos una variable que crea una lista entre el número 1 al 50.
numeros = list(range(1, 51))
#Creamos la variable que va a seleccionar los 3 números aleatorios, utlizando la función random.sample().
num_list = random.sample(numeros, 3)
#Mostramos el resultado.
print(f"\n Los posibles números ganadores son: {num_list}")

#Creamos un programa que selecciona 6 números únicos.

numeros = list(range(1, 61))
num_list = sorted(random.sample(numeros, 6))  # Selecciona y ordena 6 números únicos
print(f"\nTus números de la suerte son: {num_list}")

