#🧠 Ejercicios Día 5: Funciones + Repaso (Día 1 al 4)
#1. Función que saluda
#Definí una función saludar(nombre) que reciba un nombre y devuelva un saludo personalizado.✅ Practicás: def, parámetros, return, f-strings.

def saludar(nombre):
    return f"Hola {nombre}. ¡Bienvenido!"
print(saludar("Pedro"))

#2. Función que suma dos números
#Pedile al usuario dos números y usá una función sumar(a, b) que devuelva el resultado.✅ Practicás: input, conversión int(), return, operadores.

num1 = int(input("Por favor ingresa un primer número: "))
num2 = int(input("Por favor ingresa un segundo número: "))
def sumar(a, b):
    return a + b
print(sumar(num1, num2))


#3. Función que diga si un número es par o impar
#Definí una función es_par(numero) que devuelva True si es par, False si es impar.✅ Practicás: condicional if, operador %, booleanos.

#Creando la función 
def es_par(numero):
    if numero %2 == 0: #Uso de condicional y operador %.
        return True #Retornando los valores booleanos
    else:
        return False
print(es_par(4)) #Imprimiendo en pantalla el resultado de la función.


#4. Función que pida edad y diga si puede conducir
#Creá una función puede_conducir(edad) que diga si alguien puede o no manejar (mayores de 18).✅ Practicás: input, int(), condicionales, return.

#Creando la variable para saber la edad del usuario.
usuario = int(input("Por favor ingresa tu edad: "))
#Creando la función.
def puede_conducir(edad):
    if edad < 18: #Uso un condicional para verificar si es menor de edad.
        return "Eres menor de edad, no puedes conducir"#Retornando la respuesta cuando la condición es verdadera.
    else: #Si el usuario tiene 18 años o más, pasa automaticamente a esta sección.
        return "Puedes conducir!!"
print(puede_conducir(usuario)) #Imprimiendo en pantalla


#5. Función que calcule la longitud de un texto
#Definí una función longitud(texto) que devuelva cuántos caracteres tiene.✅ Usás len(), funciones y texto (str).

#Creando la función que calculará la cantidad de caracteres.
def longitud(texto):
    #Usamos la función len que devuelve la cantidad de caracteres en una cadena de texto.
    palabra = len(texto)
    #Retornamos la cantidad de caracteres almacenada en la variable palabra.
    return palabra
#Llamamos a la función con un texto de prueba y mostramos el resultado.
print(longitud("hola como estás?"))


#6. Función que genere una tabla de multiplicar
#Función tabla_multiplicar(numero) que imprima la tabla del número hasta el 10.✅ Usás: for, range(), print(), funciones.

## Creamos la función que generará la tabla de multiplicar del número ingresado.
def tabla_multiplicar(numero):
    #Usamos el bucle for para recorrer los números del 1 al 10.
    for i in range(1, 11):
        #Multiplicamos el número ingresado por el valor actual de i y mostramos el resultado.
        print(numero * i)
#Llamamos a la función con el número deseado para imprimir su tabla de multiplicar.
print(tabla_multiplicar(5))
  
  
#7. Función que sume una lista de números
#Definí sumar_lista(lista) que reciba una lista de números y devuelva la suma total.✅ Repasás: bucles (for), acumuladores, listas.

#Creando la función que va a recibir la suma total de los números.
def sumar_lista(lista):
    #Creamos una variable que tenga como valor 0 para que vaya acumulando el resultado.
    suma = 0
    #Usamos el bucle for para recorrer la lista y obtener cada número.
    for num in lista:
        suma += num
    print(suma) #Mostramos en pantalla el resultado de la suma.
#Llamamos a la función pasandole como parámetro una lista con números.
sumar_lista([2, 4, 6, 8])


#8. Función que pida números hasta acertar uno secreto
#Función adivinar(secreto) que le pida al usuario intentos hasta acertar el número (como el ejercicio del Día 4).✅ Usás: while, break, comparación, input.

# Función para que el usuario intente adivinar el número secreto.
def adivinar(secreto):
    # Pedimos al usuario un número antes de entrar en el bucle.
    numero_secreto = int(input("Por favor, ingresa un número: "))

    # Mientras el número ingresado sea diferente al secreto, el usuario sigue intentando.
    while numero_secreto != secreto:
        print("Lo siento, número errado. Inténtalo de nuevo.")
        
        # Pedimos otro número dentro del bucle, para que el usuario pueda seguir intentándolo.
        numero_secreto = int(input("Por favor, ingresa otro número: "))

    # Si el número ingresado es igual al secreto, mostramos un mensaje de éxito.
    print("¡Acertaste el número secreto!")
  
# Llamamos a la función con un número secreto (por ejemplo, 7).
adivinar(7)


#9. Función que cuente cuántas vocales tiene una palabra
#Función contar_vocales(palabra) → devuelve la cantidad de vocales que contiene.✅ Usás: bucles, condicionales, strings.

# Función para contar cuántas vocales tiene una palabra.
def contar_vocales(palabra):
    # Creamos una variable para contar las vocales, iniciando en 0.
    contador_vocales = 0  

    # Iteramos cada letra de la palabra.
    for letra in palabra:  
        # Verificamos si la letra es una vocal (mayúscula o minúscula).
        if letra in "aeiouAEIOU":  
            # Si es una vocal, aumentamos el contador en 1.
            contador_vocales += 1  

    # Retornamos el número total de vocales encontradas.
    return contador_vocales  

# Llamamos a la función con una palabra y mostramos el resultado.
print(contar_vocales("programación"))  # Esto imprimirá el número de vocales en "programación"
    

#10. Función general para menú de opciones
#Crea una función menu() que muestre varias opciones (1. Saludar, 2. Sumar, 3. Salir) y llame a las funciones anteriores según lo que elija el usuario.✅ Usás: funciones, condicionales, input, bucles.

# Función para saludar
def saludar():
    print("¡Hola! Espero que estés teniendo un gran día.")

# Función para sumar dos números
def sumar():
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    print(f"La suma de {num1} + {num2} es {num1 + num2}")

# Función del menú de opciones
def menu():
    while True:  # Bucle infinito hasta que el usuario elija salir
        print("\nMenú de opciones:")
        print("1. Saludar")
        print("2. Sumar")
        print("3. Salir")

        opcion = input("Elige una opción (1, 2, 3): ")

        if opcion == "1":
            saludar()  # Llamamos a la función de saludo
        elif opcion == "2":
            sumar()  # Llamamos a la función de suma
        elif opcion == "3":
            print("¡Gracias por usar el menú! Hasta luego.")
            break  # Salimos del bucle y terminamos el programa
        else:
            print("Opción inválida, por favor intenta nuevamente.")

# Llamamos a la función del menú para iniciar el programa
menu()