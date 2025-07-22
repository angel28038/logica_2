# Suma hasta cero
# Crea un programa que lea números del usuario repetidamente con while hasta que ingrese 
# un 0. Al finalizar, muestra la suma de todos los valores ingresados (excluyendo el cero).
acumulador = 0

numero = int(input("ingrese un numero: "))
acumulador = acumulador + numero
while numero > 0: 
    numero = int(input("ingrese un numero: "))
    acumulador = acumulador + numero
    if numero == 0:
        print(f"la acumulacion de todos los numeros es: {acumulador}")