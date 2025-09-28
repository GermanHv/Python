numbers = (1, 2, 3, 5)
strings = ("nico", "zule", "santi", "nico")
print(numbers)
print(type(numbers))
print(strings)
print(type(strings))

# Acceder a un valor de la tupla
print("0 =>", numbers[0])
print("-1 =>", numbers[-1])

# Encontrar la posición de un elemento en una tupla
print(strings)
print(strings.index("zule"))

# Contar cuantas veces está un elemento en una tupla
print(strings.count("nico"))

# Convertir una tupla en una lista
my_list = list(strings)
print(my_list)
print(type(my_list))
my_list[1] = "juli"
print(my_list)
my_list.pop(0)

# Convertir una lista en una tupla
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple)) 
