from tkinter import *
from subprocess import call
import mysql.connector
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

import time
import datetime
root = tk.Tk()
root.title("Ajouter Livre")
root.geometry('600x400')



labelId = Label(root,text="Id livre")
labelId.pack()
inputId = Entry(root,width=50, borderwidth=5)
inputId.pack()


labelNom = Label(root,text="Titre livre")
labelNom.pack()
inputNom = Entry(root,width=50, borderwidth=5)
inputNom.pack()


labelPrenom = Label(root,text="Annee livre")
labelPrenom.pack()
inputPrenom = Entry(root,width=50, borderwidth=5)
inputPrenom.pack()


labelDN = Label(root,text="Resume livre")
labelDN.pack()
inputDN = Entry(root,width=50, borderwidth=5)
inputDN.pack()

labelIdME = Label(root,text="Id_ME ")
labelIdME.pack()
db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
def combo_input():
    cursor = db.cursor()
    cursor.execute('SELECT Id_ME FROM maison_edition')
    data = []
    for row in cursor.fetchall():
        data.append(row[0])
    return data
me = ttk.Combobox()
me.pack()
me['values'] = combo_input()
me['state'] = 'readonly'
labelIDTYPE = Label(root,text="Id_Type")
labelIDTYPE.pack()
def combo_input():
    cursor = db.cursor()
    cursor.execute('SELECT Id_Type FROM type_livre')
    data = []
    for row in cursor.fetchall():
        data.append(row[0])
    return data
ty = ttk.Combobox()
ty.pack()
ty['values'] = combo_input()
ty['state'] = 'readonly'
labelIDAUT = Label(root,text="Id_Aut")
labelIDAUT.pack()

def combo_input():
    cursor = db.cursor()
    cursor.execute('SELECT Id_Aut FROM auteur')
    data = []
    for row in cursor.fetchall():
        data.append(row[0])
    return data
aut = ttk.Combobox()
aut.pack()
aut['values'] = combo_input()
aut['state'] = 'readonly'

def insertAdh():
    i = inputId.get()
    n = inputNom.get()
    p = inputPrenom.get()
    dn = inputDN.get()
    idme = me.get()
    idtype = ty.get()
    idaut = aut.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    mycursor = db.cursor()
    mySql_insert_query= ("INSERT INTO livre(Id_Livre,Titre_Livre,Annee_Livre,Resume_Livre,Id_Ed,Id_Type,Id_Auteur) VALUES(%s,%s,%s,%s,%s,%s,%s)")
    record = (i,n,p,dn,idme,idtype,idaut)
    try:
        mycursor.execute(mySql_insert_query,record)
        db.commit
        messagebox.showinfo("Ok","Ligne ajoute")
    except Exception as e:
        db.rollback()
        messagebox.showerror("error",e)

ButtonInsert = Button(root,text="Ajouter", command=insertAdh)
ButtonInsert.pack()


#exec = mycursor.execute("INSERT INTO Adherent VALUES()")


def back():
    root.destroy()
    call(["python","menu.py"])

buttonBack = Button(root,text="Back",command=back)
buttonBack.pack()
root.mainloop()