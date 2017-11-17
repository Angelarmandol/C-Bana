+a = array('d',[4,6,3,6,7,2,5])
 +aOrd=[]
 +funcion=[]
 +derivada=[]
 +Dmas=[]
 +Dmenos=[]
 +exp=2.718281828
 +
 +
 +
 +def metodoks(a):
 +	aOrd=a
 +	#burbuja(aOrd)
 for i in range(0, len(aOrd)-1):
 +		for j in range(0,len(aOrd)-1-i):
 +			if aOrd[j] > aOrd[j+1]:
 +				aOrd[j],aOrd[j+1]=aOrd[j+1],aOrd[j]
 +	#funcionM()
 	for x in xrange(0,len(aOrd)):
 +		pass
 +		funcion[x]=(x+1)/len(aOrd)
 +	#fprima()
 for x in xrange(0,len(aOrd)):
 +		derivada[x]=1-(exp*(aOrd/1.22))
 +	#calcularDmas(funcion, fprima)
for x in xrange(len(aOrd)):
 +		Dmas[x]=funcion[x]-fprima[x]
 +	#calcularDmenos(funcion,fprima)
 for x in xrange(len(aOrd)):
 +		pass
 +		Dmenos= fprima[x]- funcion[x]
 +	DN=max(Dmas) #paso 6 calcular DN
 +	if max(Dmenos)>DN:
 +		print("no entra")
 +		DN= max(Dmenos)
 +		CDatos=(DN-0.2/len(aOrd))*(sqrt(len(aOrd))+0.26+(0.5/sqrt(len(aOrd)))) #=(H5-0.2/50)*(RAIZ(50)+0.26+(0.5/RAIZ(50)))
 +		print "el c de datos es: "+repr(CDatos)
 +	else: 
 +		print ("no entra")
 +
 +	""""
 +#def	burbuja(aOrd): #ordena el arreglo de menor a mayor
 +	for i in range(0, len(aOrd)-1):
 +		for j in range(0,len(aOrd)-1-i):
 +			if aOrd[j] > aOrd[j+1]:
 +				aOrd[j],aOrd[j+1]=aOrd[j+1],aOrd[j]
 +#return aOrd
 +
 #def funcionM(): 
 +#paso 3 f(x)=i/n
 +
 +		pass
 +#return funcion
 +
 +def fprima():#f'(x)=1-e(-xi/1.22)
 +	pass
 +	
 +		pass
 +#return derivada
 +
 +def calcularDmas(funcion,fprima):#paso 5.1 D+=f(x)-f'(x)
 +	
 +#return derivada
 +
 +
 +def calcularDmenos(funcion, fprima): #paso 5.2 D-=F'(xi)-f(xi-1)
 +	
 +		pass
 +#return Dmenos""""