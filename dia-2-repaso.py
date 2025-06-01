#🧠 Repaso Día 1 - Variables, input, print, tipos de datos

#1-Crea una variable para tu nombre, edad y ciudad. Mostralo en una frase usando f-strings.
#nombre = "Ezequiel"
#edad = 37 
#ciudad = "Cabo Frío"
#print(f"El usuario se llama {nombre}, tiene {edad} años y vive en {ciudad}")

#2-Pedile al usuario su comida favorita y su color favorito. Mostrá un mensaje divertido con esa información.

#comida = input("Cuál es tu comida favorita? ")
#color = input("Cuál es tu color favorito? ")
#print(f"Pero que coincidencia, mi comida favorita tambien es la {comida}, pero que aburrido que te guste el color {color}")

#3-Mostrá el tipo de dato de:tu edad,tu altura (ej: 1.75),un valor como "True".

#mi_edad = 37 
#mi_altura = 1.87
#valor = True
#print(type(mi_edad))
#print(type(mi_altura))
#print(type(valor))

#🔢 Repaso Día 2 - Operaciones, conversión de tipos, len()
#1-Pedile al usuario dos números y mostrá la suma, resta, multiplicación y división.

#num1 = int(input("Pasáme el primer número: "))
#num2 = int(input("Pasáme el segundo número: "))
#print(f"El resultado de la suma es: {num1 + num2}, la resta es: {num1 - num2}, la multiplicación es: {num1 * num2}, y la división es: {round(num1 / num2)}, muy bien!!")

#2-Redondeá el resultado de una división a 2 decimales.

#division = 9 / 8
#redondeando_dos_decimales = round(division, 2)
#print(redondeando_dos_decimales)

#3-Calculá cuántos caracteres tiene una palabra que ingrese el usuario.

#frase = input("Por favor ingresa una frase: ")
#contando_caracteres = len(frase)
#print(f"Tu frase tiene {contando_caracteres} caracteres.")


#4-Convertí una cadena como "42" en número y sumale 8.

#cadena = int("42")
#suma = cadena + 8
#print(suma)

#🧪 Extra (opcional si estás cómodo/a)
#5-Mostrá el resultado de 5 + True y explicá por qué da eso.

#resultado = 5 + True 
#print(resultado)  #el resultado es 6 por que en python los valores booleanos son interpretados con valores de 1 para True y 0 para False, no se si es la respuesta al enunciado, pero no la sabía, lo busque y ahora lo sé.

#6-Sumá la edad de dos personas, pedida por teclado, y mostrá cuántos años tienen entre ambos.

#persona1 = int(input("Edad de la primera persona: "))
#persona2 = int(input("Edad de la segunda persona:" ))
#En este ejercicio no queda claro si se esta preguntando la suma de las edades de las dos personas y mostrar el resultado, o si mostrarlas por separado, en mi caso voy a sumar las edades de ambas. 

#print(f"La suma total entre las dos personas es: {persona1 + persona2}")

#########################################################################################################################
#########################################################################################################################

#🧠 Variables, entrada/salida, tipos de datos (Nivel 2)

#1. 🎤 Creador de perfiles:
#Pedile al usuario: nombre, edad, ciudad y hobby. Mostrale un mensaje como:
#"Hola Ezequiel, de 37 años, que vive en Cabo Frío y ama programar. ¡Bienvenido!"
nombre = input("Cuál es tu nombre: ")
edad = int(input("Cuál es tu edad: "))
ciudad = input("Donde vivís? ")
hobby = input("Cuál es tu hobby? ")
print(f"Hola {nombre}, de {edad}, que vive en {ciudad} y ama {hobby}. ¡Bienvenido!")

#2. 🔁 Intercambio de valores:
#Creá dos variables con valores de texto (ej: a = "sol", b = "luna") y luego intercambiá sus valores sin crear nuevas variables. Mostrá el resultado antes y después del cambio.
sol, luna = "sol", "luna"
sol, luna = luna, sol
print("sol:", sol) 
print("luna:", luna) #aclaración, no lo entendí y lo resolví con IA

#3. 🧮 Tipos misteriosos:
#¿Qué tipo de dato es el resultado de estas operaciones? Mostralo con type() y explicá por qué:

print(type("12" + "8")) #Como resultado el tipo de dato es str, ya que se estan sumando dos string
print(type(5 + 3.0)) #Como resultado da un dato de tipo flotante ya que es el producto entre una suma de un entero y un flotante
print(type(len("Python") > 3)) #Como resultado devuelve un tipo de dato booleano ya que la pregunta es que se está mostrando una cadena de caracteres y le esta preguntando si la cantidad de caracteres es mayor que el str.

#🔢 Operaciones, conversiones, len() (Nivel 2)

#4. 💸 Calculadora de propinas:
#Pedile al usuario:el total de una cuenta (ej: 1500),el porcentaje de propina que quiere dejar (ej: 10).Mostrá cuánto debería dejar de propina y el total final con propina incluida. 

usuario = int(input("Cuánto dinero es la cuenta del restaurante? "))
porcentaje_propina = int(input("Que porcentaje de propina te gustaria dejar? "))
propina = round(usuario * (porcentaje_propina / 100))
total_a_pagar_con_propina = round(usuario + propina)
print(f"El total de lo consumido es: {usuario}, la propina es de {propina} y el gasto total sería de {total_a_pagar_con_propina}")

#5. 📏 Longitud de palabras múltiples:Pedile al usuario 3 palabras (una por input()) y mostrá cuántos caracteres tiene cada una. Usá len() para cada una, y mostralo con un f-string.
# Pedir los valores al usuario
palabra1 = input("Dáme la primera palabra: ")
palabra2 = input("Dáme la segunda palabra: ")
palabra3 = input("Dáme la tercera palabra: ")

print(F"La primera palabra tiene {len(palabra1)} caracteres, la segunda palabra {len(palabra2)} y la tercera tiene {len(palabra3)} caracteres")


