name = "Juan"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))


print("Juan" + " Perez")
print(10 + 20)
print("Juan" + "12")


age = 12
print("Mi edad es " + str(age))
print(f"Mi edad es {age}")

#input siempre lo regresa un string
age = input("Escribe tu edad => ")
print(type(age))
age = int(age)
age += 10
print(f"Tu edad en 10 años será {age}")


# Ejercicio
name = 'Juana'
print(name)
age = '10'
print(age)
total = int(age) + 10

template = f"Hola mi nombre es {name}, tengo {age} años y en 10 años tendré {total} años"
print(template)