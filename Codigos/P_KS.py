from random import uniform
from math import fabs
from Gnuplot import Gnuplot
from Gnuplot import PlotItems
 
class KS:
 
    def __init__(self, lista):
        self.lista = lista
        return
   
    def obtenerDistancias(self, lista):
        lista.sort()
        tamanio = len(lista)
        distancias = []
        for i in range(tamanio):
            distancias.append(fabs(((i+1)/float(tamanio))-lista[i]))
        return distancias
 
    def estadisticoCalculado(self):
        distancias = self.obtenerDistancias(list(self.lista)) # paso una copia de la lista, no la referenci a ala origina, para mantenerla intacta y no ordenada
        return max(distancias)
 
    def graficar(self, tipo='dots', serie='Valores'):
        gp = Gnuplot(persist=1)
        gp('set title "Kolmogorov-Smirnov(Aleatoriedad)"')
        plot1 = PlotItems.Data(self.lista, with_=tipo, title=serie)
        gp.plot(plot1)
        return
