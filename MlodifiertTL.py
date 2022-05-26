from tkinter import *
from subprocess import call

import customtkinter
import mysql.connector
from tkinter import Tk,ttk
from tkinter import messagebox

from PIL import ImageTk,Image

root = Tk()
root.title("Modifier Type livre")
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

labelId = customtkinter.CTkLabel(root,text="Chercher par Id type livre",width=120,height=25, bg_color='black')
labelId.place(x=250,y=250)
inputId = Entry(root,width=50,borderwidth=5)
inputId.place(x=450,y=250)

def sel():
    idd = inputId.get()
    nom = inputNom.get()

    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    mycursor = db.cursor()

    mycursor.execute("SELECT Libelle_Type FROM type_livre WHERE Id_Type=%s",
                     (idd,))
    data = mycursor.fetchall()
    inputNom.insert(0, data)
    ii = inputId.get()
    nomm = inputNom.get()

ButtonSelect = customtkinter.CTkButton(root,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 text="Chercher",
                                 command=sel,
                                 fg_color="grey",
                                 text_color="white"
                                 )
ButtonSelect.place(x=830,y=250)

labelNom = customtkinter.CTkLabel(root,text="Libelle type livre",width=120,height=25, bg_color='black')
labelNom.place(x=250,y=300)
inputNom = Entry(root, width=50, borderwidth=5)
inputNom.place(x=450,y=300)



def modif():
    ii = inputId.get()
    nomm = inputNom.get()

    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    cursor = db.cursor()
    # prepare query and data
    query = (" UPDATE type_livre SET Libelle_Type = %s WHERE Id_Type = %s ")
    data = (nomm,ii)

    try:
        # update book title
        cursor.execute(query, data)
        messagebox.showinfo("ok","ligne est modifier")
        # accept the changes
        db.commit()

    except Exception as error:
        messagebox.showerror("error","error")
        db.rollback()



ButtonUpdate = customtkinter.CTkButton(root,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 text="Modifier",
                                 command=modif,
                                 fg_color="grey",
                                 text_color="white"
                                 )
ButtonUpdate.place(x=300,y=400)

def back():
    root.destroy()
    call(["python", "menu.py"])


buttonBack = customtkinter.CTkButton(root,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 text="back",
                                 command=back,
                                 fg_color="grey",
                                 text_color="white"
                                 )
buttonBack.place(x=500,y=400)

root.mainloop()