from tkinter import *
from subprocess import call

import customtkinter
import mysql.connector
from tkinter import  ttk
from tkinter import messagebox

from PIL import ImageTk,Image

root = Tk()
root.title("Afficher livre")
root.geometry('1166x718')
root.resizable(0, 0)

bg_frame = Image.open('images\\background1.png')
photo = ImageTk.PhotoImage(bg_frame)
bg_panel = Label(root, image=photo)
bg_panel.image = photo
bg_panel.pack(fill='both', expand='yes')

lgn_frame = Frame(root, bg='Black', width=950, height=650)
lgn_frame.place(x=100, y=35)

labelAff = customtkinter.CTkLabel(root,text="Chercher par Id livre",width=120,height=25, bg_color='black')
labelAff.place(x=250,y=125)
inputAff = Entry(root,width=50,borderwidth=5)
inputAff.place(x=420,y=120)

def rech_id():
    id = inputAff.get()
    cr = db.cursor()
    cr.execute("SELECT * FROM livre where Id_Livre=%s",(id,))
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
                                 text="Rechercher",
                                 command=rech_id,
                                 fg_color="grey",
                                 text_color="white"
                                 )
ButtonAff.place(x=830,y=120)


db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
mycursor = db.cursor()
mycursor.execute("SELECT * FROM livre")

# Using treeview widget
trv = ttk.Treeview(root, selectmode='browse')
#trv.grid(row=1, column=1, padx=20, pady=20)
trv.place(x=150,y=230)
# number of columns
trv["columns"] = ("1", "2", "3", "4", "5", "6","7")
# Defining heading
trv['show'] = 'headings'
# width of columns and alignment
trv.column("1", width=50, anchor='c')
trv.column("2", width=100, anchor='c')
trv.column("3", width=100, anchor='c')
trv.column("4", width=200, anchor='c')
trv.column("5", width=150, anchor='c')
trv.column("6", width=150, anchor='c')
trv.column("7", width=100, anchor='c')

# Headings
# respective columns
trv.heading("1", text="Id_Livre")
trv.heading("2", text="Titre_Livre")
trv.heading("3", text="Annee_Livre")
trv.heading("4", text="Resume_Livre")
trv.heading("5", text="Id_Ed")
trv.heading("6", text="Id_Type")
trv.heading("7", text="Id_Auteur")


r_set = mycursor.fetchall()
# getting data from MySQL student table
if r_set is None:
    messagebox.showerror("error","error")
else:
    for dt in r_set:
        trv.insert(parent="", index='end', iid=dt[0], text=dt[0],
                   values=(dt[0], dt[1], dt[2], dt[3], dt[4],dt[5],dt[6]))


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
buttonBack.place(x=300,y=500)
root.mainloop()