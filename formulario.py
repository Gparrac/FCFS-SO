from tkinter import *
class form:
    def __init__(self):
        self.win1 = Tk()
        #variables
        self.count_nodes = IntVar(0)
        self.error = StringVar("")
        #formulario
        
        Label(self.win1, text="Cuantos nodos necesitas?").pack(side=TOP, expand=1,fill=X)
        Entry(self.win1,textvariable=self.count_nodes).pack(side=TOP, expand=1,fill=X, pady=10)
        Label(self.win1, textvariable=self.error).pack(side=TOP, expand=1,fill=X)
        Button(self.win1,text="Comenzar simulación", command=self.start).pack(side=TOP, expand=1,fill=X)
        self.win1.mainloop()
    def start(self):
        if self.count_nodes.get() > 0 and self.count_nodes.get() <= 5:
            self.win1.destroy()
        else:
                self.error.set("El campo es requerido")
    def total_grid(self):
        return self.count_nodes.get() * 10
    def total_nodes(self):
         return self.count_nodes.get()
if __name__ == '__main__':
     app = form()