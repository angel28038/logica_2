# Contador de vocales
# Solicita al usuario una palabra y, con un for,
# cuenta cuántas vocales (a, e, i, o, u) contiene. Muestra el total al final.

contador = 0
vocales = "a,e,i,o,u,A,E,I,O,U"
palabra = input("ingrse una palabra: ")
for letra in palabra:
    if letra in vocales:
        contador += 1
    else:
        contador += 0
print (f"en la palabra {palabra} el total de vocales es: {contador}")
