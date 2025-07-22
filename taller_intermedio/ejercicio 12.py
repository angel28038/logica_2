# Validación de contraseña
# Implementa un programa que solicite una contraseña correcta (puedes fijarla en tu código)
# y permita hasta 3 intentos.

# Si el usuario acierta: imprime “¡Acceso concedido!” y termina.

# Si agota los 3 intentos: imprime “Usuario bloqueado” y termina.
intentos = 0
contraseña = "tigo123"
while intentos < 3:
    intento = input("oe parce, ingrese su contraseña")
    intentos += 1
    if intento == contraseña:
        print("parce la buena, acceso consedido")
        break
else: 
    print("quien sos vos? acceso denegado")