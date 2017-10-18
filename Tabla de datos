try:
    from tkinter import *
    from ttk import *
except ImportError:  # Python 3
    from tkinter import *
    from tkinter.ttk import *

variable = "xxxx"
 

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
        tv.heading("#0", text='Numeros Pseudoaleatorios', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('starttime', text='bbbb')
        tv.column('starttime', anchor='center', width=100)
        tv.heading('endtime', text='lo que sea')
        tv.column('endtime', anchor='center', width=100)
        tv.heading('status', text='No se')
        tv.column('status', anchor='center', width=100)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)


        for i in range(99999):
            self.treeview.insert('', '999', text=variable, values=('xXx',
                             i, 'Ok'))

    def LoadTable(self):
        self.treeview.insert('', '999', text=variable, values=('xXx',
                             '0.0xxx', 'Ok'))
    

def main():
    root = Tk()
    App(root)
     
    root.mainloop()


if __name__ == '__main__':
    main()
