from tkinter import *
from subprocess import call
import mysql.connector
from tkinter import Tk,ttk
from tkinter import messagebox

root = Tk()
root.title("Modifier Exemplaire")
root.geometry('600x400')
db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
mycursor = db.cursor()

labelId = Label(root, text="Chercher par Reference exemplaire")
labelId.pack()
inputId = Entry(root,width=50,borderwidth=5)
inputId.pack()
def sel():
    ii = inputId.get()
    idliv = me.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    mycursor = db.cursor()
    mycursor.execute("SELECT Id_Livre FROM exemplaire WHERE referance_E=%s",
                     (ii,))
    data = mycursor.fetchall()
    me.insert(1, data)

    i = inputId.get()
    nomm = me.get()
    me.set(data)


ButtonSelect = Button(root,text="Recherche",command=sel)
ButtonSelect.pack()

labelIdLiv = Label(root, text="Id livre")
labelIdLiv.pack()
def combo_input():
    cursor = db.cursor()
    cursor.execute('SELECT Id_Livre FROM exemplaire')
    data = []
    for row in cursor.fetchall():
        data.append(row[0])
    return data


me = ttk.Combobox()
me.pack()
me['values'] = combo_input()
me['state'] = 'readonly'



def modif():
    i = inputId.get()
    nomm = me.get()

    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    cursor = db.cursor()
    # prepare query and data
    query = (" UPDATE exemplaire SET Id_Livre = %s WHERE referance_E = %s ")
    data = (nomm,i)

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