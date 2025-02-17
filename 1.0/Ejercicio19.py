import os

path = os.getcwd()
path_dir = os.path.join(path, "dir_test_0")

print("- Ruta actual: " + path)
print("El directorio actual contiene:")
print(os.listdir(path))
os.mkdir(path_dir)
os.chdir(path_dir)
print("- Ruta actual: " + os.getcwd())