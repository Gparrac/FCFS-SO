from tkinter import *
from node import node 
from formulario import form
import math
import random
class circle_list:
    def __init__(self,window, total_pro, total_grid):

        #variables iniciales
        self.window = window
        self.total_pro = total_pro
        self.total_grid = total_grid
        self.cab = node('raiz')
        self.cab.next = self.cab
        self.rows_table = math.trunc(self.total_grid/7)
        self.count_box = 1
        
    def addNode(self):
        count_chart = 1
        count_table = self.total_pro + 3
        count_rows_tab = self.rows_table
        for i in range(1,self.total_pro+1):
            last_node = self.search_last()
            name = f'nd ${i}'
            last_node.next = node(name, self.cab)  
            last_node.next.create_space(self.window,count_chart,count_table,self.total_pro,count_rows_tab)        
            count_chart += 1
            count_table += 1
    def create_dashboard(self):        
        
        for i in range(1,self.total_grid + 1):
            Label(self.window, width=2,text=i ,height=1).grid(column=i,row=0,padx=5,pady=5)
        Button(self.window, text="FCFS",command=self.start).grid(column=1,row=self.total_pro+1,columnspan=self.total_grid)
        tableHeader=LabelFrame(self.window,background="red").grid(column=0,row=self.total_pro+2,columnspan=self.total_grid)
        Label(tableHeader, text="Proceso", background="yellow").grid(column=1,row=self.total_pro+2,columnspan=self.rows_table)
        Label(tableHeader, text="T. llegada", background="yellow").grid(column=self.rows_table,row=self.total_pro+2,columnspan=self.rows_table)
        Label(tableHeader, text="Rafaga", background="yellow").grid(column=self.rows_table*2,row=self.total_pro+2,columnspan=self.rows_table)
        Label(tableHeader, text="T. Comienzo", background="yellow").grid(column=self.rows_table*3,row=self.total_pro+2,columnspan=self.rows_table)
        Label(tableHeader, text="T. Final", background="yellow").grid(column=self.rows_table*4,row=self.total_pro+2,columnspan=self.rows_table)
        Label(tableHeader, text="T. Retorno", background="yellow").grid(column=self.rows_table*5,row=self.total_pro+2,columnspan=self.rows_table)
        Label(tableHeader, text="T. Espera", background="yellow").grid(column=self.rows_table*6,row=self.total_pro+2,columnspan=self.rows_table)        
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
                    aux.change_values(q.name,q.rafaga,q.auxRafaga,q.t_llegada,q.t_final,q.t_comienzo,q.t_retorno,q.t_espera,q.bloqueo,q.row_chart)
                    q.change_values(j.name,j.rafaga,j.auxRafaga,j.t_llegada,j.t_final,j.t_comienzo,j.t_retorno,j.t_espera,j.bloqueo,j.row_chart)
                    j.change_values(aux.name,aux.rafaga,aux.auxRafaga,aux.t_llegada,aux.t_final,aux.t_comienzo,aux.t_retorno,aux.t_espera,aux.bloqueo,aux.row_chart)
                j = j.next
            q = q.next                   
    def print_all(self):
        q = self.cab.next
        while q != self.cab:
            q.print()
            q = q.next;   
    def run_chart(self):
        self.block_proc(self.count_box)
        print('loop=>',self.count_box)
        if self.count_box <= self.total_grid:
            print('entrando!')
            val = True;
            q = self.cab.next
            while q != self.cab:
                if not q.run_critical_section(self.window,self.count_box,val) :                                         
                    if q.auxRafaga > q.rafaga.get() and q.next != self.cab:
                        q.next.run_critical_section(self.window,self.count_box,val)
                        q=q.next
                    val = False    
                    self.pro = q   #pendiente    
                   #print(self.count_box,'prueba=>',self.pro.name,'rafaga',self.pro.auxRafaga)                    
                         
                q = q.next
            self.count_box += 1
            
        
        self.window.after(3000,self.run_chart)
    def block_proc(self,loop):
        
        # print('==> antes bloqueo')
        # self.print_all()
        dec = random.choice([True,False])
        if  dec and self.pro.next != self.cab and self.pro.auxRafaga != 1 and self.pro.auxRafaga <= self.pro.rafaga.get():        
                    print(loop,'prueba=>',self.pro.name,'rafaga',self.pro.auxRafaga)                    
                    aux = node('aux')
                    self.pro.bloqueo.set("with")
                    aux.change_values(self.pro.name,self.pro.rafaga, self.pro.auxRafaga,self.pro.t_llegada,self.pro.t_final,self.pro.t_comienzo,self.pro.t_retorno,self.pro.t_espera,self.pro.bloqueo,self.pro.row_chart)
                    self.pro.change_values(self.pro.next.name,self.pro.next.rafaga,self.pro.next.auxRafaga,self.pro.next.t_llegada,self.pro.next.t_final,self.pro.next.t_comienzo,self.pro.next.t_retorno,self.pro.next.t_espera,self.pro.next.bloqueo,self.pro.next.row_chart)
                    self.pro.next.change_values(aux.name,aux.rafaga,aux.auxRafaga,aux.t_llegada,aux.t_final,aux.t_comienzo,aux.t_retorno,aux.t_espera,aux.bloqueo,aux.row_chart)
                    print('==> despues bloqueo')
                    self.print_all()            
if __name__ == '__main__':
    form = form()
    window = Tk()
    window.title('FCFT')
    app = circle_list(window, form.total_nodes(), form.total_grid())
    app.addNode()
    app.create_dashboard()
    
    window.mainloop()
