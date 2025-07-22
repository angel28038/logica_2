# Promedio de lista
# Dada la lista [12, 7, 22, 5, 14, 9], utiliza un for,
# un acumulador y un contador para calcular y mostrar su promedio.
contador = 0
acumulador = 0
lista = [12,7,22,5,14,9]
for numero in lista:
    acumulador += numero
    contador += 1
    promedio = acumulador/6
print(f"la cantidad de numeros es: {contador},  la suma total es: {acumulador},  y el promedio es: {promedio}")
