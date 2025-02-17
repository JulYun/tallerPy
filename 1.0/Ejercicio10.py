# Definir el diccionario
dic = {"nombre": "Casino Royale", "año": 2006, "clave": "007"}

# Imprimir el diccionario original y su tamaño
print("- El diccionario es:")
print(dic)
print("- Tiene " + str(len(dic)) + " elementos")

# Modificar el diccionario
dic["personaje"] = "James Bond"
dic["actor"] = "Daniel Craig"

# Eliminar la clave "clave" del diccionario
dic.pop("clave")

# Imprimir el diccionario modificado
print("- El diccionario modificado es:")
print(dic)
