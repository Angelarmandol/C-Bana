from array import *

print ('hola')
a = array('d',[4,6,3,6,7,2,5])
b = []	 #almacena corridas hacia arriba
c =[] #almacena corridas hacia abajo

corrida = 'corrida: '
numCorridas=0
rango = len(a)

for i in range(rango-1):
	if (a[i+1]>=a[i]): 
		print  a[i+1]
		print ('es mayor que')
		print a[i]
		
		if i < rango:
			print ('se inserta un uno')	
			b.insert(i, 1)
			#c.insert(i, 0)
			corrida=corrida+'1'
			print corrida
			print '-----------'

	else:
		print  a[i+1]
		print 'no es mayor que'
		print a[i]
		
		if i < rango:
			print ('se inserta un cero')	
			b.insert(i, 0)
			#c.insert(i, 1)
			corrida=corrida+'0'
			print corrida
			print'-------'
 
#print ("rango es: "+repr(rango))
for i in range(rango-2):
	#print (b[i])

	if((b[i])==(b[i+1])):
		#nada
		print'sin cambio'
	else:
		print'con cambio'
		numCorridas=numCorridas+1

print ("El numero de corridas de abajo hacia arriba es: "+repr(numCorridas))

#------------------------------------------------
contador = rango-2 #es dos por la longitud de el 
#array menos uno, y por el alogirtmo se le resta otro

for h in range(rango):

	print ("Se insertara en :"+repr(h)+"el valor de la posicion "+repr(contador))
	c.insert(h, b[contador])
	contador = contador-1

for i in range (rango):
	print (c[i])
	
print ('--------------------------------------')

for i in range(rango-1):
	if (a[i+1]<=a[i]): 
		print  a[i+1]
		print ('es menor que')
		print a[i]
		
		if i < rango:
			print ('se inserta un cero')	
			b.insert(i, 0)
			#c.insert(i, 0)
			corrida=corrida+'0'
			print corrida
			print '-----------'

	else:
		print  a[i+1]
		print 'es mayor que'
		print a[i]
		
		if i < rango:
			print ('se inserta un uno')	
			b.insert(i, 1)
			#c.insert(i, 1)
			corrida=corrida+'1'
			print corrida
			print'-------'

#print ("rango es: "+repr(rango))
for i in range(rango-2):
	#print (b[i])

	if((b[i])==(b[i+1])):
		#nada
		print'sin cambio'
	else:
		print'con cambio'
		numCorridas=numCorridas+1

print ("El numero de corridas de abajo hacia arriba es: "+repr(numCorridas))


#------------------------------------------------
contador = rango-2

for h in range(rango):

	print ("Se insertara en :"+repr(h)+"el valor de la posicion "+repr(contador))
	c.insert(h, b[contador])
	contador = contador-1


for i in range (rango):
	print (c[i])
