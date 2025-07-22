# Búsqueda con while-else
# Dada la lista [4, 8, 15, 16, 23, 42], pide al usuario un número a buscar.

# Recorre la lista con un while y, si lo encuentras, muestra su índice y haz break.

# Si terminas el bucle sin encontrarlo, el bloque else debe imprimir “Número no encontrado”.

lista = [4, 8, 15, 16, 23, 42]
indice = 1
numero = int(input("Introduce un número a buscar: "))
while indice < len(lista):
    if lista[indice] == numero:
        print(f"Número encontrado en el índice: {indice}")
        break
    indice += 1
else:
    print("Número no encontrado")