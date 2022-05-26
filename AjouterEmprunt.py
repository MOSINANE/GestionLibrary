from tkinter import *
from subprocess import call
import mysql.connector
from tkinter import messagebox
from tkinter import ttk,Tk
import time
import datetime
root = Tk()
root.title("Ajouter Emprunt")
root.geometry('600x400')

db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")

labelId = Label(root,text="Reference exempalaire")
labelId.pack()
def combo_input():
    cursor = db.cursor()
    cursor.execute('SELECT referance_E FROM exemplaire')
    data = []
    for row in cursor.fetchall():
        data.append(row[0])

    return data
me = ttk.Combobox()
me.pack()
me['values'] = combo_input()
me['state'] = 'readonly'


labelNom = Label(root,text="Id Adherent")
labelNom.pack()
def combo_input():
    cursor = db.cursor()
    cursor.execute('SELECT Id_Adh FROM adherent')
    data = []
    for row in cursor.fetchall():
        data.append(row[0])

    return data
meo = ttk.Combobox()
meo.pack()
meo['values'] = combo_input()
meo['state'] = 'readonly'


labelPrenom = Label(root,text="Date Emprunt")
labelPrenom.pack()
inputPrenom = Entry(root,width=50, borderwidth=5)
inputPrenom.pack()


labelDN = Label(root,text="Date retour emprunt")
labelDN.pack()
inputDN = Entry(root,width=50, borderwidth=5)
inputDN.pack()



def insertAdh():
    r = me.get()
    mm = meo.get()
    p = inputPrenom.get()
    dn = inputDN.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    mycursor = db.cursor()
    mySql_insert_query= ("INSERT INTO emprunte(referance_E,Id_Adh,date_Emp,dateRetour_Emp) VALUES(%s,%s,%s,%s)")
    record = (r,mm,p,dn)
    try:
        mycursor.execute(mySql_insert_query,record)
        db.commit
        messagebox.showinfo("Ok","Ligne ajoute")
    except Exception as e:
        db.rollback()
        messagebox.showerror(e)
ButtonInsert = Button(root,text="Ajouter", command=insertAdh)
ButtonInsert.pack()


def back():
    root.destroy()
    call(["python","menu.py"])

buttonBack = Button(root,text="Back",command=back)
buttonBack.pack()
root.mainloop()