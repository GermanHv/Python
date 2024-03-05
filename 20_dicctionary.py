person = {
  'name': 'nico',
  'last_name': 'molina',
  'langs': ['python', 'javascript'],
  'age': 99
}

print(person)

person['name'] = 'santi'
person['age'] -= 50
person['langs'].append('rust')

print(person)

del person['last_name']
person.pop('age')
print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())

# Ejercicio

person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

# Escribe tu solución 👇
person['twitter'] = '@nicobytes'
person['name'] = 'Felipe'
person.pop('age')
print(list(person.keys()))
print(person.keys())


print(list(person.values()))
print(person.values())
