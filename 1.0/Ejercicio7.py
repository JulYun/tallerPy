# Definir la lista
la_lista = ["James", "Bond", 2006, "Casino Royale"]
# Imprimir la lista original y su tamaño
print("- La lista es")
print(la_lista)
print("- Tiene " + str(len(la_lista)) + " elementos")

# Modificar el segundo elemento de la lista
la_lista[1] = "James Bond"

# Agregar un nuevo elemento al final de la lista
la_lista.append("Daniel Craig")

# Eliminar el primer elemento de la lista
la_lista.pop(0)

# Imprimir la lista modificada
print("- La lista modificada es")
print(la_lista)