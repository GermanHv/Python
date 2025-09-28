name = "Juan"
last_name = "Perez"
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

# quote = 'I'm Juan'   Esto es un error de syntaxis
quote = "I'm Juan"
print(quote)

# quote2 = "She said "Hello""   Esto es un error de syntaxis
quote2 = 'She said "Hello"'
print(quote2)

#format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print("v1", template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print("v2", template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print("v3", template)


#Ejercicio

name = input("¿Cuál es tu nombre? ")
last_name = input(f"¿Cuál es tu apellido, {name}? ")
age = input(f"¿Cuál es tu edad, {name}?")

template = f"Hola, mi nombre es {name} {last_name} y mi edad es {age} años"
print(template)