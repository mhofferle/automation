#Modularización
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def dividir(a, b):
    if b != 0:
        return a // b

def calculadora_simple(operacion, a, b):
    try: 
        a = int(a)
        b = int(b)
        if operacion == "sumar":
            return sumar(a, b)
        elif operacion == "restar":
            return restar(a, b)
        elif operacion == "dividir":
            return dividir(a, b)
        else:
            return KeyError("Operación no válida")
    except ZeroDivisionError:
        return "Error: División por cero"
    except ValueError:
        return "Error: Valores deben ser numéricos"


usuarios = {
    "ana": {"edad": 50},
    "juan": {"edad": 80}
}

def obtener_edad():
    try:
        nombre = input("Ingrese el nombre del usuario: ")
        edad = usuarios[nombre]["edad"]
        print(f"{nombre} tiene {edad} años.")
    except KeyError:
        print("Error: Usuario no encontrado")


