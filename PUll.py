import sqlite3
# import pandas as pd

connection =  sqlite3.connect('GS_DataBase')
cursorDB = connection.cursor()


cursorDB.execute("""ALTER TABLE ALL_EMPLOYEES ADD "Approved" Text""")

# cursorDB.execute("""CREATE TABLE ALL_EMPLOYEES (Ignition INTEGER, "Cost Center" INTEGER, "Full Name" TEXT, Shift TEXT, "HRS X SEM" TEXT, COMEDOR INTEGER, MODIFIER TEXT, "MODIFIED DATE" TEXT, "CURRENT FW" TEXT, APPROVED TEXT,SUPERVISOR TEXT)""")
# cursorDB.execute("INSERT INTO ALL_EMPLOYEES  VALUES (10782147,8026,'XENIA MABEL DE SANTIAGO','FULL TIME',45,103.74,'cdelgad3','11/21/2023',FY24W4','FY24W3','')")

# ALL_EMPS = [

# (10921362,8274,'AMIT PATIL','FULL TIME',45,103.74),
# (11185207,8274,'ANDRES PINON','FULL TIME',45,103.74),
# (10787648,8113,'ANTONIO SPINOLA','FULL TIME',45,103.74),
# (11018463,8317,'ARELY REYNA','FULL TIME',45,0),
# (10561054,8236,'ARMANDO ESTRADA','FULL TIME',45,103.74),
# (10565232,9052,'BRISA MARINA LOPEZ','FULL TIME',45,103.74),
# (10775107,8236,'CARLOS LUIS DELGADO','PARTIAL TIME',42,0),
# (11146124,9052,'CESAR ANTONIO GONZALEZ','FULL TIME',45,103.74),
# (11019810,8113,'CLAUDIA LIZETH GARDEA','FULL TIME',45,0),
# (10781731,8272,'DANIEL EDUARDO SEGOVIA','FULL TIME',45,103.74),
# (10550711,8274,'EDUARDO GARCIA ROIZ','FULL TIME',45,103.74),
# (10550321,9052,'ELSA MARISA CONTRERAS','FULL TIME',45,103.74),
# (11124173,8272,'ERICK JESUS RAMOS','FULL TIME',45,103.74),
# (11185208,8274,'GISELA GRADO','FULL TIME',45,103.74),
# (11187004,8099,'GUSTAVO SILVA','FULL TIME',45,103.74),
# (10561105,9992,'HECTOR AXEL CAZARES','FULL TIME',45,103.74),
# (11018977,8236,'JAVIER OMAR ABREGO','FULL TIME',45,103.74),
# (11018976,8026,'JESUS ALFONSO RODRIGUEZ','FULL TIME',45,103.74),
# (11132942,9052,'JOSE EDUARDO ALMANZA','FULL TIME',45,103.74),
# (10774487,9992,'JOSE LUIS SILVA','FULL TIME',45,103.74),
# (10556780,9052,'JUAN CARLOS RAMIREZ','FULL TIME',45,103.74),
# (10555596,8236,'LAURA OLIVIA LUEVANO','FULL TIME',45,103.74),
# (10562851,8270,'LEONEL ALFONSO SALCEDO','FULL TIME',45,103.74),
# (11083043,8274,'LIZA MAYELA HERNANDEZ','FULL TIME',45,0),
# (10551447,8113,'MAURICIO FELIPE MATU','FULL TIME',45,103.74),
# (10783493,8099,'MIGUEL ANGEL LOZANO','FULL TIME',45,103.74),
# (10787407,8113,'OMAR EDUARDO GAYTAN','FULL TIME',45,103.74),
# (10559486,8113,'OSCAR CERNA','FULL TIME',45,103.74),
# (10784395,8236,'PABLO HERNANDEZ','FULL TIME',45,0),
# (10788081,8113,'RICARDO LARA','FULL TIME',45,103.74),
# (10551118,8113,'SAUL IBZAN ARRAZATE','FULL TIME',45,103.74),
# (10782230,9052,'SERGIO ALEJANDRO PAZ','FULL TIME',45,103.74),
# (10787145,8264,'SERGIO OMAR BENITEZ','FULL TIME',45,103.74),
# (11101423,9052,'SERGIO VLADIMIR CARRANZA','FULL TIME',45,103.74),

# ]

# cursorDB.executemany("INSERT INTO ALL_EMPLOYEES  VALUES (?,?,?,?,?,?)",ALL_EMPS)
# cursorDB.execute("SELECT * FROM ALL_EMPLOYEES")

connection.commit()
connection.close()
#modified_to_test
