import tkinter
from tkinter import *
from subprocess import call

import customtkinter
import mysql.connector
from tkinter import  ttk
from tkinter import messagebox

from PIL import ImageTk,Image

root = Tk()
root.title("Supprimer Adherent")
root.geometry('1166x718')
root.resizable(0, 0)


bg_frame = Image.open('images\\background1.png')
photo = ImageTk.PhotoImage(bg_frame)
bg_panel = Label(root, image=photo)
bg_panel.image = photo
bg_panel.pack(fill='both', expand='yes')

lgn_frame = Frame(root, bg='#040405', width=950, height=650)
lgn_frame.place(x=100, y=35)


db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
mycursor = db.cursor()

labelAff = customtkinter.CTkLabel(root,text="Chercher par Id Adherent",width=120,height=25, bg_color='black')
labelAff.place(x=250,y=125)
inputAff = Entry(root,width=50,borderwidth=5)
inputAff.place(x=450,y=120)

def rech_id():
    id = inputAff.get()
    cr = db.cursor()
    cr.execute("SELECT * FROM adherent where Id_Adh=%s",(id,))
    data= cr.fetchall()
    for i in trv.get_children():
        trv.delete(i)
    for dt in data:
        trv.insert(parent="", index='end', iid=dt[0], text=dt[0],
                   values=(dt[0], dt[1], dt[2], dt[3], dt[4],dt[5],dt[6]))

ButtonAff = customtkinter.CTkButton(root,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 text="Chercher",
                                 command=rech_id,
                                 fg_color="grey",
                                 text_color="white"
                                 )
ButtonAff.place(x=780,y=120)

db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
mycursor = db.cursor()
mycursor.execute("SELECT * FROM adherent")

# Using treeview widget
trv = ttk.Treeview(root, selectmode='browse')
#trv.grid(padx=20, pady=20)
trv.place(x=225,y=190, width=700)
# number of columns
trv["columns"] = ("1", "2", "3", "4", "5", "6","7")
# Defining heading
trv['show'] = 'headings'
# width of columns and alignment
trv.column("1", width=30, anchor='c')
trv.column("2", width=80, anchor='c')
trv.column("3", width=80, anchor='c')
trv.column("4", width=80, anchor='c')
trv.column("5", width=80, anchor='c')
trv.column("6", width=80, anchor='c')
trv.column("7", width=80, anchor='c')

# Headings
# respective columns
trv.heading("1", text="Id_Adh")
trv.heading("2", text="Nom_Adh")
trv.heading("3", text="Prenom_Adh")
trv.heading("4", text="DateNaissance_Adh")
trv.heading("5", text="Adresse_Adh")
trv.heading("6", text="Email_Adh")
trv.heading("7", text="Tele_Adh")

r_set = mycursor.fetchall()
# getting data from MySQL student table
if r_set is None:
    messagebox.showerror("error","error")
else:
    for dt in r_set:
        trv.insert(parent="", index='end', iid=dt[0], text=dt[0],
                   values=(dt[0], dt[1], dt[2], dt[3], dt[4],dt[5],dt[6]))



my_str=tkinter.StringVar()
def removeRecord():
    selected = trv.selection()
    if selected:
        # a row is selected
        x = selected[0]
        trv.delete(x)
        # delete record from table
        sql = 'DELETE FROM adherent WHERE Id_Adh = %s'
        mycursor.execute(sql, (x,))
        messagebox.showinfo("ok","Adherent supprimer")
        # assume mydb is the connection object of MySQL database
        db.commit()  # make sure to commit the change


ButtonSupp = customtkinter.CTkButton(root,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 text="Supprimer",
                                 command=removeRecord,
                                 fg_color="grey",
                                 text_color="white"
                                 )
ButtonSupp.place(x=400,y=450, width=100)
def back():
    root.destroy()
    call(["python","menu.py"])

buttonBack = customtkinter.CTkButton(root,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 text="back",
                                 command=back,
                                 fg_color="grey",
                                 text_color="white"
                                 )
buttonBack.place(x=550,y=450, width=100)
root.mainloop()