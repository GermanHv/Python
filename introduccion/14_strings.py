text = "Ella sabe Python"
print ("Java" in text)
print ("Python" in text)
'''
if "Python" in text:
 print ("buena opción")
elif "Java" in text:
 print ("buena opción, también")
else:
 print ("no hay ninguna opción")

'''
#Metodos
size = len(text)
print(size)
print(text)
print(text.upper())
print(text.lower())
print(text.count("a"))
print(text.swapcase())
print(text.startswith("El"))
print(text.endswith("thon"))
print(text.replace("Python", "Go"))
print(text)
text2 = "este es un título"
print(text2)
print(text2.capitalize())
print(text2.title())
print(text2.isdigit())
print("398".isdigit())
print("Hola".isdigit())

