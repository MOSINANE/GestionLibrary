from tkinter import *
from subprocess import call
import mysql.connector
from tkinter import Tk,ttk
from tkinter import messagebox

root = Tk()
root.title("Modifier Livre")
root.geometry('600x400')
db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
mycursor = db.cursor()

labelId = Label(root, text="Chercher par Id_livre")
labelId.pack()
inputId = Entry(root,width=50,borderwidth=5)
inputId.pack()

def sel():
    idd = inputId.get()
    nom = inputNom.get()
    prenom = inputPrenom.get()
    dn = inputDN.get()
    adresse = aut.get()
    email = li.get()
    tel = me.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    mycursor = db.cursor()
    mycursor.execute("SELECT Titre_Livre FROM livre WHERE Id_Livre=%s",
                     (idd,))
    data = mycursor.fetchall()
    inputNom.insert(0, data)
    mycursor.execute("SELECT Annee_Livre FROM livre WHERE Id_Livre=%s",
                     (idd,))
    data = mycursor.fetchall()
    inputPrenom.insert(1, data)
    mycursor.execute("SELECT Resume_Livre FROM livre WHERE Id_Livre=%s",
                     (idd,))
    data = mycursor.fetchall()
    inputDN.insert(2, data)
    mycursor.execute("SELECT Id_Ed FROM livre WHERE Id_Livre=%s",
                     (idd,))
    data = mycursor.fetchall()
    li.insert(3, data)
    me.set(data)
    mycursor.execute("SELECT Id_Type FROM livre WHERE Id_Livre=%s",
                     (idd,))
    data = mycursor.fetchall()
    me.insert(4, data)
    li.set(data)
    mycursor.execute("SELECT Id_Auteur FROM livre WHERE Id_Livre=%s",
                     (idd,))
    data = mycursor.fetchall()
    li.insert(5, data)
    aut.set(data)
    ii = inputId.get()
    nomm = inputNom.get()
    prenomm = inputPrenom.get()
    dnn = inputDN.get()
    adressee = aut.get()
    emaill = li.get()
    tele = me.get()

ButtonSelect = Button(root,text="Recherche",command=sel)
ButtonSelect.pack()


labelNom = Label(root, text="Titre livre")
labelNom.pack()
inputNom = Entry(root, width=50, borderwidth=5)
inputNom.pack()


labelPrenom = Label(root, text="Annee livre")
labelPrenom.pack()
inputPrenom = Entry(root, width=50, borderwidth=5)
inputPrenom.pack()

labelDN = Label(root, text="Resume livre")
labelDN.pack()
inputDN = Entry(root, width=50, borderwidth=5)
inputDN.pack()

labelTele = Label(root, text="Id ME")
labelTele.pack()
def combo_input():
    cursor = db.cursor()
    cursor.execute('SELECT Id_Ed FROM livre')
    data = []
    for row in cursor.fetchall():
        data.append(row[0])
    return data
me = ttk.Combobox()
me.pack()
me['values'] = combo_input()
me['state'] = 'readonly'


labelEmail = Label(root, text="Id Type")
labelEmail.pack()
def combo_input():
    cursor = db.cursor()
    cursor.execute('SELECT Id_Type FROM livre')
    data = []
    for row in cursor.fetchall():
        data.append(row[0])
    return data
li = ttk.Combobox()
li.pack()
li['values'] = combo_input()
li['state'] = 'readonly'


labelAdresse = Label(root, text="Id Auteur")
labelAdresse.pack()

def combo_input():
    cursor = db.cursor()
    cursor.execute('SELECT Id_Auteur FROM livre')
    data = []
    for row in cursor.fetchall():
        data.append(row[0])
    return data
aut = ttk.Combobox()
aut.pack()
aut['values'] = combo_input()
aut['state'] = 'readonly'







def modif():
    ii = inputId.get()
    nomm = inputNom.get()
    prenomm = inputPrenom.get()
    dnn = inputDN.get()
    adressee = aut.get()
    emaill = li.get()
    tele = me.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    cursor = db.cursor()
    # prepare query and data
    query = (" UPDATE livre SET Titre_Livre = %s, Annee_Livre=%s,Resume_Livre=%s,Id_Ed=%s,Id_Type=%s,Id_Auteur=%s WHERE Id_Livre = %s ")
    data = (nomm, prenomm,dnn,adressee,emaill,tele,ii)

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