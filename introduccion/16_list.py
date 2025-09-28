numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

task = ["make a dishes", "play videogames"]
print(task)
types = [1, True, "hola"]
print(types)
print(type(types))

print(numbers[0])
print(task[0])

#ajustes o cambios , mutación. Esto en los strings no se puede.
text = "Hola"
# text[0] = "W  esto nos da un error. Tratar de modificar un caracter en un string. Con un metodo replace podría ser posible.
task[0] = "watch platzi courses"
print(task)
task[0] = "do the dishes"
print(task)

print(numbers[:3])
print(True in types) # Si hay un valor dentro de una lista.
print("hola" in types) 
