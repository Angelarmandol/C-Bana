aOrd=[]
funcion=[]
derivada=[]
Dmas=[]
Dmenos=[]
exp=2.718281828
a = [4,6,3,6,7,2,5]

def metodo_ks(a):
	aOrd=a
	burbuja(aOrd)
	funcionM()
	fprima()
	calcularDmas(funcion, fprima)
	calcularalcularDmenos(funcion,fprima)
	DN=max(Dmas) #paso 6 calcular DN
	if max(Dmenos)>max(Dmas):
		DN=max(Dmenos)
	CDatos=(DN-0.2/50)*(sqrt(len(aOrd))+0.26+(0.5/sqrt(len(aOrd)))) #=(H5-0.2/50)*(RAIZ(50)+0.26+(0.5/RAIZ(50)))
	print ("el c de datos es: ",CDatos)

	
def	burbuja(aOrd): #ordena el arreglo de menor a mayor
	for i in range(0, len(aOrd)-1):
		for j in range(0,len(aOrd)-1-i):
			if aOrd[j] > aOrd[j+1]:
				aOrd[j],aOrd[j+1]=aOrd[j+1],aOrd[j]

def funcionM(): #paso 3 f(x)=i/n
	for x in range(0,len(aOrd)):
		i=x
	funcion[x]=i/len(aOrd)

def fprima(): #f'(x)=1-e(-xi/1.22)
	pass
	for x in xrange(0,len(aOrd)):
		derivada[x]=1-(exp*(aOrd/1.22))

def calcularDmas():#paso 5.1 D+=f(x)-f'(x)
	pass
	for x in xrange(0,len(aOrd)):
		Dmas[x]=funcion[x]-fprima[x]

def calcularDmenos(): #paso 5.2 D-=F'(xi)-f(xi-1)
	for x in xrange(0,len(aOrd)):
		Dmenos[x]=fprima[x]-funcion[x]
