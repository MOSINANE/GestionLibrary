from tkinter import *
from subprocess import call
import mysql.connector
from tkinter import  ttk
from tkinter import messagebox
from PIL import ImageTk,Image

root = Tk()
root.title("Afficher Emprunte")
root.geometry('1166x718')
root.resizable(0, 0)

'''bg_frame = Image.open('images\\background1.png')
photo = ImageTk.PhotoImage(bg_frame)
bg_panel = Label(root, image=photo)
bg_panel.image = photo
bg_panel.pack(fill='both', expand='yes')

lgn_frame = Frame(root, bg='Black', width=950, height=650)
lgn_frame.place(x=100, y=35)'''


labelAff = Label(root,text="Reference Exemplaire")
labelAff.pack()
def combo_input():
    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")

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

labeladh = Label(root,text="Id Adherent")
labeladh.pack()
def combo_input():
    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")

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

db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
mycursor = db.cursor()
mycursor.execute("SELECT * FROM emprunte")

# Using treeview widget
trv = ttk.Treeview(root, selectmode='browse')
#trv.grid(row=1, column=1, padx=20, pady=20)
trv.pack()
# number of columns
trv["columns"] = ("1", "2", "3", "4")
# Defining heading
trv['show'] = 'headings'
# width of columns and alignment
trv.column("1", width=50, anchor='c')
trv.column("2", width=100, anchor='c')
trv.column("3", width=100, anchor='c')
trv.column("4", width=200, anchor='c')


# Headings
# respective columns
trv.heading("1", text="Ref_Exemplaire")
trv.heading("2", text="Id_Livre")
trv.heading("3", text="Date emprunte")
trv.heading("4", text="Date retour emprunte")

r_set = mycursor.fetchall()
# getting data from MySQL student table
if r_set is None:
    messagebox.showerror("error","error")
else:
    for dt in r_set:
        trv.insert(parent="", index='end', iid=dt[0], text=dt[0],
                   values=(dt[0], dt[1], dt[2], dt[3]))

def rech_id():
    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    id = me.get()
    ref = meo.get()
    cr = db.cursor()
    if ref == "":
        cr.execute("SELECT * FROM emprunte where referance_E=%s", (id,))
        data = cr.fetchall()
        for i in trv.get_children():
            trv.delete(i)
        for dt in data:
            trv.insert(parent="", index='end', iid=dt[0], text=dt[0],
                       values=(dt[0], dt[1], dt[2], dt[3]))

    elif id == "":
        cr.execute("SELECT * FROM emprunte where Id_Adh=%s",(ref,))
        data= cr.fetchall()
        for i in trv.get_children():
            trv.delete(i)
        for dt in data:
            trv.insert(parent="", index='end', iid=dt[0], text=dt[0],
                    values=(dt[0], dt[1], dt[2], dt[3]))
    else :
        cr.execute("SELECT * FROM emprunte where Id_Adh=%s and referance_E=%s", (ref,id,))
        data = cr.fetchall()
        for i in trv.get_children():
            trv.delete(i)
        for dt in data:
            trv.insert(parent="", index='end', iid=dt[0], text=dt[0],
                       values=(dt[0], dt[1], dt[2], dt[3]))

ButtonAff = Button(root,text="Rechercher",command=rech_id)
ButtonAff.pack()
def back():
    root.destroy()
    call(["python","menu.py"])

buttonBack = Button(root,text="Back",command=back)
buttonBack.pack()
root.mainloop()