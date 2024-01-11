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
import itertools
import pandas as pd
import os
import glob
import pyodbc
import subprocess

#AGREGAR LA OPCION DE CONSULTAR EL SHARED SERVER PARA PODER LEER LA JERARQUIA.



# import openpyxl
# subprocess.Popen(f"ssh {'webfuser'}@{'pr-wildcat-xl09.autozone.com' } {'azwfu$r'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

# f"echo {'azwfu$r'} | ssh {'webfuser'}@{'pr-wildcat-xl09.autozone.com' } "


# df = pd.read_csv(r"./az/webfocus/ibi/apps/flatfiles/uhro/wf8/ff_uito_test3.txt")
pd.read_csv('ftp://webfuser:azwfu$r@pr-wildcat-xl09.autozone.com/az/webfocus/ibi/apps/flatfiles/uito/wf8/ff_uito_test3.txt')


# print(df)

exit(0)

# files = [f for f in os.listdir('c:/Users/cdelgad3.DZ/Downloads/') if not os.path.isdir(f)]
# recentExc = [f for f in files if f[-5:] == '.xlsx']
# r = recentExc.sort(key = lambda f: os.path.getctime('c:/Users/cdelgad3.DZ/Downloads/'), reverse = True)
# print(r)
# downloads = os.listdir('c:/Users/cdelgad3.DZ/Downloads/')

# is_file = [True if '.' in item else False for item in downloads]
# files = [item for keep, item in zip(is_file, downloads) if keep]
 
# print(files) 

list_of_files = glob.glob(r'c:/Users/cdelgad3.DZ/Downloads/Payroll/*') 
latest_file = max(list_of_files, key=os.path.getctime)

 
print(latest_file)
 
# df = pd.read_excel('c:/Users/cdelgad3.DZ/Downloads/General Services W51 Dec 10-16, 2023.xlsx', skiprows=[0,1,2])
df = pd.read_excel(latest_file, skiprows=[0,1,2])
print(df)

# exit(0)


user_name = getpass.getuser()
connection =  sqlite3.connect('GS_DataBase')
cursorDB = connection.cursor()

root = Tk()
root.title("General Services Payroll")
# root.geometry("1500x850")
# root.attributes('-fullscreen',True)

root.state("zoomed")
root.config(bg='Gray')

frame1 = LabelFrame(root, text="Employee Data", font=('Arial', 14))
frame2 = LabelFrame(root, text="Search", font=('Arial', 14))
frame3 = LabelFrame(root, text="List", font=('Arial', 14))


frame1.pack(fill="both", expand="yes", padx=20, pady=10)
frame2.pack(fill="both", expand="yes", padx=20, pady=10)
frame3.pack(fill="both", expand="Yes", padx=20, pady=10)


trv = ttk.Treeview(frame3, columns=(1,2,3,4,5,6,7,8,9,10,11,12), show="headings", height="18",selectmode='browse' )
trv.pack()


trv.column("#1",anchor=CENTER,widt=80)
trv.column("#2",anchor=CENTER,widt=120)
trv.column("#3",widt=200)
trv.column("#4",anchor=CENTER,widt=80)
trv.column("#5",anchor=CENTER,widt=70)
trv.column("#6",anchor=CENTER,widt=80)
trv.column("#7",anchor=CENTER,widt=200)
trv.column("#8",anchor=CENTER,widt=120)
trv.column("#9",anchor=CENTER,widt=60)
trv.column("#10",anchor=CENTER,widt=90)
trv.column("#11",anchor=CENTER,widt=200)
trv.column("#12",anchor=CENTER,widt=60)


trv.heading(1, text="IGNITION")
trv.heading(2, text="COST CENTER")
trv.heading(3, text="FULL NAME")
trv.heading(4, text="SHIFT")
trv.heading(5, text="HRS WEEK")
trv.heading(6, text="COMEDOR")
trv.heading(7, text="MODIFIER")
trv.heading(8, text="MODIFIED DT")
trv.heading(9, text="FWEEK")
trv.heading(10, text="APPROVED")
trv.heading(11, text="SUPERVISOR")
trv.heading(12, text="HOLIDAY")


lbl = Label(frame2, width=10, text="", font=("", 13) )
lbl.pack(side =tk.LEFT, padx=10)
ent = tk.Entry(frame2,font=("", 13))
ent.pack(side =tk.LEFT, padx=6)
bnt = tk.Button(frame2, width=10, text="Search", font=("", 13),
    command=lambda: query_buscar(ent.get()))
bnt.pack(side=tk.LEFT, padx=6)

# def func(id):
#     print(id)

cbtn = Button(frame2,  width=10,text="Clear", font=("", 13),
    command=lambda: query_buscar(0))
cbtn.pack(side=tk.LEFT, padx=6)
 
# Ignition INTEGER, "Cost Center" INTEGER, "Full Name" TEXT, Shift TEXT, "HRS X SEM" TEXT, COMEDOR INTEGER)""")
lbl1 = Label(frame1, text="Ignition",font=("", 13))
lbl1.grid(column=0, row=0, padx=5, pady=3)
ent1 = Entry(frame1,font=("", 13), justify=CENTER)
ent1.grid(column=1, row=0, padx=5, pady=3)

lbl2 = Label(frame1, text="Cost Center",font=("", 13))
lbl2.grid(column=0, row=1, padx=5, pady=3)
ent2 = ttk.Combobox(frame1, value=('8274'	,'8113'	,'8317'	,'8236'	,'9052'	,'8272'	,'8099'	,'9992'	,'8026'	,'8270'	,'8264'),font=("", 11), justify=CENTER)
ent2.grid(column=1, row=1, padx=5, pady=3)

lbl3 = Label(frame1, text="Full Name",font=("", 13))
lbl3.grid(column=0, row=2, padx=5, pady=3)


query_NAME = cursorDB.execute("SELECT [Full Name] From ALL_EMPLOYEES")

# exit(0)


names = list(query_NAME)
names_list = names
ent3 = ttk.Combobox(frame1, value=(list(itertools.chain.from_iterable(names_list))),font=("", 11),width=30, justify=CENTER)
# ent3 = ttk.Combobox(frame1, names ,font=("", 11),width=30, justify=CENTER)
ent3.grid(column=1, row=2, padx=5, pady=3)

lbl4 = Label(frame1, text="Shift",font=("", 13))
lbl4.grid(column=0, row=3, padx=5, pady=3)
#ent4 = Entry(frame1,font=("", 13))
ent4 = ttk.Combobox(frame1, value=('Full Time', 'Part Time'),font=("", 11), justify=CENTER)

ent4.grid(column=1, row=3, padx=5, pady=3)

lbl5 = Label(frame1, text="Hrs Per Week",font=("", 13))
lbl5.grid(column=0, row=4, padx=5, pady=3)
ent5 = ttk.Combobox(frame1, value=('45', '36', '27', '18', '9'),font=("", 11), justify=CENTER)
ent5.grid(column=1, row=4, padx=5, pady=3)


# lbl6 = Label(frame1, text="WEEJK NBR",font=("", 13))
# lbl6.grid(column=4, row=1, padx=5, pady=3)
# ent6 = ttk.Combobox(frame1, value=('0', '103.74'),font=("", 11), justify=CENTER)
# ent6.grid(column=5, row=1, padx=5, pady=3)

lbl6 = Label(frame1, text="Comedor",font=("", 13))
lbl6.grid(column=4, row=1, padx=5, pady=3)
ent6 = ttk.Combobox(frame1, value=('0', '103.74'),font=("", 11), justify=CENTER)
ent6.grid(column=5, row=1, padx=5, pady=3)

lbl7 = Label(frame1, text="Holiday",font=("", 13))
lbl7.grid(column=4, row=2, padx=5, pady=3)
ent7 = ttk.Combobox(frame1, value=('Yes', 'No'),font=("", 11), justify=CENTER)
ent7.grid(column=5, row=2, padx=5, pady=3)

lbl8 = Label(frame1, text="Supervisor",font=("", 13))
lbl8.grid(column=4, row=3, padx=5, pady=3)
ent8 = ttk.Combobox(frame1, value=('Yes', 'No'),font=("", 11),width=30, justify=CENTER)
ent8.grid(column=5, row=3, padx=5, pady=3)

lbl9 = Label(frame1, text="Approved",font=("", 13))
lbl9.grid(column=4, row=4, padx=5, pady=3)
ent9 = ttk.Combobox(frame1, value=('YES', 'NO'),font=("", 11), justify=CENTER)
ent9.grid(column=5, row=4, padx=5, pady=3)

# modify_var  = ent1 + "," + ent2 + "," + ent3 + "," + ent4 + "," + ent5 + "," + ent6

agregar_btn = Button(frame1, width=10, text="Approve All",font=("", 13) )
agregar_btn.grid(column=6, row=4, padx=5, pady=3)

agregar_btn = Button(frame1, width=10, text="Find",font=("", 13) ,
    command=lambda: query_display(ent3.get()))
agregar_btn.grid(column=6, row=0, padx=5, pady=3)


agregar_btn = Button(frame1, width=10, text="Add",font=("", 13) ,
    command=lambda: query_agregar("3," + ent1.get() + "," + ent2.get() + "," + ent3.get() + "," + ent4.get() + "," + ent5.get() + "," + ent6.get()))
agregar_btn.grid(column=6, row=1, padx=5, pady=3)
 
actualizar_btn = Button(frame1, width=10, text="Modify",font=("", 13),
    command=lambda: query_agregar("4," + ent1.get() + "," + ent2.get() + "," + ent3.get() + "," + ent4.get() + "," + ent5.get() + "," + ent6.get()))
actualizar_btn.grid(column=6, row=2, padx=5, pady=3)
  
eliminar_btn = Button(frame1, width=10, text="Remove",font=("", 13))
eliminar_btn.grid(column=6, row=3, padx=5, pady=3)
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

                    cursorDB.execute("INSERT INTO ALL_EMPLOYEES  VALUES (" + splitted[1] + " ," + splitted[2] + " ," + "'" + splitted[3] +  "'"  + " ," +  "'" + splitted[4] + "'" + " ," + splitted[5] + " ," + splitted[6] + ",'','','','','','')")
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
            elif splitted[1] == "" or  splitted[2] == ""  or  splitted[3] == "" or  splitted[4] == "" or  splitted[5] == "" or  splitted[6] == "":    
                tk.messagebox.showinfo('Modifying process Cancelled','To modify a record, you must fill out all the fields, Employee was not modified in DB')       
            else:
                msg_box = messagebox.askokcancel("Attempt to modify Info","Are you sure you want to modify info for" + split_data[2] + "?")

                cursorDB.execute("DELETE FROM ALL_EMPLOYEES WHERE IGNITION = " + "'" + splitted[1] + "'")
                connection.commit()
                var_init = split_data[0][1:]
                var_final = split_data[9][:-1]
                print(var_init,var_final)
                query_to_add = "INSERT INTO ALL_EMPLOYEES  VALUES (" + var_init + " ," + "'" + splitted[2] + "'" + " ," +  "'" + splitted[3] +  "'" + " ," +  "'" + splitted[4]  +  "'"  + " ,"  + splitted[5]  + " ," + splitted[6] + " ," +  "'None'"  + " ," + "'None'"  + " ," + "'None'"  + " ," + "'None'"  + " ," + "'None'" +  "'None'" + ")"    
                print("--------------------------------------")
                print(query_to_add)
                                    
                cursorDB.execute(query_to_add)

                    
                connection.commit()                    

def query_display(id):
    mydata_2 = str(id)
    new_data2 = mydata_2
    print(new_data2)
    # if new_data2 == '<built-in function id>' or new_data2 == '0' or new_data2 == '':
    # for row in trv.get_children():
    print('You are in the function')
    # trv.delete(row)
    ent.delete(0, 'end')
    ent1.delete(0, 'end')
    ent2.delete(0, 'end')
    # ent3.delete(0, 'end')
    ent4.delete(0, 'end')
    ent5.delete(0, 'end')
    ent6.delete(0, 'end')
    ent7.delete(0, 'end')
    ent8.delete(0, 'end')
    ent9.delete(0, 'end')
    
    query_disp = " SELECT * FROM ALL_EMPLOYEES WHERE [Full Name]  = " + "'" + new_data2 + "'"
    query_res_3 = cursorDB.execute(query_disp )
    # Query_result_3 = list(query_res_3)
    rows = query_res_3.fetchone()
    print(rows)
    query_str_2 = str(rows)
    # split_data_2 = query_str_2.split(",")
    # query_str_2 = query_str_2.replace(",", "")
    split_data_2 = query_str_2.split("', '")
    
    # print('1 ' + split_data_2[0])
    # print('2 ' + split_data_2[1])
    # print('3 ' + split_data_2[2])
    # print('4 ' + split_data_2[3])
    # print('5 ' + split_data_2[4])
    # print('6 ' + split_data_2[5])
    # print('7 ' + split_data_2[6])
    # print('8 ' + split_data_2[7])
    # print('9 ' + split_data_2[8])
    # print('10 ' + split_data_2[9])
    # print('11 ' + split_data_2[10])
    # # print(split_data_2[11])
                        
        
        
    
    ent1.insert(0,split_data_2[0])
    ent2.insert(0,split_data_2[1])
    ent4.insert(0,split_data_2[3])
    ent5.insert(0,split_data_2[4])
    ent6.insert(0,split_data_2[5])
    ent7.insert(0,split_data_2[11])
    ent8.insert(0,split_data_2[10])
    ent9.insert(0,split_data_2[9])
    


query_buscar(id)

        
root.mainloop()


