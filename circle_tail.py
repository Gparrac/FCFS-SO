from tkinter import *
from node import node 
from formulario import form
import math
import random
class circle_list:
    def __init__(self,window, total_pro, total_grid,cuantum):

        #variables iniciales
        self.window = window
        self.total_pro = total_pro
        self.total_grid = total_grid if total_grid > 30 else 40;
        self.cab = node('raiz')
        self.cab.next = self.cab
        self.rows_table = math.trunc(self.total_grid/8)
        self.count_box = 1
        self.semaforo = StringVar(value="-")
        self.rafaga=IntVar(value=0)
        self.cuantum = cuantum    
        self.aux_cuantum = self.cuantum    
        #bloqueos 
        self.row_block = self.total_pro+20        
        self.col_block = self.rows_table

    def addNode(self):
        self.count_chart = 1
        self.count_table = self.total_pro + 11
        self.count_rows_tab = self.rows_table
        for i in range(1,self.total_pro+1):
            last_node = self.search_last()
            name = f'P {i}'
            last_node.next = node(name, self.cab)  
            last_node.next.create_space(self.window,self.count_chart,self.count_table,self.total_pro,self.count_rows_tab,self.row_block,self.col_block)        
            self.count_chart += 1
            self.count_table += 1
            self.col_block += 2
    def create_dashboard(self):        
        Label(self.window, width=2, textvariable=self.semaforo, background='#a6e22e' ,height=1,fg="#0d1011",font=('Arial',15)).grid(column=0,row=0,padx=5,pady=5, ipadx=3,ipady=3)
        for i in range(0,self.total_grid ):
            
            Label(self.window, width=2,text=i+1  ,height=1,background='#0d1011',fg="#66d9ef",font=('Arial',15)).grid(column=i+1,row=0,padx=5,pady=5)
        Entry(self.window, textvariable=self.rafaga,background='#0d1011',fg='#fd971f',width=2,font=('Arial',22)).grid(column=0,row=self.total_pro+9,pady=20)
        Button(self.window, text="+",command=self.addNewProcc,background='#fd971f',fg='#0d1011',font=('Arial',17)).grid(column=1,row=self.total_pro+9,pady=20)
        Button(self.window, text="Round Robin",command=self.start,background='#fd971f',fg='#0d1011',font=("Arial",25)).grid(column=2,row=self.total_pro+9,columnspan=self.total_grid-9,pady=20)
        Label(self.window, text="Cuantum", background="#0d1011",fg="#66d9ef",font=('Arial',20)).grid(column=self.total_grid-9,row=self.total_pro+9,columnspan=4)
        Label(self.window, text=self.cuantum,background='#0d1011',fg='#fd971f',width=2,font=('Arial',22)).grid(column=self.total_grid-4,row=self.total_pro+9,pady=20)
        LabelFrame(self.window,background="red").grid(column=0,row=self.total_pro+2,columnspan=self.total_grid)
        tableHeader=LabelFrame(self.window,background="red").grid(column=0,row=self.total_pro+10,columnspan=self.total_grid)
        #cabecera tabla
        Label(tableHeader, text="Proceso", background="#0d1011",fg="#66d9ef",font=('Arial',20)).grid(column=1,row=self.total_pro+10,columnspan=self.rows_table)
        Label(tableHeader, text="T. llegada", background="#0d1011",fg="#66d9ef",font=('Arial',20)).grid(column=self.rows_table,row=self.total_pro+10,columnspan=self.rows_table)
        Label(tableHeader, text="Rafaga", background="#0d1011",fg="#66d9ef",font=('Arial',20)).grid(column=self.rows_table*2,row=self.total_pro+10,columnspan=self.rows_table)
        Label(tableHeader, text="T. Comienzo", background="#0d1011",fg="#66d9ef",font=('Arial',20)).grid(column=self.rows_table*3,row=self.total_pro+10,columnspan=self.rows_table)
        Label(tableHeader, text="T. Final", background="#0d1011",fg="#66d9ef",font=('Arial',20)).grid(column=self.rows_table*4,row=self.total_pro+10,columnspan=self.rows_table)
        Label(tableHeader, text="T. Retorno", background="#0d1011",fg="#66d9ef",font=('Arial',20)).grid(column=self.rows_table*5,row=self.total_pro+10,columnspan=self.rows_table)
        Label(tableHeader, text="T. Espera", background="#0d1011",fg="#66d9ef",font=('Arial',20)).grid(column=self.rows_table*6,row=self.total_pro+10,columnspan=self.rows_table)        
        #cola de procesos
        Label(tableHeader, text="Registro", background="#0d1011",fg="#66d9ef",font=('Arial',20)).grid(column=1,row=self.row_block,columnspan=self.rows_table)                
        

    def start(self):
        self.order_asc()
        self.pro = self.cab.next
        self.print_all()        
        window.after(3000,app.run_chart)
    def search_last(self):
        q = self.cab.next
        while q.next != self.cab:
            q = q.next;   
        return q
    def order_asc(self):
        aux = node('aux')
        q=self.cab.next
        while q != self.cab:
            j= q.next
            while (j != self.cab):
                if q.t_llegada.get() > j.t_llegada.get(): #q > j
                    aux.change_values(q.name,q.rafaga,q.auxRafaga,q.t_llegada,q.t_final,q.t_comienzo,q.t_retorno,q.t_espera,q.bloqueo,q.row_chart,q.espera)
                    q.change_values(j.name,j.rafaga,j.auxRafaga,j.t_llegada,j.t_final,j.t_comienzo,j.t_retorno,j.t_espera,j.bloqueo,j.row_chart,j.espera)
                    j.change_values(aux.name,aux.rafaga,aux.auxRafaga,aux.t_llegada,aux.t_final,aux.t_comienzo,aux.t_retorno,aux.t_espera,aux.bloqueo,aux.row_chart,aux.espera)                    
                j = j.next
            q = q.next                   
    def print_all(self):
        q = self.cab.next
        while q != self.cab:
            q.print()
            q = q.next;   
    def run_chart(self):
        self.block_proc()
        if self.count_box <= self.total_grid:
            val = True;
            q = self.cab.next
            while q != self.cab:
                if not q.run_critical_section(self.window,self.count_box,val) :  
                    self.semaforo.set(q.name)
                    while q.auxRafaga > q.rafaga.get() and q.next != self.cab:
                        q.next.run_critical_section(self.window,self.count_box,val)
                        self.semaforo.set(q.next.name)
                        q=q.next
                    val = False    
                    self.pro = q   #pendiente    
                
                q = q.next
            self.aux_cuantum -= 1
            self.count_box += 1
            if val:
                self.semaforo.set('-')
            
        
        self.window.after(3000,self.run_chart)
    def block_proc(self):

        dec = random.choice([True,False])
        if self.aux_cuantum == 0 or (dec  and self.pro.auxRafaga != 1) and self.pro.auxRafaga <= self.pro.rafaga.get() and self.pro.next != self.cab:                     
                    self.aux_cuantum = self.cuantum      
                    aux = node('aux')
                    q = self.pro
                    if q.next != self.cab:                        
                        self.pro.block_proccess(self.window,self.col_block,self.row_block)
                        self.col_block += 2
                    while q.next !=self.cab:                         
                        
                        self.pro.bloqueo.set("with")
                        aux.change_values(q.name,q.rafaga, q.auxRafaga,q.t_llegada,q.t_final,q.t_comienzo,q.t_retorno,q.t_espera,q.bloqueo,q.row_chart,q.espera)
                        q.change_values(q.next.name,q.next.rafaga,q.next.auxRafaga,q.next.t_llegada,q.next.t_final,q.next.t_comienzo,q.next.t_retorno,q.next.t_espera,q.next.bloqueo,q.next.row_chart,q.next.espera)
                        q.next.change_values(aux.name,aux.rafaga,aux.auxRafaga,aux.t_llegada,aux.t_final,aux.t_comienzo,aux.t_retorno,aux.t_espera,aux.bloqueo,aux.row_chart,aux.espera)
                        q=q.next
                    self.print_all()  
   
    def addNewProcc(self):
        self.window.after(1000,self.insertProcc)
    def insertProcc(self):
        ln = self.search_last()
        name = f'P {self.total_pro+1}'
        ln.next = node(name, self.cab,rafaga=self.rafaga.get())  
        ln.next.create_space(self.window,self.count_chart,self.count_table,self.total_pro,self.count_rows_tab)  
        self.count_chart += 1
        self.count_table += 1  
        self.total_pro += 1
if __name__ == '__main__':
    form = form()
    window = Tk()
    window.title('FCFS')
    window.config(background='#0d1011')
    app = circle_list(window, form.total_nodes(), form.total_grid(),form.get_cuantum())
    app.addNode()
    app.create_dashboard()
    
    window.mainloop()
