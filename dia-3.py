#🔽 Día 3 – Condicionales en Python
#Temas: if, elif, else. Comparaciones con >, <, ==, !=
#Objetivo: Tomar decisiones con logica.

#🟢 Nivel 1 – Básico (Calentamiento)

#1-Pedí un número al usuario y decí si es mayor que 10.
usuario = int(input("Por favor ingresá un número: "))

if usuario > 10:
    print("El número es mayor a 10")
elif usuario == 10:
    print("El numero es igual a 10")    
else:
    print("El número es menor que 10")

#2-Preguntá la edad de una persona y decí si es mayor o menor de edad.

edad = int(input("Por favor ingresá tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

#3-Pedí una palabra y decí si tiene más de 5 caracteres.

caracteres = input("Por favor ingresá una palabra: ")
if len(caracteres) > 5:
    print("La palabra tiene más de 5 caracteres.")
elif len(caracteres) == 5:
    print("La palabra tiene 5 caracteres.")
else:
    print("La palabra tiene menos de 5 caracteres.")

#4-Pedí un número y decí si es positivo, negativo o cero.

pedir_numero = int(input("Por favor ingresá un número: "))
if pedir_numero > 0:
    print("El número ingresado es positivo.")
elif pedir_numero < 0:
    print("El número ingresado es negativo.")
else:
    print("El número ingresado es 0.")

#5-Pedí un número y decí si es par o impar.

entrada = int(input("Por favor, ingresá un número: "))
if entrada % 2 == 0:
    print("El número ingresado es par.")
else:
    print("El número ingresado es impar.")

#🟡 Nivel 2 – Práctico y útil

#1-Preguntá al usuario una contraseña. Si es correcta, mostrale “Acceso concedido”; si no, “Contraseña incorrecta”.

password = "12345"
contraseña = input("Por favor ingresá tu contraseña: ")
if contraseña == password:
    print("La contraseña es correcta.")
else:
    print("La contraseña ingresada es incorrecta, por favor intente nuevamente.")

#2- Pedí la temperatura actual. Si es menor a 10°, decí “Hace frío”; si está entre 10 y 25, “Clima agradable”; si es mayor, “Hace calor”.

temperatura = int(input("Cuántos grados esta haciendo en este momento? "))
if temperatura < 10:
    print("Hace mucho frío!!")
elif 10 <= temperatura <= 25:
    print("El clima está agradable....")
else:
    print("Está haciendo mucho calor!!")

#3- Pedí el nombre de una persona. Si se llama “Ezequiel”, decí “¡Qué nombre tan genial!”.

nombre = input("Por favor ingresá tu nombre: ")
if nombre == "Ezequiel":
    print("Qué nombre tan genial!!")
else:
    print("Es un lindo nombre..")

#4- Preguntá cuánto dinero tiene alguien y decí si puede comprar un producto de $500.

ahorros = int(input("Cuánto dinero tenes ahorrado? "))
if ahorros >= 500:
    print("Podés comprarte esa tablet que tanto querías, felicidades!!")
else:
    print("El dinero que tenés no es suficiente, lo lamento.")

#5- Pedí dos números y mostrale al usuario cuál es mayor (o si son iguales).

es_menor = int(input("Por favor, ingresá el primer número: "))
es_mayor = int(input("Por favor, ingresá el segundo número: "))
if es_menor < es_mayor:
    print(f"El número {es_menor} es menor que {es_mayor}")
elif es_menor > es_mayor:
    print(f"El número {es_menor} es mayor que {es_mayor}")
else:
    print("Los números ingresados son iguales..")

#🟠 Nivel 3 – Condiciones compuestas

#1- Pedí edad y nacionalidad. Si la persona es mayor de 18 y argentina, decí “Podés votar”.

edad = int(input("¿Cuál es tu edad? "))
nacionalidad = input("¿Cuál es tu nacionalidad? ")

if edad >= 18 and nacionalidad == "argentina":
    print("Podés votar.")
else:
    print("No podés votar.")

#2- Pedí una letra. Decí si es una vocal o consonante (considerá solo minúsculas).

letra = input("Por favor ingresá una letra: ")
if letra in ["a","e","i","o","u"]:
    print("La letra ingresada es una vocal.")
else:
    print("La letra ingresada es una consonante.")

#3- Pedí un número. Si está entre 1 y 100 (inclusive), decí “Número válido”; si no, “Fuera de rango”.

numero = int(input("Me gustaría que ingreses un número: "))
if numero >= 1 and numero <=100:
    print("Número válido!")
else:
    print("Número fuera de rango..")

#4- Pedí dos números. Si ambos son pares, decí “Ambos pares”. Si ambos son impares, decí “Ambos impares”. Si son distintos, decí “Uno par y otro impar”.

num1 = int(input("Por favor dáme un primer número: "))
num2 = int(input("Por favor dáme un segundo número: "))
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos son pares.")
elif num1 % 2 == 1 and num2 % 2 == 1:
    print("Ambos son impares.")
else:
    print("Uno es par y el otro impar.")
#5- Preguntá si tiene pasaporte y si tiene visa. Si tiene ambos, decí “Podés viajar a EE.UU.”.

pasaporte = input("Tenés pasaporte? ")
visa = input("Tenés visa? ")
if pasaporte == "si" and visa == "si":
    print("Podés viajar a Estados Unidos!!")
else:
    print("No podés viajar ya que no cumplís con los requerimientos.")

#🔴 Nivel 4 – Retadores y creativos

#1- Pedí al usuario una nota (0 a 10). Mostrá un mensaje:0–5: “Desaprobado” 6–7: “Aprobado” 8–9: “Muy bien” 10: “Excelente”

nota = int(input("Querido alumno, que nota sacaste en el exámen? "))
if nota < 0 or nota > 10:
    print("Error, la nota tiene que ser entre cero y diez.")
elif nota >= 0 and nota <= 5:
    print("Desaprobado") 
elif nota >= 6 and nota <= 7:
    print("Aprobado")
elif nota >= 8 and nota <= 9:
    print("Muy bien!!")
else:
    print("Excelente!!!")

#2- Pedí tres números y mostrale cuál es el mayor.

num1 = int(input("Dame el primer número: "))
num2 = int(input("Dame el segundo número: "))
num3 = int(input("Dame el tercer número: "))
if num1 > num2 and num1 > num3:
    print(f"El número mayor es {num1}")
elif num2 > num1 and num2 > num3:
    print(f"El número mayor es {num2}")
else:
    print(f"El número mayor es {num3}")
    
#3- Pedí una palabra y decí si es palíndroma (ej: “radar”, “oso”)

palabra = input("Ingresá una palabra: ")

# Comparamos la palabra con su versión invertida

if palabra == palabra[::-1]: # → Invierte la palabra.
    print("La palabra es palíndroma.")
else:  
    print("La palabra no es palíndroma.")


#4- Pedí el año de nacimiento y decí si la persona es mayor de 18 (usá el año actual: 2025).

mayor_de_edad = int(input("Por favor ingresá tu año de nacimiento: "))
if 2025 - mayor_de_edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad..")

#5- Pedí si llueve (sí o no) y si tiene paraguas (sí o no). Mostrá: Si llueve y tiene paraguas: “Podés salir tranquilo”. Si llueve y no tiene: “Mejor quedate en casa”. Si no llueve: “Buen día para salir”.

lluvia = input("¿Está lloviendo? ")
paraguas = input("¿Tenés paraguas? ")
if lluvia == "si" and paraguas == "si":
    print("Podés salir tranquilo.")
elif lluvia == "si" and paraguas == "no":
    print("Mejor quedarse en casa.")
else:
    print("Buen día para salir!!")





