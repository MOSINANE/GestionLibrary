from tkinter import *
from subprocess import call
import customtkinter
import mysql.connector
from tkinter import messagebox
import time
import datetime

from PIL import ImageTk,Image

root = Tk()
root.title("Ajouter Adherent")
root.geometry('1166x718')
root.resizable(0, 0)


bg_frame = Image.open('images\\background1.png')
photo = ImageTk.PhotoImage(bg_frame)
bg_panel = Label(root, image=photo)
bg_panel.image = photo
bg_panel.pack(fill='both', expand='yes')

lgn_frame = Frame(root, bg='#040405', width=950, height=650)
lgn_frame.place(x=100, y=35)


labelId = customtkinter.CTkLabel(root,text="Id Adherent",width=120,height=25, bg_color='black')
labelId.place(x=300,y=125)
inputId = Entry(root,width=50,borderwidth=5)
inputId.place(x=500,y=120)


labelNom = customtkinter.CTkLabel(root,text="Nom Adherent",width=120,height=25, bg_color='black')
labelNom.place(x=300,y=175)
inputNom = Entry(root,width=50,borderwidth=5)
inputNom.place(x=500,y=170)


labelPrenom = customtkinter.CTkLabel(root,text="Prenom Adherent",width=120,height=25, bg_color='black')
labelPrenom.place(x=300,y=230)
inputPrenom = Entry(root,width=50,borderwidth=5)
inputPrenom.place(x=500,y=225)


labelDN = customtkinter.CTkLabel(root,text="Date naissance Adherent",width=120,height=25, bg_color='black')
labelDN.place(x=300,y=285)
inputDN = Entry(root,width=50,borderwidth=5)
inputDN.place(x=500,y=280)


labelAdresse = customtkinter.CTkLabel(root,text="Adresse Adherent",width=120,height=25, bg_color='black')
labelAdresse.place(x=300,y=340)
inputAdresse = Entry(root,width=50,borderwidth=5)
inputAdresse.place(x=500,y=335)


labelEmail = customtkinter.CTkLabel(root,text="Email Adherent",width=120,height=25, bg_color='black')
labelEmail.place(x=300,y=395)
inputEmail = Entry(root,width=50,borderwidth=5)
inputEmail.place(x=500,y=390)


labelTele = customtkinter.CTkLabel(root,text="Telephone Adherent",width=120,height=25, bg_color='black')
labelTele.place(x=300,y=450)
inputTele = Entry(root,width=50,borderwidth=5)
inputTele.place(x=500,y=445)



def insertAdh():
    i = inputId.get()
    n = inputNom.get()
    p = inputPrenom.get()
    dn = inputDN.get()
    ad = inputAdresse.get()
    em = inputEmail.get()
    tel = inputTele.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    mycursor = db.cursor()
    mySql_insert_query= ("INSERT INTO adherent(Id_Adh,Nom_Adh,Prenom_Adh,DateNaissance_Adh,Adresse_Adh,Email_Adh,Tele_Adh) VALUES(%s,%s,%s,%s,%s,%s,%s)")
    record = (i,n,p,dn,ad,em,tel)
    try:
        mycursor.execute(mySql_insert_query,record)
        db.commit
        messagebox.showinfo("Ok","Adherent ajoute")
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
ButtonInsert.place(x=500,y=520)






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
buttonBack.place(x=700,y=520)
root.mainloop()