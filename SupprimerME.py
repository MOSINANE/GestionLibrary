import tkinter
from tkinter import *
from subprocess import call
import mysql.connector
from tkinter import  ttk
from tkinter import messagebox

root = Tk()
root.title("Supprimer maison edition")
root.geometry('600x400')

labelAff = Label(root,text="Id ME")
labelAff.pack()
inputAff = Entry(root,width=50,borderwidth=5)
inputAff.pack()

db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
mycursor = db.cursor()
mycursor.execute("SELECT * FROM maison_edition")

# Using treeview widget
trv = ttk.Treeview(root, selectmode='browse')
#trv.grid(row=1, column=1, padx=20, pady=20)
trv.pack()
# number of columns
trv["columns"] = ("1", "2", "3", "4", "5")
# Defining heading
trv['show'] = 'headings'
# width of columns and alignment
trv.column("1", width=30, anchor='c')
trv.column("2", width=80, anchor='c')
trv.column("3", width=80, anchor='c')
trv.column("4", width=80, anchor='c')
trv.column("5", width=80, anchor='c')


# Headings
# respective columns
trv.heading("1", text="Id_ME")
trv.heading("2", text="Nom_ME")
trv.heading("3", text="Adresse_ME")
trv.heading("4", text="Tele_ME")
trv.heading("5", text="Email_ME")


r_set = mycursor.fetchall()
# getting data from MySQL student table
if r_set is None:
    messagebox.showerror("error","error")
else:
    for dt in r_set:
        trv.insert(parent="", index='end', iid=dt[0], text=dt[0],
                   values=(dt[0], dt[1], dt[2], dt[3], dt[4]))

def rech_id():
    id = inputAff.get()
    cr = db.cursor()
    cr.execute("SELECT * FROM maison_edition where Id_ME=%s",(id,))
    data= cr.fetchall()
    for i in trv.get_children():
        trv.delete(i)
    for dt in data:
        trv.insert(parent="", index='end', iid=dt[0], text=dt[0],
                   values=(dt[0], dt[1], dt[2], dt[3], dt[4]))

my_str=tkinter.StringVar()
def removeRecord():
    selected = trv.selection()
    if selected:
        # a row is selected
        x = selected[0]
        trv.delete(x)
        # delete record from table
        sql = 'DELETE FROM maison_edition WHERE Id_ME = %s'
        mycursor.execute(sql, (x,))
        messagebox.showinfo("ok","ligne est supprimer")
        # assume mydb is the connection object of MySQL database
        db.commit()  # make sure to commit the change


ButtonAff = Button(root,text="Rechercher",command=rech_id)
ButtonSupp = Button(root,text="Supprimer",command=removeRecord)
ButtonAff.pack()
ButtonSupp.pack()
def back():
    root.destroy()
    call(["python","menu.py"])

buttonBack = Button(root,text="Back",command=back)
buttonBack.pack()
root.mainloop()