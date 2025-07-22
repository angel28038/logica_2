# Menú repetitivo
# Desarrolla un menú en bucle while con estas opciones:

# Sumar dos números

# Restar dos números

# Multiplicar dos números

# Salir
# Elige la opción, pide los operandos, muestra el resultado y vuelve a mostrar
# el menú hasta que seleccione “Salir”.
while True:
    print("\n--- Calculadora Simple ---")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    if opcion == '4':
        print("Saliendo de la calculadora.")
        break
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")
        continue
    if opcion == '1':
        resultado = num1 + num2
        print(f"Resultado: {resultado}")
    elif opcion == '2':
        resultado = num1 - num2
        print(f"Resultado: {resultado}")
    elif opcion == '3':
        resultado = num1 * num2
        print(f"Resultado: {resultado}")
    else:
       print("Opción inválida. Intenta de nuevo.")