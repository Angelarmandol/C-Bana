try:
    from tkinter import *
    from ttk import *
except ImportError:  # Python 3
    from tkinter import *
    from tkinter.ttk import *
from array import *



variable = "xxxx"
arreglo = array('d', [0.23, 0.654, 0.8763, 0.89034, 0.236, 0.3451, 0.345, 0.1231, 0.3241, 0.7230])


''' Array
‘b’ -> Represents signed integer of size 1 byte
‘B’ -> Represents unsigned integer of size 1 byte
‘c’ -> Represents character of size 1 byte
‘u’ -> Represents unicode character of size 2 bytes
‘h’ -> Represents signed integer of size 2 bytes
‘H’ -> Represents unsigned integer of size 2 bytes
‘i’ -> Represents signed integer of size 2 bytes
‘I’ -> Represents unsigned integer of size 2 bytes
‘w’ -> Represents unicode character of size 4 bytes
‘l’ -> Represents signed integer of size 4 bytes
‘L’ -> Represents unsigned integer of size 4 bytes
‘f’ -> Represents floating point of size 4 bytes
‘d’ -> Represents floating point of size 8 bytes


'''


class App(Frame):








    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):

        tv = Treeview(self)
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
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)


        for i in range(10):
            self.treeview.insert('', '999', text=variable, values=('xXx',
                             arreglo[i], 'Ok'))

    def LoadTable(self):
         self.treeview.insert('', '999', text=variable, values=('xXx',
                              '0.0xxx', 'Ok'))
    

def main():
    root = Tk()
    App(root)
     
    root.mainloop()


if __name__ == '__main__':
    main()
