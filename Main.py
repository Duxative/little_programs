import os 
# 1. Generar un diccionario a partir de dos listas (hay un modo pitónico de hacerlo) e imprimirlo: 
# Hermosillo, Ciudad Obregón, Guaymas, San Luis Río Colorado, Navojoa
# 994000, 333000, 152000, 131000, 121000


ciudades = ["Hermosillo","Ciudad Obregón","Guaymas","San Luis Río Colorado","Navojoa"]
poblacion = [994000,333000,152000,131000,121000]
d = dict(zip(ciudades,poblacion))
print(d)

# 2. Invierte una palabra sin utilizar el método reverse() e imprimirla

palabra = input("Ingresa una palabra : ")
print(f"La palabra invertida es : { palabra[::-1]}")

# 3. Imprime 3 emojis (los puedes escoger desde la siguiente

print("😎 😁 🐷")

# 4. Utiliza el módulo string para remover de una forma fácil y sencilla signos de puntuación de la siguiente cadena: 

cadena = "He hecho cosas que ustedes las personas no podrían ni imaginar. Ataqué naves con fuego en las colonias interplanetarias. He visto estrellas brillar en la noche con mil colores. Todos esos momentos se perderán en el tiempo, como lágrimas bajo la lluvia."
signos = set(["\n",".",",",";",":","!","?"])
cadena_limpia = "".join([x if x not in signos else " " for x in cadena])
print(cadena_limpia)

# 5. Utiliza la instrucción set() para encontrar la intersección entre las siguientes listas:

a = set(["Star wars", "Alien","The black hole","Star trek 3","Gravity","Inception","Dune","Blade runner","Ready player one"])
b = set(["Parasite","Casablanca","The hurt locker","Star wars","Alien","Argo","Unforgiven","Gravity","The silence of the lambs","Dune","Coda","No country for old men","Shakespeare in love","Slumdog Millionare", "The Departed", "Million Dollar Baby", "Rain Man", "Inception"])

print (a.intersection(b))

# 6. Utiliza el módulo os, para imprimir:
# el directorio de trabajo actual (current working directory)
# la ruta o sendero para encontrar un archivo
# checar si un archivo en el directorio actual es archivo o folder
archivo = "Día1.py"
print(os.getcwd())
print(os.path.abspath(""))

directorio  = "/Users/duxa/Documents/Programación/Python/pequeños_programas/little_programs/"
archivo = "/Users/duxa/Documents/Programación/Python/pequeños_programas/little_programs/Main.py"
if os.path.isfile(archivo):
    print("es un archivo")
    
if os.path.isdir(directorio):
    print("es un directorio")
