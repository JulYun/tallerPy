# Definir la lista de texto
poema = [
    "gloria fuertes (1917 - 1998) España",
    "en las noches claras",
    "resuelvo el problema de la soledad del ser",
    "Invito a la luna y con mi sombra somos tres"
]

# Imprimir la información del poema
print(poema[0].capitalize())

# Imprimir las líneas del poema en mayúsculas o en formato que desees
for linea in poema[1:]:
    print(linea.capitalize())

# Calcular y mostrar el número de palabras
num_palabras = sum(len(linea.split()) for linea in poema)
print(f"\nPequeño poema de {num_palabras} palabras")
