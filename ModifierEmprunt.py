from tkinter import *
from subprocess import call
import mysql.connector
from tkinter import Tk,ttk
from tkinter import messagebox

root = Tk()
root.title("Modifier Emprunte")
root.geometry('600x400')
db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
mycursor = db.cursor()

labelId = Label(root, text="Chercher par Reference_Exemplaire")
labelId.pack()
def combo_input():
    cursor = db.cursor()
    cursor.execute('SELECT referance_E FROM emprunte')
    data = []
    for row in cursor.fetchall():
        data.append(row[0])
    return data
ref = ttk.Combobox()
ref.pack()
ref['values'] = combo_input()
ref['state'] = 'readonly'

labelNom = Label(root, text="Chercher par Id_adherent")
labelNom.pack()
def combo_input():
    cursor = db.cursor()
    cursor.execute('SELECT Id_Adh FROM emprunte')
    data = []
    for row in cursor.fetchall():
        data.append(row[0])
    return data
id = ttk.Combobox()
id.pack()
id['values'] = combo_input()
id['state'] = 'readonly'

def sel():
    idd = ref.get()
    reff = id.get()
    prenom = inputPrenom.get()
    dn = inputDN.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    mycursor = db.cursor()
    mycursor.execute("SELECT date_Emp FROM emprunte WHERE Id_Adh=%s and referance_E=%s",
                     (reff,idd))
    data = mycursor.fetchall()
    inputPrenom.insert(0, data)

    mycursor.execute("SELECT dateRetour_Emp FROM emprunte WHERE Id_Adh=%s and referance_E=%s",
                     (reff,idd))
    data = mycursor.fetchall()
    inputDN.insert(1, data)

    ii = ref.get()
    reff = id.get()
    prenomm = inputPrenom.get()
    dnn = inputDN.get()

ButtonSelect = Button(root,text="Recherche",command=sel)
ButtonSelect.pack()

labelPrenom = Label(root, text="Date Emprunte")
labelPrenom.pack()
inputPrenom = Entry(root, width=50, borderwidth=5)
inputPrenom.pack()

labelDN = Label(root, text="Date retour emprunte")
labelDN.pack()
inputDN = Entry(root, width=50, borderwidth=5)
inputDN.pack()





def modif():
    reff = ref.get()
    ii = id.get()
    prenomm = inputPrenom.get()
    dnn = inputDN.get()

    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    cursor = db.cursor()
    # prepare query and data
    query = (" UPDATE emprunte SET referance_E = %s,Id_Adh = %s, date_Emp=%s, dateRetour_Emp=%s WHERE referance_E = %s and Id_Adh=%s ")
    data = (reff,ii,prenomm,dnn,reff,ii)

    try:
        # update book title
        cursor.execute(query, data)
        messagebox.showinfo("ok","ligne est modifier")
        # accept the changes
        db.commit()

    except Exception as error:
        messagebox.showerror("error",error)
        db.rollback()



ButtonUpdate = Button(root,text="Modifier",command=modif)
ButtonUpdate.pack()

def back():
    root.destroy()
    call(["python", "menu.py"])


buttonBack = Button(root, text="Back", command=back)
buttonBack.pack()

root.mainloop()