 
import random
'''
Criterios:
Es numerico: numerico
Son mas o igual a 50: mayorcincuenta
Algun numnero valido ( por defecto, si): numervalido

pasa o no pasa: pasa
'''

numerico=0
mayorcincuenta=0
numerovalido=1

pasa=0
#a = "0.25051451 0.8521 0.5454 0.54545 0.545454 0.65665 0.14564654 0.156654156 0.5458454 0.5445445 0.787878 0.986535"
a = " "
alea=0
for i in range(50):
	alea = random.random()
	a = a+" "+repr(alea)

vector = []


if(a.isdigit()):
	print ("no es numerica")
	numerico=0
else:
	print("numerica")
	numerico=1
	print (" ")
	a = a.split(" ")
	a.pop(0)
	a.pop(0)
	b = len(a)
	for i in range (b):
		print (a[i])

rango = len(a)

if(rango>=50):
	print ("Son mas de cincuenta, si pasa")
	mayorcincuenta=1
else:
	print("Son menos de cincuanta, no pasa")
	mayorcincuenta=0
try:
	for i in range (rango):
		float(a[i])
except ValueError:
    print "Oops!  "+repr(a[i])+"no es un numero valido"
    numerovalido=0

if(numerico == 1 and mayorcincuenta == 1 and numerovalido==1):
	print("No hay nada malo")
else:
	print("si hay algo malo")
	numerico=0
	mayorcincuenta=0
	numerovalido=1
	pasa=0

 
