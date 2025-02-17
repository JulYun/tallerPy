# Definir las operaciones aritméticas
def division(a, b):
    return a / b

def suma(a, b):
    return a + b

def multiplicacion(a, b):
    return a * b

# Definir los valores de a y b
a = 1
b = 2

# Imprimir las operaciones aritméticas con el formato solicitado
print("Operaciones Aritméticas\n")
print("Sean dos números 'a' y 'b', tal que")
print(f"a = {a}")
print(f"b = {b}\n")

print("Entonces\n")
print(f"a / b = {division(a, b)}")
print(f"a + b = {suma(a, b)}")
print(f"a * b = {multiplicacion(a, b)}")
