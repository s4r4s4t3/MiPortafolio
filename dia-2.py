#Dia 2: Operaciones basicas y conversion de tipos
#Temas: operadores matematicos, conversion con int(), float(), round(), len().
#Objetivo: Aprender a operar con numeros y a convertir tipos de datos.
#Plan Intensivo de 30 Días - Python para Principiantes
#[EJERCICIO] Ejercicios:
#- Suma, resta, multiplicacion, division entre numeros ingresados por el usuario.
#- Redondear resultados.
#- Contar caracteres con len().



#- Sumas básicas
# 1  - Escribe un programa que sume dos números fijos, por ejemplo, 5 + 3.

num1 = 20
num2 = 5
suma = num1 + num2 
print(suma)

# 2    - Luego, intenta con números ingresados por el usuario.

num1 = int(input("por favor ingresa el primer número: "))
num2 = int(input("Por favor ingresa el segundo número: "))
resultado = num1 + num2
print(f"El resultado de la suma es: {resultado}")

#- Restas y multiplicaciones
#3- Resta dos números como 10 - 4.

a = 8
b = 12
c = a - b
print(c)

#4- Multiplica dos valores, como 6 × 2.
x = 5
y = 10
z = x * y 
print(z)

#5- Luego, deja que el usuario ingrese los números.
num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))
resultado = num1 * num2
print(f"El resultado de la multiplicación es: {resultado}")

#- División y redondeo

#6- Divide 9 entre 2 y usa round() para redondear el resultado.
a = 9
b = 2
c = round(a / b)
print(c)

#7- Luego, intenta con otros números ingresados por el usuario.
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
resultado = round(num1 / num2)
print(f"El resultado de la división redondeada es, {resultado}")

#- Conversión de tipos

#8- Convierte un número ingresado como texto (input()) a int o float.
numero = float(input("Por favor ingrese un numero con decimales: "))
print(f" El número ingresado es: {numero}")

#9- Prueba con un número decimal y conviértelo a entero con int().
numero = float(input("Por favor ingrese un numero con decimales: "))
resultado = round(numero)
print(f" El número ingresado es: {resultado}")

#- Contar caracteres en un texto

#10- Pide al usuario su nombre y usa len() para contar los caracteres.
nombre = input("Por favor ingrese su nombre: ")
resultado = len(nombre)
print(f"La cantidad de caracteres que tiene tu nombre es: {resultado} ")

#11- Luego, intenta con frases más largas.

frase = input("Por favor ingrese su un mensaje personalizado: ")
resultado = len(frase)
print(f"La cantidad de caracteres que tiene tu frase es: {resultado} ")



