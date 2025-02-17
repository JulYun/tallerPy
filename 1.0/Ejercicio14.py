# Lista de diccionarios con las películas
peliculas = [{"nombre": "Casino Royale", "año": 2006}, {"nombre": "Quantum of Solace", "año": 2008}]

# Iterar sobre cada película
for pelicula in peliculas:
    print("- Pelicula")
    for propiedad in pelicula:
        # Verificar si la propiedad es "año" y convertirla a string
        if propiedad == "año":
            print(propiedad + ": " + str(pelicula[propiedad]))
        else:
            print(propiedad + ": " + pelicula[propiedad])
