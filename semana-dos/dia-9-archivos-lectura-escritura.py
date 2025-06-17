#📂 Ejercicios Día 9: Archivos en Python (Lectura y Escritura)
#🟢 Nivel 1: Básicos
#1️⃣ Crear y escribir en un archivo

#1- Pedile al usuario que ingrese su nombre y edad.Guardá esa información en un archivo llamado datos_personales.txt.

#Pedimos la información al usuario.
nombre = input("Ingresá tu nombre: ")
edad = int(input("Ingresá tu edad: "))
#Abrimos un archivo en modo de escritura.
with open("datos_personales.txt", "w") as archivo:
    archivo.write(f"Nombre: {nombre}, Edad: {edad}")
#Mostramos un mensaje de éxito.
print("La información se guardo correctamente!")


#2️⃣ Leer un archivo existente. Creá un archivo llamado mensaje.txt con el texto: "Hola! Este es un mensaje secreto."Luego, desde tu código Python, abrilo y mostrá el contenido por pantalla.

#Esto nos dice desde qué carpeta Python intenta acceder al archivo.
#import os
#print("Estoy parado en:", os.getcwd())

#Leer un archivo existente.

archivo = open("mensaje.txt", "r")
#Creamos una variable que se encarga de leer el archivo.
contenido = archivo.read()
#Mostramos el resultado.
print(contenido)
# Alternativa recomendada: usar with open() para que Python cierre el archivo automáticamente.
archivo.close()


#3️⃣ Guardar varios inputs en un archivo: Pedí al usuario que escriba tres frases.Guardalas en un archivo llamado frases.txt, una por línea.

#Pedimos las tres frases al usuario.
frase1 = input("Por favor ingresá la primera frase: ")
frase2 = input("Por favor ingresá la segunda frase: ")
frase3 = input("Por favor ingresá la tercera frase: ")
#Creamos una variable para abrir el archivo.
archivo = open("frases.txt", "a")
#Agregamos la información al archivo existente con archivo.write.
archivo.write(f"\n La primera frase es: {frase1}.\n La segunda frase es: {frase2}.\n La tercera frase es: {frase3}.")
#Cerramos el archivo.
archivo.close()
#Otra alternativa de resolverlo sin un f-string sería la siguiente:
#archivo.write(frase1 + "\n")
#archivo.write(frase2 + "\n")
#archivo.write(frase3 + "\n")
#Si el archivo está vacío, podemos evitar el primer salto de línea.


#🟡 Nivel 2: Con bucles y listas
#4️⃣ Guardar una lista de nombres

#Creá una lista con 5 nombres (pueden ser fijos o pedírselos al usuario).Guardá todos esos nombres en un archivo llamado nombres.txt, uno por línea.

# Creamos una lista con 5 nombres (pueden ser fijos o ingresados por el usuario)
lista_nombres = ["juan", "pedro", "pablo", "ezequiel", "ramon"]

# Abrimos el archivo 'nombres.txt' en modo escritura (esto crea el archivo si no existe)
# El modo 'w' sobreescribe el contenido si el archivo ya tiene algo.
archivo = open("nombres.txt", "w")

# Recorremos la lista nombre por nombre
for nombre in lista_nombres:
    # Escribimos cada nombre seguido de un salto de línea para que se guarde en líneas separadas
    archivo.write(nombre + "\n")

# Cerramos el archivo para guardar los cambios correctamente
archivo.close()


#5️⃣ Leer línea por línea con un bucle: Abrí el archivo nombres.txt y, usando un bucle, imprimí cada nombre agregando delante el texto: "Nombre:". Resultado esperado (si por ejemplo hay "Juan", "Pedro")

#Abrimos el archivo utilizando with open().
with open("nombres.txt", "r") as archivo:
    #Recorremos el archivo con un bucle for para iterar sobre cada línea dentro de nuestro archivo.
    for i in archivo:
        #Mostramos el resultado.
        print(f"Nombre: {i.strip()}")



#6️⃣ Crear un archivo de tabla de multiplicar: Pedí al usuario un número del 1 al 10. Generá la tabla de multiplicar de ese número y guardala en tabla.txt.
#Ejemplo (si el usuario pone 3):
#python-repl
#Copiar código
#3 x 1 = 3  
#3 x 2 = 6  

# Pedimos un número al usuario
entrada = int(input("Ingresá un número del 1 al 10 para hacer su tabla de multiplicar: "))

# Abrimos el archivo en la carpeta "semana-dos" en modo escritura.
with open("semana-dos/tabla.txt", "w") as archivo:
    # Recorremos los números del 1 al 10.
    for i in range(1, 11):
        # Escribimos cada línea de la tabla.
        archivo.write(f"{entrada} x {i} = {entrada * i}\n")


 
#🔵 Nivel 3: Condicionales y control de flujo + archivos

#7️⃣ Filtro de frases largas: Pedí 5 frases al usuario. Guardá solo las frases que tengan más de 20 caracteres en un archivo frases_largas.txt.

#Abrimos el archivo frases_largas.txt en modo escritura, "w" dentro de la carpeta semana dos.
#Si el archivo no existe, se crea; si existe, se sobreescribe.

with open("semana-dos/frases_largas.txt", "w") as archivo:
    #Usamos un bucle for para repetir 5 veces (Una vez por frase a ingresar).
    for i in range(1, 6):
        #Pedimos al usuario que ingrese una frase.
        frase = input("Ingresá una frases larga: ")
        #Verificamos si la frase tiene más de 20 caracteres
        if len(frase) > 20:
            #Si la frase es suficientemente larga, la escribimos en el archivo con un salto de línea.
            archivo.write(frase + "\n")



#8️⃣ Registro de intentos fallidos: Hacé un mini juego donde el usuario tiene que adivinar un número entre 1 y 5.
#Cada vez que falle, guardá el intento incorrecto en un archivo errores.txt.
#Cuando acierte, mostrá cuántos intentos fallidos hizo.

import random  # Importamos para generar el número aleatorio

# Generamos un número aleatorio entre 1 y 5
numero_secreto = random.randint(1, 5)

# Inicializamos el contador de fallos
intentos_fallidos = 0

# Abrimos el archivo errores.txt en modo escritura ('w')
# Si ya existe, se sobreescribe; si no, se crea
with open("semana-dos/errores.txt", "w") as archivo:
    
    while True:
        # Pedimos al usuario que adivine un número entre 1 y 5
        intento = int(input("Adiviná un número entre 1 y 5: "))
        
        # Verificamos si acertó
        if intento == numero_secreto:
            print(f"¡Correcto! Adivinaste el número. Fallaste {intentos_fallidos} vez/veces antes de acertar.")
            break  # Salimos del bucle
        else:
            print("Incorrecto. Probá de nuevo.")
            intentos_fallidos += 1  # Sumamos un fallo
            archivo.write(f"Intento fallido: {intento}\n")  # Registramos el fallo en el archivo



#🟣 Nivel 4: Lectura y procesamiento

#9️⃣ Contador de líneas: Leé el archivo nombres.txt que hiciste antes.Contá cuántas líneas tiene (es decir, cuántos nombres hay) y mostrale al usuario:
#Ejemplo: "El archivo tiene 5 nombres."

# Abrimos el archivo en modo lectura
with open("semana-dos/nombres.txt", "r") as archivo:
    
    # Leemos todas las líneas del archivo y las guardamos en una lista
    lineas = archivo.readlines()
    
    # Contamos cuántas líneas hay (es decir, cuántos nombres)
    cantidad_nombres = len(lineas)

# Mostramos el resultado al usuario
print(f"El archivo tiene {cantidad_nombres} nombre(s).")



#10️⃣ Buscador de palabras clave: En un archivo notas.txt, guardá 5 frases sobre cualquier tema.Luego pedile al usuario que escriba una palabra clave.Mostrale todas las líneas del archivo donde aparezca esa palabra.
#Ejemplo:
#Si la palabra clave es "Python" y hay una línea que dice "Me gusta programar en Python", entonces mostrala.

# Abrimos el archivo notas.txt en modo lectura
with open("semana-dos/notas.txt", "r", encoding='utf-8') as archivo:
    
    # Leemos todas las líneas del archivo
    lineas = archivo.readlines()

# Pedimos al usuario una palabra clave para buscar
clave = input("Ingresá una palabra clave para buscar en las frases: ")

# Recorremos cada línea del archivo
for linea in lineas:
    
    # Verificamos si la palabra clave está dentro de la línea (sin distinguir mayúsculas/minúsculas)
    if clave.lower() in linea.lower():
        
        # Si la contiene, la mostramos
        print(f"Coincidencia encontrada: {linea.strip()}")




#🟤 Nivel 5: Reto Divertido del Día

#11️⃣ Tu Diario Secreto 🗝️
#Cada vez que el usuario ejecute el programa, que pueda escribir una entrada nueva en su diario (una frase o párrafo).
#El programa debe guardar todas las entradas en el archivo diario.txt, agregándolas una debajo de la otra (modo append).
#Opcional: Al final podés agregar un comando que muestre todo el diario completo.

# 👤 Paso 1: Pedimos al usuario que escriba algo para su diario
# Puede ser una frase, un pensamiento, una idea del día, etc.
entrada = input("Escribí tu entrada de hoy para el diario: ")

# 📁 Paso 2: Abrimos (o creamos) el archivo 'diario.txt' en modo 'append'
# Esto significa que agregaremos contenido al final del archivo sin borrar lo que ya existía
with open("semana-dos/diario.txt", "a", encoding='UTF-8') as archivo:
    # ✍️ Paso 3: Escribimos la entrada seguida de un salto de línea para que quede separada
    archivo.write(entrada + "\n")

# 🧐 Paso 4: Preguntamos al usuario si quiere ver todo su diario completo
# Le damos la opción con una respuesta tipo 's' para sí, o cualquier otra para no
ver_diario = input("¿Querés ver todo tu diario completo? (s/n): ")

# 🖼️ Paso 5: Si el usuario respondió 's' (minúscula o mayúscula), mostramos el contenido entero
if ver_diario.lower() == "s":
    print("\n📖 Tu diario completo:\n")  # Encabezado visual simpático
    # 📖 Abrimos el archivo nuevamente, esta vez en modo lectura
    with open("semana-dos/diario.txt", "r") as archivo:
        # 👁️ Mostramos todo el contenido del archivo en pantalla
        print(archivo.read())