from tkinter import *
from subprocess import call
import mysql.connector
from tkinter import Tk,ttk
from tkinter import messagebox

root = Tk()
root.title("Modifier maison edition")
root.geometry('600x400')
db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
mycursor = db.cursor()

labelId = Label(root, text="Chercher par Id Maison edition")
labelId.pack()
inputId = Entry(root,width=50,borderwidth=5)
inputId.pack()

def sel():
    idd = inputId.get()
    nom = inputNom.get()
    prenom = inputPrenom.get()
    dn = inputDN.get()
    adresse = inputAdresse.get()

    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    mycursor = db.cursor()
    mycursor.execute("SELECT Nom_ME FROM maison_edition WHERE Id_ME=%s",
                     (idd,))
    data = mycursor.fetchall()
    inputNom.insert(0, data)
    mycursor.execute("SELECT Adresse_ME FROM maison_edition WHERE Id_ME=%s",
                     (idd,))
    data = mycursor.fetchall()
    inputPrenom.insert(1, data)
    mycursor.execute("SELECT Tele_ME FROM maison_edition WHERE Id_ME=%s",
                     (idd,))
    data = mycursor.fetchall()
    inputDN.insert(2, data)
    mycursor.execute("SELECT Email_ME FROM maison_edition WHERE Id_ME=%s",
                     (idd,))
    data = mycursor.fetchall()
    inputAdresse.insert(3, data)

    ii = inputId.get()
    nomm = inputNom.get()
    prenomm = inputPrenom.get()
    dnn = inputDN.get()
    adressee = inputAdresse.get()


ButtonSelect = Button(root,text="Recherche",command=sel)
ButtonSelect.pack()


labelNom = Label(root, text="Nom ME")
labelNom.pack()
inputNom = Entry(root, width=50, borderwidth=5)
inputNom.pack()


labelPrenom = Label(root, text="Adresse ME")
labelPrenom.pack()
inputPrenom = Entry(root, width=50, borderwidth=5)
inputPrenom.pack()

labelDN = Label(root, text="Tele ME")
labelDN.pack()
inputDN = Entry(root, width=50, borderwidth=5)
inputDN.pack()

labelAdresse = Label(root, text="Email ME")
labelAdresse.pack()
inputAdresse = Entry(root, width=50, borderwidth=5)
inputAdresse.pack()





def modif():
    ii = inputId.get()
    nomm = inputNom.get()
    prenomm = inputPrenom.get()
    dnn = inputDN.get()
    adressee = inputAdresse.get()


    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    cursor = db.cursor()
    # prepare query and data
    query = (" UPDATE maison_edition SET Nom_ME = %s, Adresse_ME=%s,Tele_ME=%s,Email_ME=%s WHERE Id_ME = %s ")
    data = (nomm, prenomm,dnn,adressee,ii)

    try:
        # update book title
        cursor.execute(query, data)
        messagebox.showinfo("ok","ligne est modifier")
        # accept the changes
        db.commit()

    except Exception as error:
        messagebox.showerror("error","error")
        db.rollback()


ButtonUpdate = Button(root,text="Modifier",command=modif)
ButtonUpdate.pack()

def back():
    root.destroy()
    call(["python", "menu.py"])


buttonBack = Button(root, text="Back", command=back)
buttonBack.pack()

root.mainloop()