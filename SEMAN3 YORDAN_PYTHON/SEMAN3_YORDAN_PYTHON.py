def ejer1():
    nombre = input("Ingrese su nombre: ")
    carrera = input("Ingrese su carrera: ")

    print(f"\n{nombre}, Bienvenido al curso de Fundamentos de Algoritmo de la carrera{carrera}")

def ejer2():
    print("\"Leonardo\"")

def ejer3():
    num1 = int(input("Ingrese número1: "))
    num2 = int(input("Ingrese número2: "))

    print("Suma: ", (num1+num2))
    print("Resta: ", (num1-num2))
    print("Multiplicación: ", (num1*num2))
    print("División: ", (num1/num2))

import math #importando libreria math

def ejer4():
    num = float(input("Ingrese número decimal: "))

    raiz = math.sqrt(num)
    redo = round(num,2)
    cubo = math.pow(num,3)
    cubica = num ** (1/3)

    print("Raiz cuadrada: ",raiz)
    print("Redondeado: ",redo)
    print("Al cubo: ",cubo)
    print("Raiz cubica: ",cubica)

def ejer5():
    num = input("Ingrese un número: ")

    entero = int(num)
    decim = float(num)

    print("Resto: ",(entero%2))
    print("Decimal: ",(decim/3))

ejer5()