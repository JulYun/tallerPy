import os

with open("020.txt", "w") as file:
   file.write("Hola mundo desde python :)")
   file.write("Adios")
   
if os.path.exists("dir_test_0"):
   print("El archivo 020.txt se creo exitosamente")
   with open("020.txt", "r") as file:
      for content in file:
         print(content)