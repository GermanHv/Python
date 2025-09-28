#CRUD Create, Read, Update & Delete
numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1] = 10
print(numbers)

# Agregar un elemento al final de la lista
numbers.append(700)
print(numbers)

# Agregar un elemento en una posición específica
numbers.insert(0, "hola")
print(numbers)
numbers.insert(3, "change")
print(numbers)
     
# Fusionar listas
tasks = ["todo 1", "todo 2", "todo 3"]
new_list = numbers + tasks
print(new_list)

# Encontrar la posición de un elemento en una lista
index = new_list.index("todo 2")
new_list[index] = "todo changed"
print(new_list)

# Eliminar un elemento de una lista
new_list.remove("todo 1")
print(new_list)

# Eliminar el último elemento de la lista
new_list.pop()
print(new_list)

# Eliminar un elemento de una posición específica
new_list.pop(0)
print(new_list)

# Invertir el orden de la lista
new_list.reverse()
print(new_list)

# Ordenar una lista
numbers_a = [1, 4, 6, 3]
numbers_a.sort()
print(numbers_a)

strings = ["re", "ab", "ed"]
strings.sort()
print(strings)

# Ejercicio
letters = ['A', 'B', 'C', 'D', 'E', 'F']

letters.append("G")
letters[0] = "Z"
letters.remove("C")
letters.reverse()

print(letters)