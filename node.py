from tkinter import *


class node:  # creamos estructura nodo
    def __init__(self, name, nex_node=None):
        self.name = name
        self.next = nex_node
        self.rafaga = IntVar(value=0)
        self.t_llegada = IntVar(value=0)
        self.t_final = IntVar(value=0)
        self.t_comienzo = IntVar(value=0)
        self.t_retorno = IntVar(value=0)
        self.t_espera = IntVar(value=0)
        self.bloqueo = StringVar(value="without")  # with, without, run
        self.auxRafaga = 1

    def create_space(self, window, last_chart, last_table, total_pro, row_table):
        self.row_chart = last_chart
        Label(window, text=self.name, background='#0d1011',fg="#fd971f", font=("Arial",17)).grid(
            column=0, row=last_chart, padx=5, pady=5)
        Label(window, text=self.name, background='#0d1011',fg="#fd971f", font=("Arial",17)).grid(
            column=1, row=last_table, padx=5, pady=5, columnspan=total_pro)
        Entry(window, textvariable=self.t_llegada, width=4,background='#0d1011',fg="white",font=('Arial',17)).grid(
            column=row_table, row=last_table, padx=5, pady=5, columnspan=row_table)
        Entry(window, textvariable=self.rafaga, width=4, background='#0d1011',fg="white",font=('Arial',17)).grid(
            column=row_table*2, row=last_table, padx=5, pady=5, columnspan=row_table)
        Label(window, textvariable=self.t_comienzo, width=4, background='#0d1011',fg="white",font=('Arial',17)).grid(
            column=row_table*3, row=last_table, padx=5, pady=5, columnspan=row_table)
        Label(window, textvariable=self.t_final, width=4, background='#0d1011',fg="white",font=('Arial',17)).grid(
            column=row_table*4, row=last_table, padx=5, pady=5, columnspan=row_table)
        Label(window, textvariable=self.t_retorno, width=4, background='#0d1011',fg="white",font=('Arial',17)).grid(
            column=row_table*5, row=last_table, padx=5, pady=5, columnspan=row_table)
        Label(window, textvariable=self.t_espera, width=4, background='#0d1011',fg="white",font=('Arial',17)).grid(
            column=row_table*6, row=last_table, padx=5, pady=5, columnspan=row_table)

    def run_critical_section(self, window, column, val):
        
        if val:
            if self.auxRafaga <= self.rafaga.get():
                if self.bloqueo.get() == 'with':
                    self.bloqueo.set('without')
                if self.auxRafaga == 1:                    
                    self.t_comienzo.set(column-1)                
                self.cal_t_final()
                self.cal_t_retorno()
                self.cal_t_espera()
                self.auxRafaga += 1
                Label(window, width=2, height=1, background="#a6e22e").grid(
                    column=column, row=self.row_chart, padx=5, pady=5)
                return False
            else:                   
                Label(window, width=2, height=1, background="#777777").grid(
                    column=column, row=self.row_chart, padx=5, pady=5)
                return True
        else:
            if self.bloqueo.get() == 'without':
                Label(window, width=2, height=1, background="#777777").grid(
                    column=column, row=self.row_chart, padx=5, pady=5)
                return True
            else:
                Label(window, width=2, height=1, background="#f92672").grid(
                    column=column, row=self.row_chart, padx=5, pady=5)
                return True

    def cal_t_final(self):
        self.t_final.set(self.auxRafaga+self.t_comienzo.get())

    def cal_t_retorno(self):
        self.t_retorno.set(self.t_final.get()-self.t_llegada.get())

    def cal_t_espera(self):
        self.t_espera.set(self.t_retorno.get()-self.auxRafaga)

    def change_values(self, name, rafaga, auxRafaga ,t_llegada, t_final, t_comienzo, t_retorno, t_espera, bloqueo, row_chart):
        self.name = name
        self.rafaga = rafaga
        self.t_llegada = t_llegada
        self.t_final = t_final
        self.t_comienzo = t_comienzo
        self.t_retorno = t_retorno
        self.t_espera = t_espera
        self.bloqueo = bloqueo
        self.row_chart = row_chart
        self.auxRafaga = auxRafaga

    def print(self):
        print('----')
        print('name', self.name)
        print('rafaga', self.auxRafaga)
        print('estado', self.bloqueo.get())
        print('----')
