for element in range(1, 20):
  print(element)

my_list = [23, 45, 67, 89, 43]
for element in my_list:
  print(element)

my_tuple = ('nico', 'juli', 'santi')
for element in my_tuple:
  print(element)

product = {
  'name': 'camisa',
  'price': 100,
  'stock': 89
}

# solo las llaves
for element in product:
  print(element) 

# solo los valores
for element in product:
  print(element, '=>', product[element]) 

for key, value in product.items():
  print(key, '=>', value)

people = [
  {
    'name': 'nico',
    'age': 34
  },
  {
    'name': 'zule',
    'age': 45
  },
  {
    'name': 'santi',
    'age': 4
  }
]
# interaciones de diccionarios
for person in people:
  print(person)

for person in people:
  print('name =>', person['name'])

# Ejercicio

my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

# Escribe tu solución 👇
for i in my_list:
  if i > 0:
    new_list.append(i)

print(new_list)