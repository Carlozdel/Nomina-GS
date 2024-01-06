import sqlite3
# import pandas as pd

connection =  sqlite3.connect('GS_DataBase')
cursorDB = connection.cursor()

cursorDB.execute("""UPDATE ALL_EMPLOYEES SET HOLIDAY = 'NO'""")
# cursorDB.execute("""DROP TABLE ALL_EMPLOYEES; """)
# cursorDB.execute("""ALTER TABLE ALL_EMPLOYEES ADD "HOLIDAY" Text""")

# cursorDB.execute("""CREATE TABLE ALL_EMPLOYEES (Ignition Text, "Cost Center" Text, "Full Name" TEXT, Shift TEXT, "HRS X SEM" TEXT, COMEDOR Text, MODIFIER TEXT, "MODIFIED DATE" TEXT, "CURRENT FW" TEXT, APPROVED TEXT,SUPERVISOR TEXT)""")
# cursorDB.execute("INSERT INTO ALL_EMPLOYEES  VALUES (	'10782147'	,	'8026'	,	'De Santiago Calzada, Xenia Mabel'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'MAURICIO FELIPE MATU'	)")

# ALL_EMPS = [

# (	'11018976'	,	'8026'	,	'Rodriguez Rodriguez, Jesus Alfonso'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'MAURICIO FELIPE MATU'	),
# (	'11057315'	,	'8026'	,	'Loya, Sarahi'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'MAURICIO FELIPE MATU'	)	,
# (	'10550321'	,	'9052'	,	'Contreras Garcia, Elsa Marisa'	,	'Full Time'	,	'45'	,	'0'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'JUAN CARLOS RAMIREZ'	)	,
# (	'10783493'	,	'8099'	,	'Lozano Vazquez, Miguel Angel'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'BRISA MARINA LOPEZ'	)	,
# (	'10551447'	,	'8113'	,	'Matu Becerra, Mauricio Felipe'	,	'Full Time'	,	'45'	,	'0'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'LAURA OLIVIA LUEVANO'	)	,
# (	'10555596'	,	'8236'	,	'Luevano Ortega, Laura Olivia'	,	'Full Time'	,	'45'	,	'0'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'OCTAVIO MARTINEZ'	)	,
# (	'10559486'	,	'8113'	,	'Cerna Perez, Oscar'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'MAURICIO FELIPE MATU'	)	,
# (	'10787407'	,	'8113'	,	'Gaytan Holguin, Omar Eduardo'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'JUAN CARLOS RAMIREZ'	)	,
# (	'10787648'	,	'8113'	,	'Spinola Flores, Antonio'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'MAURICIO FELIPE MATU'	)	,
# (	'10788081'	,	'8113'	,	'Lara Garcia, Ricardo'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'MAURICIO FELIPE MATU'	)	,
# (	'11019810'	,	'8113'	,	'Gardea Bretado, Claudia Lizeth'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'MAURICIO FELIPE MATU'	)	,
# (	'10559903'	,	'8236'	,	'Federico Munoz'	,	'Full Time'	,	'45'	,	'0'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'GASPAR ALBERTO QUINTANA'	)	,
# (	'10562851'	,	'8270'	,	'Salcedo Allard, Leonel Alfonso'	,	'Full Time'	,	'45'	,	'0'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'MAURICIO FELIPE MATU'	)	,
# (	'10561054'	,	'8236'	,	'Estrada Lopez, Armando'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'CARLOS LUIS DELGADO'	)	,
# (	'10565232'	,	'8099'	,	'Lopez Acosta, Brisa Marina'	,	'Full Time'	,	'45'	,	'0'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'VICTOR ALEJANDRO VENEGAS'	)	,
# (	'10775107'	,	'8236'	,	'Delgado Quezada, Carlos Luis'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'LAURA OLIVIA LUEVANO'	)	,
# (	'10772829'	,	'8236'	,	'Gaspar Quintana'	,	'Full Time'	,	'45'	,	'0'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'VICTOR ALEJANDRO VENEGAS'	)	,
# (	'10782230'	,	'9992'	,	'Paz Holguin, Sergio Alejandro'	,	'Full Time'	,	'45'	,	'0'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'BRISA MARINA LOPEZ'	)	,
# (	'10784395'	,	'8236'	,	'Hernandez Hernandez, Pablo'	,	'Full Time'	,	'45'	,	'0'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'CARLOS LUIS DELGADO'	)	,
# (	'10785227'	,	'8236'	,	'Mario Balderrama'	,	'Full Time'	,	'45'	,	'0'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'GASPAR ALBERTO QUINTANA'	)	,
# (	'10781730'	,	'8236'	,	'Avila, Mayco Erik'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'GASPAR ALBERTO QUINTANA'	)	,
# (	'10786396'	,	'8236'	,	'Daniela Martinez'	,	'Full Time'	,	'45'	,	'0'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'GASPAR ALBERTO QUINTANA'	)	,
# (	'10781731'	,	'8272'	,	'Segovia, Daniel Eduardo'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'BRISA MARINA LOPEZ'	)	,
# (	'11124173'	,	'8272'	,	'Ramos Salazar, Erick Jesus'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'BRISA MARINA LOPEZ'	)	,
# (	'10550711'	,	'8274'	,	'Garcia Roiz Paredes, Eduardo'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'LAURA OLIVIA LUEVANO'	)	,
# (	'10921362'	,	'8274'	,	'Patil, Amit Prakash'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'LAURA OLIVIA LUEVANO'	)	,
# (	'11018977'	,	'8236'	,	'Abrego Quezada, Javier Omar'	,	'Full Time'	,	'45'	,	'0'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'CARLOS LUIS DELGADO'	)	,
# (	'11185207'	,	'8274'	,	'Pinon Marin, Andres'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'LAURA OLIVIA LUEVANO'	)	,
# (	'11185208'	,	'8274'	,	'Grado Saenz, Gisela'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'LAURA OLIVIA LUEVANO'	)	,
# (	'11018463'	,	'8317'	,	'Reyna Cruz, Arely'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'MAURICIO FELIPE MATU'	)	,
# (	'11192743'	,	'8317'	,	'Franco Gamez, Victor David'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'MAURICIO FELIPE MATU'	)	,
# (	'11083043'	,	'8274'	,	'Hernandez Moriel, Liza Mayela'	,	'Full Time'	,	'45'	,	'0'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'LAURA OLIVIA LUEVANO'	)	,
# (	'10556780'	,	'9052'	,	'Ramirez Rodriguez, Juan Carlos'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'VICTOR ALEJANDRO VENEGAS'	)	,
# (	'10561105'	,	'9052'	,	'Cazares Montes, Hector Axel'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'JUAN CARLOS RAMIREZ'	)	,
# (	'10774487'	,	'9052'	,	'Silva Aguirre, Jose Luis'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'JUAN CARLOS RAMIREZ'	)	,
# (	'10787145'	,	'9052'	,	'Benitez Valdez, Sergio Omar'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'JUAN CARLOS RAMIREZ'	)	,
# (	'11187004'	,	'8099'	,	'Silva Molina, Gustavo'	,	'Full Time'	,	'45'	,	'0'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'BRISA MARINA LOPEZ'	)	,
# (	'11101423'	,	'9992'	,	'Carranza Zamora, Sergio Vladimir'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'BRISA MARINA LOPEZ'	)	,
# (	'11146124'	,	'9992'	,	'Gonzalez Ramos, Cesar Antonio'	,	'Full Time'	,	'45'	,	'103.74'	,	'CARLOS LUIS DELGADO'	,	'11/29/2023'	,	'P04W02'	,	'YES'	,	'BRISA MARINA LOPEZ'	)	


# ]

# cursorDB.executemany("INSERT INTO ALL_EMPLOYEES  VALUES (?,?,?,?,?,?,?,?,?,?,?)",ALL_EMPS)


connection.commit()
connection.close()

