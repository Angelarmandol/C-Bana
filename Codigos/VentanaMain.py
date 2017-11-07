try:
 import tkinter
 from tkinter import *
 from tkinter.ttk import *
 from array import *

except ImportError:
 raise ImportError("Se requiere el modulo Tkinter")

import tkinter as tk
import ctypes 

variable = "xxxx"
arreglo = array('d', [0.23, 0.654, 0.8763, 0.89034, 0.236, 0.3451, 0.345, 0.1231, 0.3241, 0.7230])
ventana = tk.Tk()
ventana.geometry("800x600")
ventana.title("C-Bana")
vector = []
a = []

def resolucionPrincipal(resol):
	ventana.geometry("1000x600")
	#ventana.mainloop()

def hola():
    print ("Hola!")



def comprobar():
	 
	##antes de comprobar, verificar que este no este vacia

	global a
	a = texto.get("1.0",END)
	a = a.replace(" ", "\n")
	a = a.split("\n")

	b = len(a)
	for i in range (b):
		print (a[i])


	print ("comprobando")
	b = len(a)
	for i in range (b-1):
		if(a[i].isdigit()):
			print ("no es numerica!!!!")

		else:
			print("numerica")
		 

	rango = len(a)

	try:
		for i in range (rango-1):
			float(a[i])
	except ValueError:
	    print ("Oops!  "+repr(a[i])+"no es un numero valido")
	return a

def otraventana():
	b = len(a)
	comprobar()
	if (b!=0):
		ventana2 = tk.Tk()
		tv = Treeview(ventana2)
		
		ventana2.geometry("600x200")
		ventana2.resizable(False, False) #para no permitir 
		ventana2.title("Tabla de datos")
		tv['columns'] = ('starttime', 'endtime', 'status')
		tv.heading("#0", text='*////*', anchor='w')
		tv.column("#0", anchor="w")
		tv.heading('starttime', text='bbbb')
		tv.column('starttime', anchor='center', width=100)
		tv.heading('endtime', text='Numeros Pseudoaleatorios')
		tv.column('endtime', anchor='center', width=100)
		tv.heading('status', text='No se')
		tv.column('status', anchor='center', width=100)
		tv.grid(sticky = (N,S,W,E))
		
		
		print("longitud de a es "+repr(b))
		#insert normal
		#tv.insert('', '999', text=variable, values=('xXx','99', 'Ok'))
		for i in range(b):
	            tv.insert('', '999', text=variable, values=('xXx',a[i], 'Ok'))
		#self.treeview = tv
		#self.grid_rowconfigure(0, weight = 1)
		#self.grid_columnconfigure(0, weight = 1)
		ventana2.mainloop()
	else:
	 print("no hay datos")
	 b = 0
	 ctypes.windll.user32.MessageBoxW(0, "No hay numeros para generar la tabla", "Error", 1)
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
 
texto = Text(ventana, height=20, width=40)
texto.pack()
texto.config(width=200)
 
boton = tk.Button(ventana, text="Comprobar", command=comprobar)	
boton.pack()

#Muestra la ventana
ventana.mainloop()

