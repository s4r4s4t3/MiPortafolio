#Dia 1: Introduccion a Python
#Temas: input(), print(), variables, tipos de datos basicos (str, int, float, bool), f-strings.
#- Aprende que es una variable y como guardar informacion.
#- Usa input() para pedir datos al usuario.
#- Mostra resultados con print().
#- Identifica el tipo de dato con type().
#- Hace operaciones basicas y mostra resultados.
# Objetivo: Familiarizarse con la estructura de un programa simple en Python.
#[EJERCICIO] Ejercicios:
#- Crear variables de texto y numeros.
#- Pedir nombre, edad, altura.
#- Mostrar resultados combinando texto y variables.



 #Ejercicios del Día 1 (ajustados)
#1-Pide al usuario su nombre y muéstralo por pantalla.
usuario = input("Dame tu nombre de usuario por favor: ")
print(f"El nombre de usuario es: {usuario}")

#2-Pide al usuario su edad y guárdala en una variable.
edad = int(input("Por favor ingrese su Edad: "))
print(f"La edad del usuario es: {edad}")

#3-Muestra un saludo personalizado usando el nombre y edad.
nombre = input("Por favor ingrese su nombre: ")
edad = int(input("Por favor ingrese su edad: "))
print(f"El usuario se llama {nombre}, y tiene {edad} años. ")

#4-Crea una variable altura y asígnale un número con decimales.
altura = float(input("Ingrese su altura: "))
print(f"El usuario mide {altura} metros")

#5-Muestra por pantalla tu nombre, edad y altura usando print().
nombre = "Ezequiel"
edad = 37
altura = 1.88
print(f"El usuario e llama {nombre}, tiene {edad} años y mide {altura} metros.")

#6-Crea tres variables: una cadena de texto, un número entero y un número decimal. Muestra sus tipos con type().
cadena = "hola como estas?"
numero_entero = 34
numero_decimal = 1.88
print(type(cadena))
print(type(numero_entero))
print(type(numero_decimal))

#7-Pide al usuario dos números y muestra su suma. 🔁 Opcional (si te sentís cómodo): Mostrar también resta y multiplicación.
num1 = int(input("Dame el primer numero: "))
num2 = int(input("Dame el siguiente numero: "))

print(f"La suma de los numeros es: {num1 + num2} ")
print(f"La resta de los numeros es: {num1 - num2}")
print(f"La mutiplicación de los numeros es: {num1 * num2}")

#🧠 Ejercicios de refuerzo – Día 1
#1-Pide al usuario su color favorito y su comida favorita, y mostrálos juntos en una oración.
color = input("Cual es tu color favorito? ")
comida = input("Cuál es tu comida favorita? ")
print(f"El color favorito del usuario es {color} y su comida favorita es {comida}")



#2-Pide al usuario su ciudad y su país, y arma una frase como: “Vivís en Rosario, Argentina”.
ciudad = input("En que ciudad vivís? ")
pais = input("Cuál es tu país de residencia? ")
print(f"Vivís en {ciudad}, {pais}.")

#3-Guarda tu nombre en una variable y mostrá cuántas letras tiene con len(). (explicado previamente)
nombre = "Ezequiel"
print(len(nombre))

#4-Crea tres variables: nombre, edad y hobby. Mostralas en una sola línea con f-string.
nombre = "Pablo"
edad = 28
hobby = "estudiar programación"
print(f"Me llamo {nombre}, tengo {edad} años y mi hobby es {hobby}.")

#5-Pedile al usuario un número decimal y mostrale el doble.
numero_decimal = float(input("Pasame un número decimal asi te muestro el doble: "))
print(numero_decimal * 2)

#6-Pedile al usuario su año de nacimiento y mostrále cuántos años tiene. (sin condicionales)
nacimiento = int(input("Decime tu año de nacimiento, y te digo tu edad: "))
edad = 2025 - nacimiento
print(f"Tu edad es {edad}")

#7-Mostrá el tipo de dato de las siguientes variables: "Python", 30, 3.14, True
a = "Python"
b = 30
c = 3.14
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))


#8-Convertí un número guardado como texto ("45") en entero y sumale 5. Mostrá el resultado.
num = int("45")
num1 = num + 5
print(num1)

#9-Pedile al usuario su estatura en metros y mostrála con solo 1 decimal. (round())
estatura = round(float(input("Decime tu altura: ")))
print(f"La altura es {estatura}") 

#10-Mostrá un mensaje de bienvenida personalizado como: “Hola Ezequiel, bienvenido al mundo Python!”
nombre = input("Decime tu nombre: ")
print(f"Hola {nombre}, bienvenido al mundo de Python")