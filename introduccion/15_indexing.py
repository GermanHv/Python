text = "Ella sabe Python"
print(len(text))
print(text[0])

size = len(text)
print(text[size - 1])
print(text[-1])


# Slicing , es lista[inicio:fin:step]  en el fin omite ese caracter.
print("slicing")
print(text[0:4])
print(text[10:16])
print(text[:9]) #toma del inicio hasta el 10
print(text[5:-1])
print(text[5:])
print(text[5:0]) #No funciona
print(text[5:0:-1])
print(text[5:16])
print(text[:]) #del inicio al final

print(text[10:16:1])
print(text[10:16:2])
print(text[::2])
print(text[::-1]) #Texto al revés

print(text[14:9:-1])
print(text[15:9:-1])
print(text[16:9:-1])
print(text[17:9:-1])
print(text[18:9:-1])


#Ejercicio palindromo
'''
print("Bienvenido a polindroPy")
while True:
  palabra = input("Introduce una palabra para verificar si es palindromo (o escribe 'salir' para terminar): ")
  if palabra.lower().replace(" ", "") == "salir":
    break
  palabra = palabra.replace(" ", "")
  palindromo = palabra[::-1] 
  print(palabra.capitalize() + " es palindromo" if palindromo == palabra else palabra.capitalize() + " no es un palindromo")
'''