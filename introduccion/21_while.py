"""
Ciclo infinito
while True:
  print('se ejecuto')
"""

counter = 0
while counter < 10:
  counter += 1
  print(counter)

# Ejercicio
counter = 0
while counter < 20:

  counter += 1
  if counter == 15:
    break
  print(counter)

# Ejercicio
counter = 0
while counter < 20:
  counter += 1
  if counter < 15:
    continue
  print(counter)