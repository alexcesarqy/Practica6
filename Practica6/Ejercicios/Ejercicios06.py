# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 13:05:20 2024

@author: HP
"""
# Ejercicios
#%% Números Pares, Impares y Primos
# Este programa permite realizar operaciones sobre un rango de números.
# Opciones del menú:
# 1. Ingresar números de inicio y fin del rango.
# 2. Imprimir los números pares del rango.
# 3. Imprimir los números impares del rango.
# 4. Imprimir los números primos del rango.
# 5. Salir.

#%% Función para obtener números pares
def obtener_pares(inicio, fin):
    """Devuelve una lista de números pares en el rango [inicio, fin]."""
    return [num for num in range(inicio, fin + 1) if num % 2 == 0]

#%% Función para obtener números impares
def obtener_impares(inicio, fin):
    """Devuelve una lista de números impares en el rango [inicio, fin]."""
    return [num for num in range(inicio, fin + 1) if num % 2 != 0]

#%% Función para verificar si un número es primo
def es_primo(numero):
    """Verifica si un número es primo."""
    if numero < 2:
        return False
    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:
            return False
    return True

#%% Función para obtener números primos
def obtener_primos(inicio, fin):
    """Devuelve una lista de números primos en el rango [inicio, fin]."""
    return [num for num in range(inicio, fin + 1) if es_primo(num)]

#%% Función principal con el menú
def main():
    while True:
        print("\n*** Menú de Opciones ***")
        print("1. Ingresar números de inicio y fin del rango.")
        print("2. Imprimir los números pares del rango.")
        print("3. Imprimir los números impares del rango.")
        print("4. Imprimir los números primos del rango.")
        print("5. Salir.")

        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                inicio = int(input("Ingrese el número de inicio del rango: "))
                fin = int(input("Ingrese el número de fin del rango: "))
            elif opcion == 2:
                print("Números pares:", obtener_pares(inicio, fin))
            elif opcion == 3:
                print("Números impares:", obtener_impares(inicio, fin))
            elif opcion == 4:
                print("Números primos:", obtener_primos(inicio, fin))
            elif opcion == 5:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción no válida, intente nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")
        except NameError:
            print("Error: Ingrese primero el rango de números (opción 1).")

#%% Ejecutar la función principal
if __name__ == "__main__":
    main()
#%% Tabla de Multiplicar
# Este programa permite trabajar con tablas de multiplicar y un rango de números.

#%% Función para imprimir una tabla de multiplicar
def imprimir_tabla(numero):
    """Imprime la tabla de multiplicar del número dado."""
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

#%% Función para imprimir tablas de números en un rango
def imprimir_tablas_rango(inicio, fin, condicion):
    """
    Imprime tablas de multiplicar para números en el rango [inicio, fin].
    La condición determina si son números pares o impares.
    """
    for numero in range(inicio, fin + 1):
        if condicion(numero):
            imprimir_tabla(numero)

#%% Función principal con el menú
def main():
    while True:
        print("\n*** Menú de Opciones ***")
        print("1. Ingresar rango de números.")
        print("2. Imprimir tablas de multiplicar para números pares.")
        print("3. Imprimir tablas de multiplicar para números impares.")
        print("4. Imprimir tabla de multiplicar para un número específico.")
        print("5. Salir.")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                inicio = int(input("Ingrese el número de inicio del rango: "))
                fin = int(input("Ingrese el número de fin del rango: "))
                print("Rango establecido correctamente.")
            elif opcion == 2:
                imprimir_tablas_rango(inicio, fin, lambda x: x % 2 == 0)
            elif opcion == 3:
                imprimir_tablas_rango(inicio, fin, lambda x: x % 2 != 0)
            elif opcion == 4:
                numero = int(input("Ingrese el número para imprimir su tabla de multiplicar: "))
                imprimir_tabla(numero)
            elif opcion == 5:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción no válida, intente nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")
        except NameError:
            print("Error: Ingrese primero el rango de números (opción 1).")

#%% Ejecutar la función principal
if __name__ == "__main__":
    main()
#%% Números Capicúa
# Este programa permite identificar números capicúa dentro de un rango de hasta 4 cifras.

#%% Función para verificar si un número es capicúa
def es_capicua(numero):
    """
    Verifica si un número es capicúa.
    Un número es capicúa si se lee igual de izquierda a derecha y de derecha a izquierda.
    """
    str_num = str(numero)
    return str_num == str_num[::-1]

#%% Función para imprimir números capicúa según el rango y número de cifras
def imprimir_capicuas(inicio, fin, cifras):
    """
    Imprime números capicúa dentro del rango [inicio, fin] con el número especificado de cifras.
    """
    print(f"\nNúmeros capicúa de {cifras} cifras en el rango {inicio} a {fin}:")
    for numero in range(inicio, fin + 1):
        if len(str(numero)) == cifras and es_capicua(numero):
            print(numero, end=" ")
    print()

#%% Función principal con el menú
def main():
    while True:
        print("\n*** Menú de Números Capicúa ***")
        print("1. Ingresar un rango de números (máximo 4 cifras).")
        print("2. Imprimir números capicúa de dos cifras.")
        print("3. Imprimir números capicúa de tres cifras.")
        print("4. Salir.")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                inicio = int(input("Ingrese el número de inicio del rango: "))
                fin = int(input("Ingrese el número de fin del rango: "))
                if inicio < 0 or fin > 9999 or inicio > fin:
                    raise ValueError("El rango debe estar entre 0 y 9999 y ser válido.")
                print("Rango establecido correctamente.")
            elif opcion == 2:
                imprimir_capicuas(inicio, fin, 2)
            elif opcion == 3:
                imprimir_capicuas(inicio, fin, 3)
            elif opcion == 4:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción no válida, intente nuevamente.")
        except ValueError as e:
            print(f"Error: {e}")
        except NameError:
            print("Error: Ingrese primero el rango de números (opción 1).")

#%% Ejecutar la función principal
if __name__ == "__main__":
    main()
#%% [Ejercicio 4]

# Definiendo funciones para manejar las entradas y operaciones
def ingresar_nombre():
    while True:
        nombre = input("Ingrese su nombre: ").strip()
        if nombre.isalpha():
            return nombre
        else:
            print("El nombre debe contener solo letras. Por favor, intente nuevamente.")

def ingresar_apellido():
    while True:
        apellido = input("Ingrese su apellido: ").strip()
        if apellido.isalpha():
            return apellido
        else:
            print("El apellido debe contener solo letras. Por favor, intente nuevamente.")

def ingresar_dni():
    while True:
        try:
            dni = int(input("Ingrese su DNI: ").strip())
            if dni > 0:
                return dni
            else:
                print("El DNI debe ser un número positivo. Por favor, intente nuevamente.")
        except ValueError:
            print("El DNI debe ser un número. Por favor, intente nuevamente.")

def ingresar_celular(celular_num):
    while True:
        try:
            celular = int(input(f"Ingrese el número de celular {celular_num}: ").strip())
            if celular > 0:
                return celular
            else:
                print(f"El número de celular {celular_num} debe ser un número positivo. Por favor, intente nuevamente.")
        except ValueError:
            print(f"El número de celular {celular_num} debe ser un número. Por favor, intente nuevamente.")

def ingresar_altura():
    while True:
        try:
            altura = float(input("Ingrese su altura en metros: ").strip())
            if altura > 0:
                return altura
            else:
                print("La altura debe ser un número positivo. Por favor, intente nuevamente.")
        except ValueError:
            print("La altura debe ser un número. Por favor, intente nuevamente.")

def ingresar_peso():
    while True:
        try:
            peso = float(input("Ingrese su peso en kilogramos: ").strip())
            if peso > 0:
                return peso
            else:
                print("El peso debe ser un número positivo. Por favor, intente nuevamente.")
        except ValueError:
            print("El peso debe ser un número. Por favor, intente nuevamente.")

def imprimir_datos(nombre, apellido, dni, celular1, celular2, altura, peso):
    print("\nDatos del Postulante:")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"DNI: {dni}")
    print(f"Celular 1: {celular1}")
    print(f"Celular 2: {celular2}")
    print(f"Altura: {altura} m")
    print(f"Peso: {peso} kg")

def main():
    print("MENU - Datos del Postulante")
    datos_completos = False
    while not datos_completos:
        print("\nSeleccione una opción:")
        print("1. Ingresar Nombre")
        print("2. Ingresar Apellido")
        print("3. Ingresar DNI")
        print("4. Ingresar Celular 1")
        print("5. Ingresar Celular 2")
        print("6. Ingresar Altura")
        print("7. Ingresar Peso")
        print("8. Imprimir los datos ingresados del postulante")
        print("9. Salir")

        opcion = input("Ingrese la opción deseada: ").strip()

        if opcion == "1":
            nombre = ingresar_nombre()
        elif opcion == "2":
            apellido = ingresar_apellido()
        elif opcion == "3":
            dni = ingresar_dni()
        elif opcion == "4":
            celular1 = ingresar_celular(1)
        elif opcion == "5":
            celular2 = ingresar_celular(2)
        elif opcion == "6":
            altura = ingresar_altura()
        elif opcion == "7":
            peso = ingresar_peso()
        elif opcion == "8":
            imprimir_datos(nombre, apellido, dni, celular1, celular2, altura, peso)
        elif opcion == "9":
            datos_completos = True
        else:
            print("Opción no válida. Intente nuevamente.")

#%% [Ejercicio 5]

# Función para ingresar un dato textual sin números o símbolos extraños
def ingresar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto.isalpha():  # Verifica que solo contenga letras
            return texto
        else:
            print("El dato debe contener solo letras. Por favor, intente nuevamente.")

# Función para ingresar una nota y validar que sea un número entre 0 y 20
def ingresar_nota(mensaje):
    while True:
        try:
            nota = float(input(mensaje).strip())
            if 0 <= nota <= 20:  # Verifica que la nota esté en el rango correcto
                return nota
            else:
                print("La nota debe estar entre 0 y 20. Por favor, intente nuevamente.")
        except ValueError:
            print("La nota debe ser un número. Por favor, intente nuevamente.")

# Función para calcular el promedio
def calcular_promedio(nota1, nota2, nota3, nota4, nota_proyecto_final):
    promedio = (nota1 + nota2 + nota3 + nota4 + (nota_proyecto_final * 3)) / 7
    return promedio

# Función para imprimir el estado del alumno
def imprimir_estado(promedio):
    if promedio > 10.5:
        estado = "APROBADO"
    else:
        estado = "DESAPROBADO"
    
    if promedio > 17.5:
        estado += " QUINTO SUPERIOR"
    if promedio > 19.5:
        estado += " DECIMO SUPERIOR"
    
    print(f"Promedio: {promedio:.2f}")
    print(f"Estado: {estado}")

# Función principal para el flujo del programa
def main():
    print("MENU - Datos del Alumno")
    while True:
        print("\nSeleccione una opción:")
        print("1. Ingresar Nombre")
        print("2. Ingresar Apellido")
        print("3. Ingresar Nota 1")
        print("4. Ingresar Nota 2")
        print("5. Ingresar Nota 3")
        print("6. Ingresar Nota 4")
        print("7. Ingresar Nota Proyecto Final")
        print("8. Imprimir promedio del alumno")
        print("9. Salir")

        opcion = input("Ingrese la opción deseada: ").strip()

        # Variables globales para los datos del alumno
        nombre = ""
        apellido = ""
        nota1 = nota2 = nota3 = nota4 = nota_proyecto_final = 0

        if opcion == "1":
            nombre = ingresar_texto("Ingrese su nombre: ")
        elif opcion == "2":
            apellido = ingresar_texto("Ingrese su apellido: ")
        elif opcion == "3":
            nota1 = ingresar_nota("Ingrese la Nota 1: ")
        elif opcion == "4":
            nota2 = ingresar_nota("Ingrese la Nota 2: ")
        elif opcion == "5":
            nota3 = ingresar_nota("Ingrese la Nota 3: ")
        elif opcion == "6":
            nota4 = ingresar_nota("Ingrese la Nota 4: ")
        elif opcion == "7":
            nota_proyecto_final = ingresar_nota("Ingrese la Nota Proyecto Final: ")
        elif opcion == "8":
            promedio = calcular_promedio(nota1, nota2, nota3, nota4, nota_proyecto_final)
            imprimir_estado(promedio)
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Llamar la función main para ejecutar el programa
main()

#%% [Ejercicio 6]

# Función para ingresar un dato textual sin números o símbolos extraños
def ingresar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto.isalpha():  # Verifica que solo contenga letras
            return texto
        else:
            print("El dato debe contener solo letras. Por favor, intente nuevamente.")

# Función para ingresar una nota y validar que sea un número entre 0 y 20
def ingresar_nota(mensaje):
    while True:
        try:
            nota = float(input(mensaje).strip())
            if 0 <= nota <= 20:  # Verifica que la nota esté en el rango correcto
                return nota
            else:
                print("La nota debe estar entre 0 y 20. Por favor, intente nuevamente.")
        except ValueError:
            print("La nota debe ser un número. Por favor, intente nuevamente.")

# Función para calcular el promedio
def calcular_promedio(nota1, nota2, nota3, nota4, nota_proyecto_final):
    promedio = (nota1 + nota2 + nota3 + nota4 + (nota_proyecto_final * 3)) / 7
    return promedio

# Función para imprimir el estado del alumno
def imprimir_estado(promedio):
    if promedio > 10.5:
        estado = "APROBADO"
    else:
        estado = "DESAPROBADO"
    
    if promedio > 17.5:
        estado += " QUINTO SUPERIOR"
    if promedio > 19.5:
        estado += " DECIMO SUPERIOR"
    
    print(f"Promedio: {promedio:.2f}")
    print(f"Estado: {estado}")

# Función principal para el flujo del programa
def main():
    print("MENU - Datos del Alumno")
    while True:
        print("\nSeleccione una opción:")
        print("1. Ingresar Nombre")
        print("2. Ingresar Apellido")
        print("3. Ingresar Nota 1")
        print("4. Ingresar Nota 2")
        print("5. Ingresar Nota 3")
        print("6. Ingresar Nota 4")
        print("7. Ingresar Nota Proyecto Final")
        print("8. Imprimir promedio del alumno")
        print("9. Salir")

        opcion = input("Ingrese la opción deseada: ").strip()

        # Variables globales para los datos del alumno
        nombre = ""
        apellido = ""
        nota1 = nota2 = nota3 = nota4 = nota_proyecto_final = 0

        if opcion == "1":
            nombre = ingresar_texto("Ingrese su nombre: ")
        elif opcion == "2":
            apellido = ingresar_texto("Ingrese su apellido: ")
        elif opcion == "3":
            nota1 = ingresar_nota("Ingrese la Nota 1: ")
        elif opcion == "4":
            nota2 = ingresar_nota("Ingrese la Nota 2: ")
        elif opcion == "5":
            nota3 = ingresar_nota("Ingrese la Nota 3: ")
        elif opcion == "6":
            nota4 = ingresar_nota("Ingrese la Nota 4: ")
        elif opcion == "7":
            nota_proyecto_final = ingresar_nota("Ingrese la Nota Proyecto Final: ")
        elif opcion == "8":
            promedio = calcular_promedio(nota1, nota2, nota3, nota4, nota_proyecto_final)
            imprimir_estado(promedio)
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Llamar la función main para ejecutar el programa
main()

#%% [Ejercicio 7]

# Función para verificar si el nombre y apellido contienen solo letras
def es_valido_nombre_apellido(texto):
    return texto.isalpha()

# Función para ingresar y validar el nombre
def ingresar_nombre():
    while True:
        nombre = input("Ingrese su nombre: ").strip()
        if es_valido_nombre_apellido(nombre):
            return nombre
        else:
            print("El nombre debe contener solo letras, sin números ni símbolos extraños.")

# Función para ingresar y validar el apellido
def ingresar_apellido():
    while True:
        apellido = input("Ingrese su apellido: ").strip()
        if es_valido_nombre_apellido(apellido):
            return apellido
        else:
            print("El apellido debe contener solo letras, sin números ni símbolos extraños.")

# Función para ingresar y validar la edad
def ingresar_edad():
    while True:
        try:
            edad = int(input("Ingrese su edad: ").strip())
            if edad > 0:
                return edad
            else:
                print("La edad debe ser un número positivo.")
        except ValueError:
            print("Por favor ingrese una edad válida (número entero).")

# Función para ingresar y validar el peso
def ingresar_peso():
    while True:
        try:
            peso = float(input("Ingrese su peso en kilogramos: ").strip())
            if peso > 0:
                return peso
            else:
                print("El peso debe ser un número positivo.")
        except ValueError:
            print("Por favor ingrese un peso válido (número real).")

# Función para ingresar y validar el sexo
def ingresar_sexo():
    while True:
        sexo = input("Ingrese su sexo (M para Mujer, H para Hombre): ").strip().upper()
        if sexo in ["M", "H"]:
            return sexo
        else:
            print("Debe ingresar 'M' para Mujer o 'H' para Hombre.")

# Función para imprimir la dieta para mujeres
def imprimir_dieta_mujer(peso):
    if peso < 40:
        print("No hay dieta recomendada.")
    elif 40 <= peso < 50:
        print("Dieta rica en vegetales. Ejemplo: ensaladas, espinaca, brócoli, zanahorias.")
    elif 50 <= peso < 60:
        print("Dieta rica en vegetales y frutas. Ejemplo: ensaladas, manzanas, uvas, pepinos.")
    elif 60 <= peso < 80:
        print("Dieta rica en vegetales, frutas y semillas. Ejemplo: ensaladas con almendras, chia, zanahorias.")
    else:
        print("Debe someterse a cirugía debido a su peso.")

# Función para imprimir la dieta para varones
def imprimir_dieta_hombre(peso):
    if peso < 60:
        print("No hay dieta recomendada.")
    elif 60 <= peso < 75:
        print("Dieta rica en vegetales. Ejemplo: ensaladas, espinaca, pepinos, zanahorias.")
    elif 75 <= peso < 95:
        print("Dieta rica en vegetales y frutas. Ejemplo: ensaladas, manzanas, uvas, pepinos.")
    elif 95 <= peso < 120:
        print("Dieta rica en vegetales, frutas y semillas. Ejemplo: ensaladas con almendras, chia, zanahorias.")
    else:
        print("Debe someterse a cirugía debido a su peso.")

# Función para imprimir la dieta basada en el sexo y el peso
def imprimir_dieta(sexo, peso):
    if sexo == "M":
        imprimir_dieta_mujer(peso)
    elif sexo == "H":
        imprimir_dieta_hombre(peso)

# Función principal que maneja el menú y las opciones
def main():
    while True:
        print("\nMENU - Datos del Paciente")
        print("1. Ingresar Nombre")
        print("2. Ingresar Apellido")
        print("3. Ingresar Edad")
        print("4. Ingresar Peso")
        print("5. Ingresar Sexo")
        print("6. Imprimir Dieta")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = ingresar_nombre()
            print(f"Nombre ingresado: {nombre}")
        elif opcion == "2":
            apellido = ingresar_apellido()
            print(f"Apellido ingresado: {apellido}")
        elif opcion == "3":
            edad = ingresar_edad()
            print(f"Edad ingresada: {edad}")
        elif opcion == "4":
            peso = ingresar_peso()
            print(f"Peso ingresado: {peso} kg")
        elif opcion == "5":
            sexo = ingresar_sexo()
            print(f"Sexo ingresado: {sexo}")
        elif opcion == "6":
            if 'sexo' in locals() and 'peso' in locals():
                imprimir_dieta(sexo, peso)
            else:
                print("Debe ingresar el sexo y el peso para imprimir la dieta.")
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

# Llamar a la función principal para ejecutar el programa
main()

