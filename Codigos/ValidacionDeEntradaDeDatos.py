
##La cadena de texto se guarda en a, el vector se regresa como a.

'''

Validacion de los datos:
__________________
Ya hechas:
1) Todos numericos (con puntuacion)
2) Sin puntos dobles

__________________
Por hacer




'''

a = "0.25051451 0.8521 0.5454 0.54545 0.545454 0.65665 0.14564654 0.156654156 0.5458454 0.5445445 0.787878 0.986535"


vector = []


if(a.isdigit()):
	print ("no es numerica")

else:
	print("numerica")
	print (" ")
	a = a.split(" ")
	b = len(a)
	for i in range (b):
		print (a[i])

rango = len(a)

try:
	for i in range (rango):
		float(a[i])
except ValueError:
    print "Oops!  "+repr(a[i])+"no es un numero valido"
