try:
    from tkinter import *
    from tkinter.ttk import *

    
except ImportError:  # Python 3
    from tkinter import *
   
from array import *
import ctypes 
import tkinter as tk
import random

from random import *




'''
Criterios:
Es numerico: numerico
Son mas o igual a 50: mayorcincuenta
Algun numnero valido ( por defecto, si): numervalido
pasa o no pasa: pasa
'''


arreglo = array('d', [0.23, 0.654, 0.8763, 0.89034, 0.236, 0.3451, 0.345, 0.1231, 0.3241, 0.7230])
ventana = tk.Tk()
ventana.geometry("800x600")
ventana.title("C-Bana")
vector = []
a = []
rango2=0
aOrd=[]
aOrdGlobal=[]
respa  = []
efedeexisi = []
def resolucionPrincipal(resol):
    ventana.geometry("1000x600")
    #ventana.mainloop()

def hola():
    print ("Hola!")

def burbuja(aOrd): #ordena el arreglo de menor a mayor
    
    respa = a
    

    for i in range(1, len(aOrd)):
        for j in range(0,len(aOrd)-i):
            if aOrd[j] > aOrd[j+1]:
                k = aOrd[j+1]
                aOrd[j+1]=aOrd[j]
                aOrd[j]=k
    longaOrd = len(aOrd)
    print ("al final de l metodo, valor inicial de aOrg es: "+repr(aOrd[0]))
    print ("al final de l metodo, valor final de aOrg es: "+repr(aOrd[117]))
    global aOrdGlobal
    aOrdGlobal = aOrd

def comprobar():
    global a
     




    a=texto.get("1.0","end-1c")
    numerico=0
    mayorcincuenta=0
    numerovalido=1
    
    pasa=0
    a=a.replace(",",".")
    #a = "0.25051451 0.8521 0.5454 0.54545 0.545454 0.65665 0.14564654 0.156654156 0.5458454 0.5445445 0.787878 0.986535"
    '''
    a = " "
    alea=0
    for i in range(50):
        alea = random.random()
        a = a+" "+repr(alea)
'''
    

    #print (a)
    if(a.isdigit()):
        print ("no es numerica")
        numerico=0
    else:
        print("numerica")
        numerico=1
        print (" ")
        #print (a)
        

        a = a.split(" ")
        #print(a)
        #a.pop(0)
        #a.pop(0)
        b = len(a)
        contador=0
        
    '''
        for i in range (b):
            print (a[i])
            print("/////"+repr(b))
    '''
    a=a[0].split("\n")

    print(a[0])
    print(a[1])
    print ("longiyud es "+repr(len(a)))
    rango = len(a)
    






    global rango2
    rango2=rango
    print("se a guardado como rango2 "+repr(rango2))
  







    if(rango>=50):
        print ("Son mas de cincuenta, si pasa")
        mayorcincuenta=1
    else:
        print("Son menos de cincuanta, no pasa")

        mayorcincuenta=0
        ctypes.windll.user32.MessageBoxW(0, "No hay numeros suficientes para generar la tabla", "Error", 1)
    '''
    try:
        for i in range (rango):
            float(a[i])
    except ValueError:
        print ("Oops!  "+repr(a[i])+"no es un numero valido")
        #numerovalido=0
    '''

    if(numerico == 1 and mayorcincuenta == 1 and numerovalido==1):
        print("No hay nada malo")
       
    else:
        print("si hay algo malo")
        numerico=0
        mayorcincuenta=0
        numerovalido=1
        pasa=0

    print("Termina comprobar, a es:")
    print (a[0])
    print (a[1])

    
def otraventana():

    comprobar()
    print("el valor de la variable rango 2 es: "+repr(rango2))
    ventana2 = tk.Tk()
    tv = Treeview(ventana2, selectmode="extended",columns=("A","B"))
    ventana2.geometry("900x500")
    tv.pack(expand=YES, fill=BOTH)
    #tv.grid_rowconfigure(0, weight = 1)
    #tv.grid_columnconfigure(0, weight = 1)


    #ventana2.geometry("600x200")
    #ventana2.resizable(True, True) #para no permitir 
    ventana2.title("Tabla de datos")
    tv['columns'] = ('starttime', 'endtime', 'status', 'wea1')

    tv.heading('#0', text='i')
    tv.column('#0', anchor='center', width=100)

    tv.heading('starttime', text='Numeros Pseudoaleatorios')
    tv.column('starttime', anchor='center', width=200)

    tv.heading('endtime', text='Numeros ordenados')
    tv.column('endtime', anchor='center', width=200)

    tv.heading('status', text='f(x)=i/n')
    tv.column('status', anchor='center', width=200)

    tv.heading('wea1', text='wea2')
    tv.column('wea1', anchor='center', width=200)

    respa = a[:] #no me jodas python!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! es una copia de la lista, otro objeto
    aOrd=a
    #print("primer valor de  a es: "+repr(a[0]))
    burbuja(aOrd)
    #print("despues de burbuja, valor de a es: "+repr(a[0]))
    #print("despues de burbuja, valor de respa es: "+repr(respa[0]))
    #print("longitud de a es "+repr(rango2))
    #insert normal
    #tv.insert('', '999', text=variable, values=('xXx','99', 'Ok'))
    efedeexisi = aOrd[:]

    rango = len(efedeexisi)
    for i in range(rango):
        efedeexisi[i]=float(efedeexisi[i])/rango
    

    #print ("longiud de aOrd es: "+ repr(len(aOrd)))
    for g in range(rango2):
        tv.insert('', 'end', text= g, values=(respa[g], a[g], efedeexisi[g], 'wea3'))
    tv.pack()
    ventana2.mainloop()
        
    
##  Styles:
##  0 : OK
##  1 : OK | Cancel
##  2 : Abort | Retry | Ignore
##  3 : Yes | No | Cancel
##  4 : Yes | No
##  5 : Retry | No 
##  6 : Cancel | Try Again | Continue

     
    



####################### menu

#menu principal
menubarra = Menu(ventana)


fileMenu = tk.Menu(ventana)
 
#archivo

menuarchivo = Menu(menubarra, tearoff=0)
menuarchivo.add_command(label="x Abrir", command=hola)
menuarchivo.add_command(label="x Guardar", command=hola)
menuarchivo.add_separator()
menuarchivo.add_command(label="Salir", command=ventana.quit)
menubarra.add_cascade(label="Archivo", menu=menuarchivo)

#tabla
tabla = Menu(menubarra, tearoff=0, postcommand=hola)
tabla.add_command(label="Abrir", command=otraventana)
menubarra.add_cascade(label="Tabla", menu=tabla)

#prueba
prueba = Menu(menubarra, tearoff=0, postcommand=hola)
prueba.add_command(label="x prueba", command=otraventana)
menubarra.add_cascade(label="x prueba", menu=prueba)



#submenu
menubarra.add_cascade(label="x Configuracion", menu=fileMenu)
fileMenu.add_command(label="x Otro", command=hola)



#Muestra el menu
ventana.config(menu=menubarra)


 
##################################### menu

#texto = label("hola")
 
texto = Text(ventana, height=50, width=40)
texto.pack()
texto.config(width=200)
 
boton = tk.Button(ventana, text="Comprobar", command=comprobar) 
boton.pack()

#Muestra la ventana
ventana.mainloop()
