#📘 Día 7 – Diccionarios y Repaso
#🔑 Temas:
#Diccionarios (dict)
#Claves y valores
#Acceso y modificación
#Repaso general (listas, tuplas, funciones, condicionales)

#🧠 Objetivo:
#Aprender a asociar claves con valores usando diccionarios y consolidar lo aprendido en los primeros 6 días.

#📝 Ejercicios del Día 7

#1- Crear una ficha personal usando un diccionario
#Guardar nombre, edad, ciudad y ocupación. Mostrar el contenido con print().

#Creamos una variable contenedora para nuestra ficha personal.
ficha_personal = {}
#Pedimos los datos al usuario.
nombre = input("Ingresá tu nombre: ")
edad = int(input("ingresá tu edad: "))
ciudad = input("Ingresá tu ciudad: ")
ocupacion = input("Ingresá tu ocupación: ")
#Almacenamos los datos ingresados por el usuario en la variable contenedora.
ficha_personal = {"Nombre": nombre, "Edad": edad, "Ciudad": ciudad, "Ocupación": ocupacion}
#Mostramos el resultado.
print(ficha_personal)


#2- Modificar el valor de una clave en el diccionario anterior
#Cambiar la ciudad por otra y mostrar el resultado actualizado.

#Creamos una variable contenedora para nuestra ficha personal.
ficha_personal = {}
#Pedimos los datos al usuario.
nombre = input("Ingresá tu nombre: ")
edad = int(input("ingresá tu edad: "))
ciudad = input("Ingresá tu ciudad: ")
ocupacion = input("Ingresá tu ocupación: ")
#Almacenamos los datos ingresados por el usuario en la variable contenedora.
ficha_personal = {"Nombre": nombre, "Edad": edad, "Ciudad": ciudad, "Ocupación": ocupacion}
#Cambiamos la ciudad ingresada por el usuario, por otra. Modificando el resultado final.
ficha_personal["Ciudad"] = "Brasilia"
#Mostramos el resultado.
print(ficha_personal)



#3- Agregar una nueva clave al diccionario
#Por ejemplo, "email", y asignarle un valor.

#Creamos la variable contenedora.
diccionario = {}
#Pedimos los datos al usuario.
nombre = input("Ingresá tu nombre: ")
edad = int(input("Ingresá tu edad: "))
ciudad = input("Ingresá tu ciudad: ")
ocupacion = input("Ingresá tu ocupación: ")
#Guardamos los valores ingresados en la variables contenedora.
diccionario = {"nombre": nombre, "edad": edad, "ciudad": ciudad, "ocupación": ocupacion}
#Agregamos una clave valor a nuestro diccionario.
diccionario["email"] = "salud@gmail.com"
#Mostramos el resultado.
print(diccionario)



#4- Eliminar una clave del diccionario
#Usar del para eliminar "ocupación".

#Creamos la variable contenedora.
diccionario = {}
#Pedimos los datos al usuario.
nombre = input("Ingresá tu nombre: ")
edad = int(input("Ingresá tu edad: "))
ciudad = input("Ingresá tu ciudad: ")
ocupacion = input("Ingresá tu ocupación: ")
#Guardamos los valores ingresados en la variables contenedora.
diccionario = {"nombre": nombre, "edad": edad, "ciudad": ciudad, "ocupación": ocupacion}
#Eliminamos una clave de nuestro diccionario.
del diccionario["ocupación"]
#Mostramos el resultado.
print(diccionario)


#5- Verificar si una clave existe en el diccionario
#Usar in para ver si existe "email" y mostrar un mensaje adecuado.

#Creamos el diccionario.
diccionario = {
    "nombre": "pepe",
    "ciudad": "san justo",
    "email": "pepe@gmail.com"
}
#Guardamos en una variable la clave que queremos verificar en nuestro diccionario.
clave = "email"
#Usamos el condicional if, para comprobar si la clave está en el diccionario.
if clave in diccionario:
    #Mostramos el resultado.
    print(f"La clave {clave} se encuentra en el diccionario.")
#En caso de no encontrarse la clave, mostramos el mensaje.
else:
    print(f"La clave {clave} no se encuentra en el diccionario")



#6- Recorrer el diccionario mostrando claves y valores
#Usar un bucle for.

#Creamos el diccionario.
diccionario = {
    "nombre": "pepe",
    "ciudad": "san justo",
    "email": "pepe@gmail.com"
}
#Usamos un for para iterar sobre nuestro diccionario.
for clave, valor in diccionario.items():
    #Mostramos el resultado.
    print(f"Clave: {clave} -> valor {valor}")


#7- Crear una función que reciba un diccionario con datos personales y lo muestre ordenado
#(clave: valor por línea).

def diccionario(datos):
    for clave, valor in sorted(datos.items()):
        print(f"-> {clave} <- -> {valor} <-")
datos_personales = {
    "nombre": "pepe",
    "ciudad": "san justo",
    "email": "pepe@gmail.com"
}

diccionario(datos_personales)


#8- Repaso: Pedir al usuario nombre, edad, 3 colores favoritos y guardarlo todo en un diccionario.
#Los colores pueden almacenarse como una lista dentro del diccionario. Luego mostrar el contenido completo.

diccionario = {} 
nombre = input("Ingresá tu nombre: ")
edad = int(input("Ingresá tu edad: "))
colores = input("Ingresá tres colores favoritos separados con comas: ")
lista_colores = colores.split(",")
diccionario = {f"nombre": nombre, "edad": edad, "colores": lista_colores}
print(diccionario)


