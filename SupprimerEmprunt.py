import tkinter
from tkinter import *
from subprocess import call
import mysql.connector
from tkinter import  ttk
from tkinter import messagebox

root = Tk()
root.title("Supprimer Emprunte")
root.geometry('600x400')

labelAff = Label(root,text="Chercher par Reference Exemplaire")
labelAff.pack()
def combo_input():
    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")

    cursor = db.cursor()
    cursor.execute('SELECT referance_E FROM exemplaire')
    data = []
    for row in cursor.fetchall():
        data.append(row[0])
    return data
ref = ttk.Combobox()
ref.pack()
ref['values'] = combo_input()
ref['state'] = 'readonly'

labelAff = Label(root,text="Chercher par Id Adherent")
labelAff.pack()
def combo_input():
    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    cursor = db.cursor()
    cursor.execute('SELECT Id_Adh FROM adherent')
    data = []
    for row in cursor.fetchall():
        data.append(row[0])

    return data
id = ttk.Combobox()
id.pack()
id['values'] = combo_input()
id['state'] = 'readonly'

def rech_id():
    reff = ref.get()
    idd = id.get()
    cr = db.cursor()
    cr.execute("SELECT * FROM emprunte where referance_E=%s and Id_Adh = %s",(reff,idd))
    data= cr.fetchall()
    for i in trv.get_children():
        trv.delete(i)
    for dt in data:
        trv.insert(parent="", index='end', iid=dt[0], text=dt[0],
                   values=(dt[0], dt[1], dt[2], dt[3]))

ButtonAff = Button(root,text="Rechercher",command=rech_id)
ButtonAff.pack()


'''labelPrenom = Label(root, text="Date Emprunte")
labelPrenom.pack()
inputPrenom = Entry(root, width=50, borderwidth=5)
inputPrenom.pack()

labelDN = Label(root, text="Date retour emprunte")
labelDN.pack()
inputDN = Entry(root, width=50, borderwidth=5)
inputDN.pack()'''


db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
mycursor = db.cursor()
mycursor.execute("SELECT * FROM emprunte")

# Using treeview widget
trv = ttk.Treeview(root, selectmode='browse')
#trv.grid(row=1, column=1, padx=20, pady=20)
trv.pack()
# number of columns
trv["columns"] = ("1","2","3","4")
# Defining heading
trv['show'] = 'headings'
# width of columns and alignment
trv.column("1", width=30, anchor='c')
trv.column("2", width=30, anchor='c')
trv.column("3", width=30, anchor='c')
trv.column("4", width=30, anchor='c')


# Headings
# respective columns
trv.heading("1", text="Ref_exemplaire")
trv.heading("2", text="Id_Adherent")
trv.heading("3", text="Date_Emprunte")
trv.heading("4", text="Date_retour_emprunte")


r_set = mycursor.fetchall()
# getting data from MySQL student table
if r_set is None:
    messagebox.showerror("error","error")
else:
    for dt in r_set:
        trv.insert(parent="", index='end', iid=dt[0], text=dt[0],
                   values=(dt[0], dt[1], dt[2], dt[3]))


my_str=tkinter.StringVar()
def removeRecord():
    selected = trv.selection()
    if selected:
        # a row is selected
        x = selected[0]
        y = id.get()
        trv.delete(x)
        # delete record from table
        sql = 'DELETE FROM emprunte WHERE referance_E = %s and Id_Adh = %s'
        mycursor.execute(sql, (x,y))
        messagebox.showinfo("ok","ligne est supprimer")
        # assume mydb is the connection object of MySQL database
        db.commit()  # make sure to commit the change


ButtonSupp = Button(root,text="Supprimer",command=removeRecord)
ButtonSupp.pack()
def back():
    root.destroy()
    call(["python","menu.py"])

buttonBack = Button(root,text="Back",command=back)
buttonBack.pack()
root.mainloop()