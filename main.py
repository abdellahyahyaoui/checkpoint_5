
#crear bucle
for i in range(1, 11):
  print(i)


# Crear una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
a = 60
b = 90
c = 80

def suma(a, b, c):
    return a + b + c

print(suma(a, b, c))
# Crear una función lambda con la misma funcionalidad que la función de suma que acaba de crear.


suma_lambda = lambda a, b, c: a + b + c
print(suma_lambda(a, b, c))


# Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista.
nombre = 'Enrique'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

# Comprobando si el valor de la variable nombre coincide con algún valor de la lista_nombre.

# solucion_1

coincide = False
for n in lista_nombre:
    if nombre == n:
        coincide = True
        break

if coincide:
    print("el valor de la variable nombre coincide con algún valor de la lista_nombre.")
else:
    print("el valor de la variable nombre no coincide con algún valor de la lista_nombre.")

# solucion_2

if lista_nombre.count(nombre) > 0:
  print("el valor de la variable nombre coincide con algún valor de la lista_nombre.")
else:
  print("el valor de la variable nombre no coincide con algún valor de la lista_nombre.")





#------------------------------ejemplos de la preguntas teoricas--------------------------------



#---------------------------------------- condicionales--------------


#Verificar si un número es positivo, negativo o cero:


numero = 10

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")


#Verificar si un número es par o impar

numero = 15

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

#Determinar si un año es bisiesto:

año = 2024

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")

#Determinar si un número es primo

numero = 17
es_primo = True

if numero < 2:
    es_primo = False
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print("El número es primo")
else:
    print("El número no es primo")



#------------------------------------------ bucles en Python-------------------------


# Bucle for para imprimir números del 1 al 5
print("Bucle for:")
for numero in range(1, 6):
    print(numero)

# Bucle for para iterar sobre una lista e imprimir cada elemento
print("\nIterar sobre una lista:")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

# Bucle for para iterar sobre una cadena e imprimir cada carácter
print("\nIterar sobre una cadena:")
cadena = "Python"
for caracter in cadena:
    print(caracter)

# Bucle for para iterar sobre una lista de tuplas e imprimir cada par de valores
print("\nIterar sobre una lista de tuplas:")
puntos = [(1, 2), (3, 4), (5, 6)]
for x, y in puntos:
    print(f"x: {x}, y: {y}")

# Bucle while para imprimir números del 1 al 5
print("\nBucle while:")
numero = 1
while numero <= 5:
    print(numero)
    numero += 1






#-----------------------------------listas de comprencion---------------------------------


# Lista por comprensión para obtener los cuadrados de los primeros 5 números enteros
cuadrados = [x**2 for x in range(1, 6)]

# Lista por comprensión para obtener los cubos de los números pares del 1 al 10
cubos_pares = [x**3 for x in range(2, 11, 2)]

# Lista por comprensión para obtener los números impares del 1 al 10
impares = [x for x in range(1, 11) if x % 2 != 0]

# Lista por comprensión para convertir una lista de cadenas a mayúsculas
nombres = ["juan", "maría", "pedro"]
nombres_mayusculas = [nombre.upper() for nombre in nombres]

# Lista por comprensión para filtrar elementos de una lista
numeros = [10, 20, 30, 40, 50]
numeros_pares = [num for num in numeros if num % 2 == 0]

# Lista por comprensión para crear una lista de tuplas
pares = [(x, y) for x in range(1, 4) for y in range(1, 4)]


# Lista por comprensión para obtener las vocales de una cadena
cadena = "Python es genial"
vocales = [char for char in cadena if char.lower() in "aeiou"]

# Lista por comprensión para crear una lista de listas
matriz = [[i*j for j in range(1, 4)] for i in range(1, 4)]

# Imprimir todas las listas resultantes
print("Cuadrados:", cuadrados)
print("Cubos de pares:", cubos_pares)
print("Números impares:", impares)
print("Nombres en mayúsculas:", nombres_mayusculas)
print("Números pares:", numeros_pares)
print("Pares de números:", pares)
print("Vocales en la cadena:", vocales)
print("Matriz:", matriz)



#-----------------------------------argumentos------------------------------------


# Función con argumento posicional
def saludar(nombre):
    print("¡Hola,", nombre, "!")

saludar("Juan")

# Función con argumento de palabra clave
def presentar(nombre, edad):
    print("Hola, soy", nombre, "y tengo", edad, "años.")

presentar(nombre="María", edad=25)

# Función con argumento por defecto
def saludar_por_defecto(nombre="Mundo"):
    print("Hola,", nombre, "!")

saludar_por_defecto()
saludar_por_defecto("Python")

# Función con argumentos arbitrarios *args
def sumar(*args):
    total = 0
    for num in args:
        total += num
    return total

resultado = sumar(1, 2, 3, 4, 5)
print("La suma es:", resultado)

# Función con argumentos arbitrarios **kwargs
def mostrar_informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(clave + ":", valor)

mostrar_informacion(nombre="Juan", edad=30, ciudad="Madrid")

# Función con argumentos mixtos
def mostrar_datos(nombre, *args, **kwargs):
    print("Nombre:", nombre)
    print("Otros datos:", args)
    print("Información adicional:", kwargs)

mostrar_datos("María", 25, "Madrid", email="maria@example.com", telefono="123456789")



#-----------------------------------------------funciones lambda------------------------


# Ejemplo 1: Función lambda para sumar dos números
suma = lambda a, b: a + b
print("Suma:", suma(3, 5))

# Ejemplo 2: Función lambda para calcular el cuadrado de un número
cuadrado = lambda x: x**2
print("Cuadrado:", cuadrado(4))

# Ejemplo 3: Función lambda para ordenar una lista de tuplas por el segundo elemento
puntos = [(1, 2), (3, 1), (5, 4), (2, 3)]
puntos_ordenados = sorted(puntos, key=lambda x: x[1])
print("Puntos ordenados:", puntos_ordenados)

# Ejemplo 4: Función lambda para filtrar números pares de una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", pares)

# Ejemplo 5: Función lambda para multiplicar dos números y sumar otro
operacion = lambda x, y, z: (x * y) + z
print("Operación:", operacion(2, 3, 5))











  


