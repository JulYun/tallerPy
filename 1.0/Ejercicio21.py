import os

def leer_poemas():
    # Definir el directorio base
    directorio = './poemas'
    
    # Lista de archivos de poemas que quieres leer
    archivos_poemas = ['poema1.txt', 'poema2.txt', 'poema3.txt']
    
    # Leer e imprimir cada archivo de poema
    for archivo_poema in archivos_poemas:
        # Crear la ruta completa al archivo
        ruta_poema = os.path.join(directorio, archivo_poema)
        
        try:
            # Abrir y leer el archivo
            with open(ruta_poema, 'r', encoding='utf-8') as poema:
                print(f"\nLeyendo {archivo_poema}:")
                print(poema.read())
        except FileNotFoundError:
            print(f"El archivo {archivo_poema} no se encontró en el directorio {directorio}.")

# Llamar a la función para leer los poemas
leer_poemas()
