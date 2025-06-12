#📘 Día 6 – Ejercicios (Listas y Tuplas)
#1- Crear una lista con los nombres de 5 amigos. Mostrar el primer y el último nombre.

#Creamos una lista con 5 amigos.
lista_amigos = ["junior", "pedro", "juan", "daniela", "gustavo"]
#Imprimimos el resultado. 
print(lista_amigos[0], lista_amigos[-1])

#2- Pedir al usuario 3 comidas favoritas y guardarlas en una lista. Mostrar la lista completa.

#Creando una variable contenedora.
lista = []
#Pedimos el dato al usuario.
entrada_usuario = input("Por favor ingresá cuales son tus 3 comidas favoritas separadas por comas: ")
#Convertimos los datos ingresados a una lista.
lista = entrada_usuario.split(",")
#Imprimimos el resultado.
print(lista)


#3- Crear una lista con 6 números enteros. Mostrar el número mayor y el menor usando funciones de Python.

#Creamos una variable que contiene la lista.
lista = [1, 7, 2, 60, 13, 50]
#Creamos dos variables y usamos las funciones para ver cual número es mayor y cual menor.
num_mayor = max(lista)
num_menor = min(lista)
#Imprimimos el resultado.
print(f"El número mayor de la lista es: {num_mayor}, mientras que el número menor es: {num_menor}")



#4- Dada la lista colores = ["rojo", "azul", "verde", "amarillo"], mostrar todos los colores uno por uno usando un bucle.

#Creamos una variable que contiene una lista de colores.
lista_colores = ["rojo", "azul", "verde", "amarillo"]
#Utilizamos un bucle for para iterar cada elemento de la lista.
for color in lista_colores:
    #Mostramos el resultado en pantalla.
    print(f"Los colores de la lista son: {color}")

#5- Crear una tupla con 4 frutas. Mostrar el segundo elemento.

#Creamos una variable que contiene una tupla con frutas.
tupla = ("pera", "naranja", "kiwi", "melón")
#Mostramos el resultado utilizando el índice donde se encuentra el segundo elemento de la tupla.
print(tupla[1])


#6- Pedir al usuario 4 palabras y almacenarlas en una tupla. Mostrar toda la tupla.

#Pedimos al usuario 4 palabras(tiene diferentes formas de resolverse).
entrada_usuario = input("Por favor ingresá cuatro palabras separadas por comas: ")
#Creamos una variable que contiene la entrada del usuario y la convertimos a una lista .split()
lista_de_palabras = entrada_usuario.split(",")
#Creamos otra variable para convertir la lista a una tupla.
tupla_palabras = tuple(lista_de_palabras)
#Mostramos el resultado en pantalla.
print(tupla_palabras)


#7- Crear una lista de 5 números. Agregar un número al final y otro al principio. Mostrar la lista modificada.

#Creamos una variable que contiene una lista con números.
lista_numeros = [6, 12, 15, 10, 20]
#Creamos una variable contenedora que agrega un número al inicio.Empieza con el indice y luego el elemento.
inicio = lista_numeros.insert(0, 8)
#Creamos la variable para agregar un número al final;
final = lista_numeros.append(32)
#Mostramos el resultado.
print(lista_numeros)


#8- Eliminar el segundo elemento de la lista animales = ["perro", "gato", "pájaro", "pez"] y mostrar la lista resultante.

#Creamos una variable que contiene una lista de animales.
lista_animales = ["perro", "gato", "pájaro", "pez"]
#Creamos una variable para eliminar un elemento de la lista por su índice.
eliminando_elemento = lista_animales.pop(1)
#Mostramos el resultado.
print(lista_animales)


#9- Invertir una lista de números [1, 2, 3, 4, 5] y mostrar el resultado.

#Creando una variable que contiene una lista de números.
lista_numeros = [1, 2, 3, 4, 5, 6, 7]
#Ahora usamos la función .reverse() que invierte el contenido de la lista.
lista_numeros.reverse()
#Mostramos el resultado. [7, 6, 5, 4, 3, 2, 1]
print(lista_numeros)


#10- Contar cuántas veces aparece el número 3 en la lista [1, 3, 5, 3, 3, 2, 4].

#Creamos una lista con números desordenados y repetidos.
lista = [1, 3, 5, 3, 3, 2, 4, 3, 5]
#Usamos la función .count() para ver cuantas veces se repite el elemento dentro de la lista.
cantidad_repetición = lista.count(3)
#Mostramos el resultado.
print(cantidad_repetición)


#📝 Ejercicios combinados

#1️⃣- Pedir al usuario su nombre y edad. Guardarlos en un diccionario con las claves "nombre" y "edad". Luego, mostrar el contenido del diccionario.(Repasamos input(), diccionarios y print())

#Creamos una variable contenedora que almacena los datos ingresados al diccionario. 
diccionario = {}
#Pedimos los datos al usuario.
nombre = input("Ingresá tu nombre: ")
edad = int(input("Ingresá tu edad: "))
#Creamos una variable para convertir los datos ingresados a un diccionario.
diccionario = {"nombre": nombre, "edad": edad}
#mostramos el resultado.
print(diccionario)



#2️⃣- Crear una lista con 5 números enteros. Calcular la suma total de los elementos y mostrar el resultado.(Repasamos listas, operaciones matemáticas y funciones básicas como sum())

#Creamos la lista con números enteros.
lista = [4, 8, 12, 16, 20]
#Creamos una variable que va a contener la suma de los números dentro de la lista.
resultado = sum(lista)
#Mostramos el resultado.
print(resultado)


#3️⃣- Pedir al usuario que ingrese 4 colores separados por comas. Guardarlos en una tupla y luego mostrar el tercer color ingresado.(Repasamos input(), tuplas y acceso a elementos por índice)

#Pedimos los datos al usuario.
pedir_colores = input("Por favor ingresá 4 colores separados con #comas: ")
##Convertimos los datos ingresados a una lista.
lista_de_colores = pedir_colores.split(",")
#Convertimos la lista a una tupla.
tupla_colores = tuple(lista_de_colores)
#Mostramos el resultado.
print(f"El tercer color ingresado es: {tupla_colores[2]}")


#4️⃣- Crear una función que reciba una lista de números y devuelva el número mayor. Probarla con [10, 25, 3, 89, 54].(Repasamos funciones, listas y max())

#Creamos una función que contiene una lista de números.
def encontrar_mayor(lista_numeros):
    #Retornamos la lista y verficamos que número es el mayor.
    return max(lista_numeros)
#Creamos la lista.
lista_prueba = [10, 25, 3, 89, 54]
#Mostramos el resultado.
print(encontrar_mayor(lista_prueba))


#5️⃣- Crear una lista con 6 nombres y eliminar el tercer nombre usando pop(). Luego, imprimir la lista modificada.(Repasamos listas y métodos de modificación como pop())

#Creamos la lista con 6 nombres.
lista_nombres = ["juan", "pepe", "arnaldo", "sofía", "eduardo", "raquel"]
#Eliminamos .pop() el elemento según su índice.
eliminando_elemento = lista_nombres.pop(2)
#Mostramos el resultado.
print(lista_nombres)

