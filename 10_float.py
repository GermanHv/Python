# Ejercicio
x = 3.3
y = 1.1 + 2.2
print(x)
print(y)
print(x == y)

y_str = format(y, ".2g")
print(y_str)
print(y_str == str(x))


print(x, y)
tolerance = 0.00001
print(abs(x - y) < tolerance)

y = round (y, 1)
print(y)
print(x == y)