import os 
# 1. Generar un diccionario a partir de dos listas


print("Programa 1: diccionario hecho con 2 listas\n")

ciudades = ["Hermosillo","Ciudad Obreg贸n","Guaymas","San Luis R铆o Colorado","Navojoa"]
poblacion = [994000,333000,152000,131000,121000]
d = dict(zip(ciudades,poblacion))
print(d)

print("--------------------------\n")

# 2. Invierte una palabra sin utilizar el m茅todo reverse() e imprimirla
print("Programa 2: invertir palabra\n")

palabra = input("Ingresa una palabra : ")
print(f"La palabra invertida es : { palabra[::-1]}")

print("--------------------------\n")

# 3. Imprime 3 emojis (los puedes escoger desde la siguiente
print("Programa 3: Imprimir 3 emojis\n")
print("馃槑 馃榿 馃惙")
print("--------------------------\n")

# 4. Utiliza el m贸dulo string para remover de una forma f谩cil y sencilla signos de puntuaci贸n de la siguiente cadena: 
print("Programa 4: remover signos \n")

cadena = "He hecho cosas que ustedes las personas no podr铆an ni imaginar. Ataqu茅 naves con fuego en las colonias interplanetarias. He visto estrellas brillar en la noche con mil colores. Todos esos momentos se perder谩n en el tiempo, como l谩grimas bajo la lluvia."
signos = set(["\n",".",",",";",":","!","?"])
cadena_limpia = "".join([x if x not in signos else " " for x in cadena])
print(cadena_limpia)

print("--------------------------\n")

# 5. Utiliza la instrucci贸n set() para encontrar la intersecci贸n entre las siguientes listas:
print("Programa 5: Intersecci贸n\n")

a = set(["Star wars", "Alien","The black hole","Star trek 3","Gravity","Inception","Dune","Blade runner","Ready player one"])
b = set(["Parasite","Casablanca","The hurt locker","Star wars","Alien","Argo","Unforgiven","Gravity","The silence of the lambs","Dune","Coda","No country for old men","Shakespeare in love","Slumdog Millionare", "The Departed", "Million Dollar Baby", "Rain Man", "Inception"])
print (a.intersection(b))

print("--------------------------\n")
# 6. Utiliza el m贸dulo os 

print("Programa 6: m贸dulo os\n")

archivo = "D铆a1.py"
print(os.getcwd())
print(os.path.abspath(""))

directorio  = "/Users/duxa/Documents/Programacio虂n/Python/peque帽os_programas/little_programs/"
archivo = "/Users/duxa/Documents/Programacio虂n/Python/peque帽os_programas/little_programs/Main.py"
if os.path.isfile(archivo):
    print("es un archivo")
    
if os.path.isdir(directorio):
    print("es un directorio")
