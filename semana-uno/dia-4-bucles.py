#🧠 Ejercicios Día 4: Bucles + Repaso (Día 1 a Día 3)

#1. Contador personalizado
#Pedir al usuario dos números: inicio y fin. Mostrar todos los números entre esos dos usando un bucle for. Usa input() y int() para capturar datos (Día 1–2), Usa range() y for (Día 4)

#Creando las variables para pedirle al usuario dos números
inicio = int(input("Por favor ingresá un primero número: "))
fin = int(input("Por favor dame el siguiente número: "))
#Verificando el orden de los números y ajustando el rango 
if inicio < fin:
    for i in range(inicio, fin):
        print(i) #mostrando el resultado
else:
    for i in range(inicio, fin, -1): #itera en orden inverso
        print(i) #Mostrando el resultado

print("Listo!!") #Fín del programa



#2. Suma acumulada
#Pedir al usuario que ingrese 5 números (uno por uno) y mostrar la suma total al final.Usa for, suma acumulada (Día 4) Conversión con int() (Día 2)

#Creando una variable que almacene la suma total.
suma_total = 0 #guardando la suma acumulada
for i in range(5): #Este bucle se ejecuta 5 veces, permitiendo al suario ingresar un total de 5 números
       numero = int(input("Ingresá un número: ")) #Pidiendo al usuario
       suma_total += numero #Sumando el número y guardandolo en la variable suma_total
print(f"La suma total es igual a {suma_total}") #Mostrando el resultado almacenado en la variable suma_total


#3. ¿Cuántas letras tiene tu nombre? (versión bucle)
#Pedir el nombre al usuario y mostrar cuántas letras tiene usando un bucle for (sin usar len() directamente). Entrada con input() (Día 1), Contar manualmente con for (Día 4)

nombre = input("Por favor, ingresá tu nombre: ") #Creando la variable para pedir el nombre al usuario
contador_letras = 0 #Creando la variable contenedora, es decir la que va a guardar el resultado de la suma de las letras.
for letra in nombre: #Iteramos cada letra en la variable nombre (los espacios tambien cuentan)
    contador_letras += 1 #Aquí usamos la variable contador_letras que se va a ir sumando una a una.
print(f"La cantidad de letras que tiene tu nombre es {contador_letras}") #Mostrando el resultado con un f-strings


#4. Verificador de mayor de edad (varios intentos)
#Pedir edades de 3 personas y decir si cada una puede conducir. Usa for, condicionales if (Día 3), Muestra resultados con f-strings (Día 1)

for i in range(3): #creando un for que maneja 3 entradas
    edad = int(input(f"Ingresá la edad de la persona {i+1}: "))  # Indicamos el número de cada persona
    if edad >= 18: #Creando una condición para corroborar que el usuario sea mayor de edad
        print(f"Con {edad} años, puedes conducir.")
    else:
        print(f"Con {edad} años, no puedes conducir.") #Mostrando los resultados



#5. Tabla de multiplicar
#Pedir al usuario un número y mostrar su tabla del 1 al 10. Usa for con range(1, 11), Multiplicación (Día 2)

# Pido un número al usuario
numero = int(input("Ingresa un número: "))

# Muestro su tabla del 1 al 10
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


#6. Repetir contraseña
#Pedir al usuario que escriba una contraseña hasta que coincida con "python123". Mostrar un mensaje de éxito al final. Usa while, input() (Día 1, 4), Comparaciones (Día 3)

# Pedimos al usuario la contraseña por primera vez.
contraseña = input("Por favor imgresá la contraseña: ")
#Usamos el bucle while para repetir la solicitud hasta que el usuario ingrese la contraseña correcta.
while contraseña != "python123":
#Si la contraseña es incorrecta, mostramos un mensaje de error para que el usuario vuelva a intentarlo.
    print("contraseña incorrecta, por favor intente nuevamente.")
#Volvemos a pedir la contraseña, permitiendo nuevos intentos.
    contraseña = input("Por favor imgresá la contraseña: ")
#Cuando la cotraseña es correcta, el bucle se detiene mostrando un mensaje de éxito.
print("Acceso concedido! Contraseña correcta.")


#7. Sumar solo positivos
#Pedir al usuario que ingrese 5 números. Si el número es negativo, no lo sumes (usa continue). Conversión con int() (Día 2), for, continue, suma acumulada (Día 4)

#Variable donde se se va a guardar la suma total de n positívos
suma_total = 0 #comienza en 0 por que aún no tiene ningun valor
#Creando un bucle for con range() para repetir la acción 5 veces
for i in range(5):
#Pedir el número al usuario y convertirlo a entero
    numero = int(input("Ingresá un número: "))
    if numero < 0: #Creamos una condición para ver si el numero es negativo
        continue #Salta la iteración y no suma el número
    suma_total += numero #Agrega el número a la suma acumulada
print(f"La suma total de los números positivos es: {suma_total}")


#8. Números pares hasta un límite
#Pedir un número y mostrar todos los pares desde 0 hasta ese número. for, condicional if n % 2 == 0 (Día 3–4)

#Pedir el número al usuario
limite = int(input("Ingresá un número límite: "))
for n in range(limite + 1): #usamos limite + 1 para incluir el número ingresado. Ya que range() no incluye el último número.
    if n % 2 == 0: #Verificamos si el número es par.
        print(n) #Mostramos solo los números pares.
        

#9. Simulador de intentos
#El usuario tiene 3 intentos para adivinar un número secreto. Si acierta, termina el juego (break). while o for, break, input() (Día 1–4), Comparación con if (Día 3)

#Elegimos un número secreto y establecemos un límite de intentos
numero_secreto = 7 #Definimos el número secreto que el usuario debe adivinar.
intentos_maximos = 3 #Máximo de intentos permitidos.
#Usamos un for para repetir el proceso hasta que el usuario adivine o se acaben los intentos.
for intento in range(intentos_maximos): #Se ejecutará máximo 3 veces
#Dentro del bucle pedimos el número    
    numero_usuario = int(input("Adivina el número secreto: "))
    #Creamos la condición 
    if numero_usuario == numero_secreto:
        #Imprimimos si el usuario acierta el número.
        print("Adivinaste el número secreto!!")
        break #Evita que el bucle siga.
#Usamos el else fuera del for para evitar que se imprima cada vez que el usuario falla.   
else:
    print(f"Lo siento, agotaste los intentos. El número secreto era {numero_secreto}")



#10. Contar vocales
#Pedir una palabra y contar cuántas vocales tiene (usando un bucle for). input(), recorrer cadena con for, Comparaciones con if (Día 3)

#El primer paso es pedir la palabra al usuario
palabra = input("Ingresá una palabra: ")
#Creamos una variable para guardar la cantidad de vocales encontradas
contador_vocales = 0 #Comienza en cero por que no tiene ninguna vocal por ahora.
for letra in palabra: #Iteramos cada letra de la palabra.
    #Verificamos si la letra es una vocal con un condicional.
    if letra in "aeiouAEIOU":
        contador_vocales += 1 #Incrementa la cuenta de vocales, cada vez que encontramos una en la palabra.
print(f"La palabra '{palabra}' tiene {contador_vocales} vocales.")




