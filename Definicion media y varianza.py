""""para corridas por arriba y por debajo """
a = array('d',[4,6,3,6,7,2,5])
def sacarMediayVar(a):  """saca la media y la varianza"""
tamA=len(a) """numero de datos en el arreglo"""
mayor= max(a); """numero mayor en el arreglo"""
menor=min(a); """numero menor en el arreglo"""
media = [(2*tamA)-1]/3 
varianza= [(16*tamA)-29]/90
print "la media es: "+media
print "la varianza es: "+varianza

""""para corridas por arriba y por debajo de la media"""
def valorEstadistico(a,numCorridas):
	valorE=[(2*mayor*menor)/tamA]+(1/2) #valor esperado
varianza=[2*mayor * menor *(2*mayor * menor –tamA)]/ tamA *(tamA-1)
estadistico=(numCorridas-valorE)/varianza

