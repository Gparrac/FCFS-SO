from tkinter import *
class form:
    def __init__(self):
        self.win1 = Tk()
        self.win1.config(background='#0d1011')
        #variables
        self.count_nodes = IntVar(value=0)
        self.error = StringVar(value="")
        #formulario
        
        Label(self.win1, text="Cuantos procesos necesitas?",fg="white", background='#0d1011').pack(side=TOP, expand=1,fill=X,ipadx=5)
        Entry(self.win1,textvariable=self.count_nodes,background='#0d1011', highlightbackground = "#0d1011", highlightcolor= "#fd971f",highlightthickness=0,fg="white").pack(side=TOP, expand=1,fill=X, pady=10)
        Label(self.win1, textvariable=self.error,fg="white", background='#0d1011').pack(side=TOP, expand=1,fill=X)
        Button(self.win1,text="Comenzar simulación",background='#66d9ef',fg='#0d1011',command=self.start).pack(side=TOP, ipadx=5,expand=1,fill=X)
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