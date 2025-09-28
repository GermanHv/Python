import random

options = ("piedra", "papel", "tijera")

user_option = input("piedra, papel o tijera => ")
user_option = user_option.lower().strip()
computer_option = random.choice(options)

if not user_option in options:
  print("Esa opción no es válida")

print ("user opción => ", user_option)
print ("computer opción => ", computer_option)

if user_option == computer_option:
  print("Empate!")
elif user_option == "piedra":
  if computer_option == "tijera":
    print("piedra gana a tijera")
    print("user ganó")
  else:
    print("papel gana a piedra")
    print("computer ganó")
    
elif user_option == "papel":
  if computer_option == "piedra":
    print("papel gana a piedra")
    print("user ganó")
  else:
    print("tijera gana a papel")
    print("computer ganó")
elif user_option == "tijera":
  if computer_option == "papel":
    print("tijera gana a papel")
    print("user ganó")
  else:
    print("piedra gana a tijera")
    print("computer ganó")


'''
number = int(input("Ingresa un número: "))
print(number)
# Escribe tu solución 👇

number = int(number)
operación = number % 2
if operación == 0:
  print ("Es par")
else:
  print("Es impar")
'''