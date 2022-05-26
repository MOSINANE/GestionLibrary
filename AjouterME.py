from tkinter import *
from subprocess import call
import mysql.connector
from tkinter import messagebox
import time
import datetime
root = Tk()
root.title("Ajouter Maison Edition")
root.geometry('600x400')


labelId = Label(root,text="Id ME")
labelId.pack()
inputId = Entry(root,width=50, borderwidth=5)
inputId.pack()


labelNom = Label(root,text="Nom ME")
labelNom.pack()
inputNom = Entry(root,width=50, borderwidth=5)
inputNom.pack()


labelPrenom = Label(root,text="Adresse ME")
labelPrenom.pack()
inputPrenom = Entry(root,width=50, borderwidth=5)
inputPrenom.pack()


labelDN = Label(root,text="Email ME")
labelDN.pack()
inputDN = Entry(root,width=50, borderwidth=5)
inputDN.pack()


labelAdresse = Label(root,text="Tele ME")
labelAdresse.pack()
inputAdresse = Entry(root,width=50, borderwidth=5)
inputAdresse.pack()




def insertAdh():
    i = inputId.get()
    n = inputNom.get()
    p = inputPrenom.get()
    dn = inputDN.get()
    ad = inputAdresse.get()

    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    mycursor = db.cursor()

    mySql_insert_query= ("INSERT INTO maison_edition(Id_ME,Nom_ME,Adresse_ME,Email_ME,Tele_ME) VALUES(%s,%s,%s,%s,%s)")
    record = (i,n,p,dn,ad)
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