my_diccionary = {}
print(type(my_diccionary))
my_diccionary = {
  "name": "Juan",
  "last_name": "Perez",
  "age": 25
}
print(my_diccionary)

print(len(my_diccionary))
print(my_diccionary["age"])
print(my_diccionary.get("age"))

# print(my_diccionary["valor"]) Me da un error
print(my_diccionary.get("valor")) # Me devuelve un None

print("name" in my_diccionary)
print("avion" in my_diccionary)