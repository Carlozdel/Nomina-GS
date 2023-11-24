# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:59:50 2023

@author: cdelgad3
"""

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import getpass
# import MySQLdb as mdbk

# import pandas as pd

user_name = getpass.getuser()
# print(path)

connection =  sqlite3.connect('GS_DataBase')
cursorDB = connection.cursor()

root = Tk()
root.title("Nomina General Services")
root.geometry("1300x850")
# root.attributes('-fullscreen',True)
root.config(bg='Gray')
# root.grid_rowconfigure(0, weight=1)
# root.grid_columnconfigure(0, weight=1)
# root.resizable(0,0)

frame1 = LabelFrame(root, text="Datos del Empleado", font=('Arial', 14))
frame2 = LabelFrame(root, text="Busqueda", font=('Arial', 14))
frame3 = LabelFrame(root, text="Listado", font=('Arial', 14))


frame1.pack(fill="both", expand="yes", padx=20, pady=10)
frame2.pack(fill="both", expand="yes", padx=20, pady=10)
frame3.pack(fill="both", expand="Yes", padx=20, pady=10)


trv = ttk.Treeview(frame3, columns=(1,2,3,4,5,6,7,8,9,10), show="headings", height="18",selectmode='browse' )
trv.pack()


trv.column("#1",anchor=CENTER,widt=80)
trv.column("#2",anchor=CENTER,widt=120)
trv.column("#3",widt=200)
trv.column("#4",anchor=CENTER,widt=120)
trv.column("#5",anchor=CENTER,widt=140)
trv.column("#6",anchor=CENTER,widt=80)
trv.column("#7",anchor=CENTER,widt=120)
trv.column("#8",anchor=CENTER,widt=120)
trv.column("#9",anchor=CENTER,widt=120)
trv.column("#10",anchor=CENTER,widt=120)


trv.heading(1, text="IGNITION")
trv.heading(2, text="COST CENTER")
trv.heading(3, text="FULL NAME")
trv.heading(4, text="SHIFT")
trv.heading(5, text="HRS POR SEMANA")
trv.heading(6, text="COMEDOR")
trv.heading(7, text="MODIFIER")
trv.heading(8, text="MODIFIED DT")
trv.heading(9, text="FWEEK")
trv.heading(10, text="APPROVED")


lbl = Label(frame2, width=10, text="Buscar", font=("", 13) )
lbl.pack(side =tk.LEFT, padx=10)
ent = tk.Entry(frame2,font=("", 13))
ent.pack(side =tk.LEFT, padx=6)
bnt = tk.Button(frame2, width=10, text="Buscar", font=("", 13),
    command=lambda: query_buscar(ent.get()))
bnt.pack(side=tk.LEFT, padx=6)

# def func(id):
#     print(id)

cbtn = Button(frame2,  width=10,text="Limpiar", font=("", 13),
    command=lambda: query_buscar(0))
cbtn.pack(side=tk.LEFT, padx=6)
 
# Ignition INTEGER, "Cost Center" INTEGER, "Full Name" TEXT, Shift TEXT, "HRS X SEM" TEXT, COMEDOR INTEGER)""")
lbl1 = Label(frame1, text="Ignition",font=("", 13))
lbl1.grid(column=0, row=0, padx=5, pady=3)
ent1 = Entry(frame1,font=("", 13))
ent1.grid(column=1, row=0, padx=5, pady=3)

lbl2 = Label(frame1, text="Cost Center",font=("", 13))
lbl2.grid(column=0, row=1, padx=5, pady=3)
ent2 = ttk.Combobox(frame1, value=('8274'	,'8113'	,'8317'	,'8236'	,'9052'	,'8272'	,'8099'	,'9992'	,'8026'	,'8270'	,'8264'),font=("", 11))
ent2.grid(column=1, row=1, padx=5, pady=3)

lbl3 = Label(frame1, text="Full Name",font=("", 13))
lbl3.grid(column=0, row=2, padx=5, pady=3)
ent3 = Entry(frame1,font=("", 13))
ent3.grid(column=1, row=2, padx=5, pady=3)

lbl4 = Label(frame1, text="Shift",font=("", 13))
lbl4.grid(column=0, row=3, padx=5, pady=3)
#ent4 = Entry(frame1,font=("", 13))
ent4 = ttk.Combobox(frame1, value=('Full Time', 'Part Time'),font=("", 11))

ent4.grid(column=1, row=3, padx=5, pady=3)

lbl5 = Label(frame1, text="Hrs Por Semana",font=("", 13))
lbl5.grid(column=0, row=4, padx=5, pady=3)
ent5 = ttk.Combobox(frame1, value=('45', '36', '27', '18', '9'),font=("", 11))
ent5.grid(column=1, row=4, padx=5, pady=3)

lbl6 = Label(frame1, text="Comedor",font=("", 13))
lbl6.grid(column=0, row=5, padx=5, pady=3)
ent6 = ttk.Combobox(frame1, value=('0', '103.74'),font=("", 11))
ent6.grid(column=1, row=5, padx=5, pady=3)

# modify_var  = ent1 + "," + ent2 + "," + ent3 + "," + ent4 + "," + ent5 + "," + ent6

agregar_btn = Button(frame1, width=10, text="Agregar",font=("", 13) ,
    command=lambda: query_agregar("3," + ent1.get() + "," + ent2.get() + "," + ent3.get() + "," + ent4.get() + "," + ent5.get() + "," + ent6.get()))
agregar_btn.grid(column=4, row=1, padx=5, pady=3)
 
actualizar_btn = Button(frame1, width=10, text="Actualizar",font=("", 13),
    command=lambda: query_agregar("4," + ent1.get() + "," + ent2.get() + "," + ent3.get() + "," + ent4.get() + "," + ent5.get() + "," + ent6.get()))
actualizar_btn.grid(column=4, row=2, padx=5, pady=3)
  
eliminar_btn = Button(frame1, width=10, text="Eliminar",font=("", 13))
eliminar_btn.grid(column=4, row=3, padx=5, pady=3)
# id=1


def query_buscar(id):
    # print(id)
    mydata = str(id)
    if mydata == '<built-in function id>' or mydata == '0' :
        for row in trv.get_children():
            trv.delete(row)
        ent.delete(0, 'end')
        ent1.delete(0, 'end')
        ent2.delete(0, 'end')
        ent3.delete(0, 'end')
        ent4.delete(0, 'end')
        ent5.delete(0, 'end')
        ent6.delete(0, 'end')
        query = cursorDB.execute("SELECT * From ALL_EMPLOYEES")
        Query_result = list(query)

        for row in Query_result:
            trv.insert("",'end',text=row[0],values=list(row)) # add data 

    else:
        for row in trv.get_children():
            trv.delete(row)

        query = " SELECT * FROM ALL_EMPLOYEES WHERE IGNITION LIKE " + "'%" + id + "%'" + " OR [Full Name] LIKE " + "'%" + id + "%'" 
        query_res = cursorDB.execute(query )
        Query_result = list(query_res)

        for row in Query_result:
            trv.insert("",'end',text=row[0],values=list(row)) 

def query_agregar(id):
    mydata_2 = str(id)
    new_data = mydata_2
    splitted = new_data.split(",")
    # print(splitted)
    if splitted[0] == '3':
        msg_box = messagebox.askokcancel("Adding Info","You are attempting to add a new record to the DB")
        print(msg_box)

        if msg_box == True:
            # for i in range(1, 6):
                if splitted[1] == "" or  splitted[2] == ""  or  splitted[3] == "" or  splitted[4] == "" or  splitted[5] == "" or  splitted[6] == "":
                    tk.messagebox.showinfo('Addition Cancelled','There are empty fields in your addition, employee has not been added to DB')
                    # return
                else:

                    cursorDB.execute("INSERT INTO ALL_EMPLOYEES  VALUES (" + splitted[1] + " ," + splitted[2] + " ," + "'" + splitted[3] +  "'"  + " ," +  "'" + splitted[4] + "'" + " ," + splitted[5] + " ," + splitted[6] + ",'','','','')")
                    connection.commit()
                    tk.messagebox.showinfo('Addition Completed', 'You virtually added a new record')
                    for row in trv.get_children():
                        trv.delete(row)
                    ent.delete(0, 'end')
                    ent1.delete(0, 'end')
                    ent2.delete(0, 'end')
                    ent3.delete(0, 'end')
                    ent4.delete(0, 'end')
                    ent5.delete(0, 'end')
                    ent6.delete(0, 'end')
                    query = " SELECT * FROM ALL_EMPLOYEES WHERE IGNITION = " + splitted[1]
                    query_res = cursorDB.execute(query )
                    Query_result = list(query_res)

                    for row in Query_result:
                        trv.insert("",'end',text=row[0],values=list(row)) 
                    # connection.close()
                    return
        else:   
            tk.messagebox.showinfo('Return', 'You cancelled the adding process')
            return
    elif splitted[0] == '4':


        if splitted[1] == '':
            msg_box = messagebox.askokcancel("Attempt to modify Info","You did not select an employee to modify.")
        else:
            query_mod = " SELECT * FROM ALL_EMPLOYEES WHERE IGNITION =" + "'" + splitted[1] + "'"
            query_res_mod = cursorDB.execute(query_mod)
            rows = query_res_mod.fetchone()
            print(rows)
            query_str = str(rows)
            split_data = query_str.split(",")
            
            if rows is None:
                msg_box = messagebox.askokcancel("Attempt to modify Info","Employee was not found in DB") 
            else:    
                # print(query_mod)
                msg_box = messagebox.askokcancel("Attempt to modify Info","Are you sure you want to modify info for" + split_data[2] + "?")
                # msg_box = messagebox.askokcancel("Attempt to modify Info","Are you sure you want to modify info for?")

                if splitted[1] == "" or  splitted[2] == ""  or  splitted[3] == "" or  splitted[4] == "" or  splitted[5] == "" or  splitted[6] == "":
                    tk.messagebox.showinfo('Modifying process Cancelled','In order to do a modify, you must fill out all the fields, Employee was not modified in DB')       
                else:
                    cursorDB.execute("DELETE FROM ALL_EMPLOYEES WHERE IGNITION = " + "'" + splitted[1] + "'")
                    connection.commit()
                    var_init = split_data[0][1:]
                    var_final = split_data[9][:-1]
                    print(var_init,var_final)
                    query_to_add = "INSERT INTO ALL_EMPLOYEES  VALUES (" + var_init + " ," + split_data[1] + " ," + split_data[2] + " ," + split_data[3]   + " ,"  + split_data[4]  + " ," + split_data[5] + " ," +  "'" + split_data[6] + "'"  + " ," + "'"  + split_data[7] + "'"  + " ," + "'"  +split_data[8] + "'"  + " ," + "'" + var_final  + "'" + ")"    
                    # query_to_add = query_to_add[1:-1]
                    # print(query_to_add)
                    cursorDB.execute(query_to_add)
                    
                    connection.commit()                    


query_buscar(id)

        
root.mainloop()


