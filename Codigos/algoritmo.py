from array import *


 
print ('hola')
a = array('d',[4,6,3,6,7,2,5])

rango = len(a)

for i in range(rango-1):
	if (a[i+1]>=a[i]): 
		print  a[i+1]
		print ('es mayor que')
		print a[i]
		print '-----------'
	else:
		print  a[i+1]
		print 'no es mayor que'
		print a[i]
		print'-------'
