# -*- coding: utf-8 -*-


import sqlite3

connection = sqlite3.connect("myTable.db")

crsr = connection.cursor()

sql_command = """CREATE TABLE emp ( 
id INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE);"""
 
# execute the statement
crsr.execute(sql_command)
 
# SQL command to insert the data in the table
sql_command = """INSERT INTO emp VALUES (01, "Bharadwaj", "Bulusu", "M", "1990-01-19");"""
crsr.execute(sql_command)

