# Iteración sobre tuplas
# Define la tupla (10, 20, 30, 40, 50) y recórrela con un for
# para imprimir cada elemento y su índice (usa enumerate).
tupla = (10, 20, 30, 40, 50)

for indice, elemento in enumerate(tupla):
  print(f"Elemento en el índice {indice}: es: {elemento}")