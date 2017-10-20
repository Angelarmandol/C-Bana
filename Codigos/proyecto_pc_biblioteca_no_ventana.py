print ("nada1")                                           
try:
    from tkinter import *
    from tkinter.ttk import *
   
     

    

except ImportError:
        print ("nada2")  
    

variable = "xxxx"
from array import *
arreglo = array('d', [0.23, 0.654, 0.8763, 0.89034, 0.236, 0.3451, 0.345, 0.1231, 0.3241, 0.7230])

     
  
class App(Frame):
         







                def __init__(self, parent):     
                    Frame.__init__(self, parent)
                    self.CreateUI()     
                    self.LoadTable()     
                    self.grid(sticky =(N,S,W,E))     
                    parent.grid_rowconfigure(0, weight = 1)
                    parent.grid_columnconfigure(0, weight = 1)     
                    print("entro")

                def CreateUI(self):

                    tv = Treeview(self) 
                    tv['columns'] = ('starttime', 'endtime','status') 
                    tv.heading("#0", text='*////*', anchor='w')
                    tv.column("#0", anchor="w") 
                    tv.heading('starttime',
                    text='bbbb') 
                    tv.column('starttime', anchor='center',
                    width=100) 
                    tv.heading('endtime', text='Numeros Pseudoaleatorios') 
                    tv.column('endtime', anchor='center',
                    width=100) 
                    tv.heading('status', text='No se')
                    tv.column('status', anchor='center', width=100) 
                    tv.grid(sticky = (N,S,W,E)) 
                    self.treeview = tv 
                    self.grid_rowconfigure(0,weight = 1) 
                    self.grid_columnconfigure(0, weight = 1)


                    #for i in range(10):     
                    # self.treeview.insert('', '999', text=variable, values=('xXx',arreglo[i], 'Ok'))

                def LoadTable(self):  

                    for i in range(10):
                        self.treeview.insert('', '999', text=variable, values=('xXx', arreglo[i], 'Ok'))
                
            

def main():
    root = Tk()
    App(root)
                     
    root.mainloop()


    if __name__ == '__main__':
      main()


