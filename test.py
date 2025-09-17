print("¡Hola Automation Tester!")

#nombre = input("Ingresa tu nombre: ")
#edad = int(input("Ingresa tu edad: "))
#profesion = input("Ingresa tu profesion: ")
#print("Hola " + nombre + ", tienes " + str(edad) + " años y tu profesion es " + profesion)

print(10 // 5) # División entera, si se usa solo un / se obtiene un float 2.0

for i in range(0, 21, 2): # range(start, stop, step) Genera una secuencia de números desde start hasta stop-1, con un paso de step (de cuánto en cuánto aumentar). 
    print(i) # Imprime del 0 al 20, de 2 en 2
    
for i in range(1, 10):
    print(i) # Imprime del 1 al 9, el 10 no se incluye
    
for i in range(11):
    if i == 5:
        break
    print(i) # Imprime del 0 al 4, cuando i es igual a 5 se detiene el ciclo por el break

# Listas - mutables
mi_lista = ["manzana", 200, True, 15.5]
print(mi_lista[0]) # Acceder al primer elemento de la lista

mi_lista.append("naranja") # Agregar un elemento al final de la lista
print(mi_lista)

mi_lista.remove(200) # Eliminar un elemento de la lista
print(mi_lista)

mi_lista[1] = "pera" # Modificar un elemento de la lista
print(mi_lista) # Imprime la lista modificada

for i in mi_lista:
    print(i) # Imprime cada elemento de la lista    



# Tuplas - inmutables
mi_tupla = ("banana", 300, 25.5)



# Diccionarios - pares clave-valor
persona = {
    "nombre": "Carlos",
    "edad": 28,
    "ciudad": "Madrid"
}
print(persona["nombre"]) # Acceder al valor asociado a la clave "nombre"
persona["edad"] = 54 # Modificar el valor asociado a la clave "edad"

print(persona.keys())  # Imprime todas las claves del diccionario
print(persona.values())  # Imprime todos los valores del diccionario
print(persona.items())  # Imprime todos los pares clave-valor del diccionario


# Funciones
def saludo(nombre):
    return(f"Hola, {nombre}!")
print (saludo("Ana")) # Llamar a la función con el argumento "Ana"


#Modularización
def suma(a, b):
    return a + b

def calculadora_simple(operacion, a, b):
    if operacion == "suma":
        return suma(a, b)
    else:
        return "Operación no válida"



# Manejo de excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

try:
    numero = int("hola")
except ValueError as e:
    print(f"Error: {e}")

try:
    print(persona["color"])
except KeyError as e:
    print(f"Error: La clave no existe")