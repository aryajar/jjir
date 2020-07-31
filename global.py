a = 9
def change():
	global a
	print(a)
	a = 100
print("Befor the function call ", a)
print("inside change function", end=' ')
change()
print("After the function call", a)