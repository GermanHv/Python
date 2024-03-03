print (not True)
print (not False)

# Consider this snippet from ./12_not.py
print ("Not and")
print ("not True and True =>", not (True and True))
print ("not True and False =>", not (True and False))
print ("not False and True =>", not (False and True))
print ("not False and False =>", not (False and False))

print ("Not or")
print ("not True or True =>", not (True or True))
print ("not True or False =>", not (True or False))
print ("not False or True =>", not (False or True))
print ("not False or False =>", not (False or False))

stock = input("Ingrese el número de stock => ")
stock = int(stock)
print(not (stock >= 100 and stock <= 1000))
