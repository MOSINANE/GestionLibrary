from tkinter import *
from subprocess import call

import customtkinter
import mysql.connector
from tkinter import messagebox
import time
import datetime

from PIL import ImageTk,Image

root = Tk()
root.title("Ajouter Type livre")
root.geometry('1166x718')
root.resizable(0, 0)

bg_frame = Image.open('images\\background1.png')
photo = ImageTk.PhotoImage(bg_frame)
bg_panel = Label(root, image=photo)
bg_panel.image = photo
bg_panel.pack(fill='both', expand='yes')

lgn_frame = Frame(root, bg='#040405', width=950, height=650)
lgn_frame.place(x=100, y=35)

labelId = customtkinter.CTkLabel(root,text="Id Type livre",width=120,height=25, bg_color='black')
labelId.place(x=300,y=200)
inputId = Entry(root,width=50, borderwidth=5)
inputId.place(x=500,y=200)


labelNom = customtkinter.CTkLabel(root,text="Libelle type livre",width=120,height=25, bg_color='black')
labelNom.place(x=300,y=275)
inputNom = Entry(root,width=50, borderwidth=5)
inputNom.place(x=500,y=275)




def insertAdh():
    i = inputId.get()
    n = inputNom.get()

    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    mycursor = db.cursor()
    mySql_insert_query= ("INSERT INTO type_livre(Id_Type,Libelle_Type) VALUES(%s,%s)")
    record = (i,n)
    try:
        mycursor.execute(mySql_insert_query,record)
        db.commit
        messagebox.showinfo("Ok","Ligne ajoute")
    except Exception as e:
        db.rollback()
        messagebox.showerror(e)
ButtonInsert = customtkinter.CTkButton(root,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 text="Ajouter",
                                 command=insertAdh,
                                 fg_color="grey",
                                 text_color="white"
                                 )
ButtonInsert.place(x=300,y=400)

#exec = mycursor.execute("INSERT INTO Adherent VALUES()")


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
buttonBack.place(x=500,y=400)
root.mainloop()