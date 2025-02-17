# Definir las variables
x = 3
y = "3"
cad = "La suma es: x + y = "

# Imprimir el valor inicial de x
print("La variable x es el número:")
print(x)

# Imprimir el valor inicial de y
print("La variable y es la cadena:")
print(y)

# Realizar la suma de x y y (convirtiendo y a entero)
x = x + int(y)

# Actualizar la cadena con el resultado de la suma
cad = cad + str(x)

# Imprimir la cadena con el resultado
print(cad)
