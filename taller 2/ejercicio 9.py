# Pares e impares
# Dada la lista [3, 8, 15, 22, 7, 10, 13], recórrela con un for y utiliza
# dos contadores para determinar cuántos son
# pares y cuántos impares. Muestra ambos totales.
contador_pares = 1
contador_impares = 1
lista = [ 3, 8, 15, 22, 7, 10, 13 ]
for i in lista:
    if i % 2 == 0:
        contador_pares += 1
    if i % 3 == 0:
        contador_impares += 1
print (f" la cantidad de numeros pares es: {contador_pares}, la cantidad de numeros impares es: {contador_impares},")