# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 12:23:07 2024

@author: HP
"""

#%% Práctica de Python: Funciones y Excepciones
# En esta práctica, trabajaremos con excepciones y validaciones en Python.

# Manejo de Excepciones en Python
# try:
#     <código>
# except:
#     <código>
# El bloque try ejecuta código, y si ocurre una excepción, se gestiona en el bloque except.

#%% Validación de número entero
# Validar el ingreso de números enteros
def validar_entero():
    """
    Solicita un número entero al usuario y valida su entrada.
    """
    while True:
        try:
            num = int(input("Ingrese un número entero: "))
            print(f"El número ingresado es {num}")
            break
        except ValueError:
            print("Error: Debe ingresar un número entero. Intente nuevamente.")

validar_entero()

#%% Validación de número entero positivo
# Validar el ingreso de números enteros positivos
def validar_entero_positivo():
    """
    Solicita un número entero positivo al usuario y valida su entrada.
    """
    while True:
        try:
            num = int(input("Ingrese un número entero positivo: "))
            if num < 0:
                raise ValueError("El número no es positivo.")
            print(f"El número ingresado es {num}")
            break
        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.")

validar_entero_positivo()
#%% TÍTULO Y DESCRIPCIÓN
# Estructura Funciones
# La creación de funciones permite organizar mejor el código, evitar repeticiones
# y dividir programas largos en partes manejables.

#%% FUNCIÓN PRINCIPAL
def main():
    """
    Función principal.
    """
    print("Bienvenido al programa principal.")

# Ejecutamos la función principal
if __name__ == '__main__':
    main()

#%% EJEMPLO: PROGRAMA CON MENÚ
# Librería necesaria para limpiar pantalla
import os

def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menú.
    """
    os.system('clear')  # Limpia pantalla (funciona en terminal, no en Spyder)
    titulo = "Menú General"
    print(titulo.center(50, '*'))
    print("\n\n")
    print("Selecciona una Opción:")
    print("\t1 - Primera Opción")
    print("\t2 - Segunda Opción")
    print("\t3 - Tercera Opción")
    print("\t9 - Salir")

def validar():
    """
    Función que valida la selección del usuario.
    """
    while True:
        menu()
        opcionMenu = input("Inserta un número: ")
        if opcionMenu == "1":
            input("Has pulsado la opción 1...\nPulsa una tecla para continuar.")
        elif opcionMenu == "2":
            input("Has pulsado la opción 2...\nPulsa una tecla para continuar.")
        elif opcionMenu == "3":
            input("Has pulsado la opción 3...\nPulsa una tecla para continuar.")
        elif opcionMenu == "9":
            print("Saliendo del programa...")
            break
        else:
            input("Opción incorrecta...\nPulsa una tecla para continuar.")

# Ejecutamos la validación
if __name__ == '__main__':
    validar()
    print('\tFINALIZÓ EL PROGRAMA!!!!!')
