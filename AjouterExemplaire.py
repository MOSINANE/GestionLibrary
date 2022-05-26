from tkinter import *
from subprocess import call
import mysql.connector
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import time
import datetime
root = Tk()
root.title("Ajouter Exemplaire")
root.geometry('600x400')

labelId = Label(root,text="Referance exemplaire")
labelId.pack()
inputId = Entry(root,width=50, borderwidth=5)
inputId.pack()


labelNom = Label(root,text="Id Livre")
labelNom.pack()
db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
def combo_input():
    cursor = db.cursor()
    cursor.execute('SELECT Id_Livre FROM livre')
    data = []
    for row in cursor.fetchall():
        data.append(row[0])

    return data
me = ttk.Combobox()
me.pack()
me['values'] = combo_input()
me['state'] = 'readonly'
#me.place(relx="0", rely="0")


def insertAdh():
    i = inputId.get()
    n = me.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    mycursor = db.cursor()
    mySql_insert_query= ("INSERT INTO exemplaire(referance_E,Id_Livre) VALUES(%s,%s)")
    record = (i,n)
    try:
        mycursor.execute(mySql_insert_query,record)
        db.commit
        messagebox.showinfo("Ok","Ligne ajoute")
    except Exception as e:
        db.rollback()
        messagebox.showerror(e)
ButtonInsert = Button(root,text="Ajouter", command=insertAdh)
ButtonInsert.pack()

#exec = mycursor.execute("INSERT INTO Adherent VALUES()")


def back():
    root.destroy()
    call(["python","menu.py"])

buttonBack = Button(root,text="Back",command=back)
buttonBack.pack()
root.mainloop()