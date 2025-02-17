# Inicializar la variable a
a = 2

# Bucle while para comparar y modificar a
while a < 6:
    print("a = " + str(a) + " es menor que 6")
    
    # Si a es igual a 3, se sale del bucle
    if a == 3:
        break
    
    # Incrementar el valor de a
    a += 1

# Imprimir el valor final de a
print("- El valor final de a es " + str(a))
