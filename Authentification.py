from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox
from subprocess import call

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
      #  self.window.state('zoomed')
        self.window.title('Authentification')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "BIENVENUE"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============================Utilisateur====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Utilisateur", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"))
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)
        # ===== Username icon =========
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # ========= get ==================================================================
        def login_cnx():
            username = self.username_entry.get()
            password = self.password_entry.get()
            db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
            mycursor = db.cursor()
            sql = "select Nom_Admin, Mdp_Admin from admins where Nom_Admin=%s and Mdp_Admin=%s"
            val = (username, password)
            mycursor.execute(sql, val)
            result = mycursor.fetchone()
            if result:
                self.window.destroy()
                call(["python", "menu.py"])
            elif username == "" and password == "":
                messagebox.showerror("Erreur", "les cases sont vide")
            elif username == "":
                messagebox.showerror("Erreur", "Case utilisateur est vide")
            elif password == "":
                messagebox.showerror("Erreur", "Case mot de passe est vide")
            else:
                messagebox.showinfo("Erreur", "vous n'??tes pas admin")
        # ========================================================================
        # ============================Connect button================================
        # ========================================================================
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='CONNECTER', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=login_cnx)
        self.login.place(x=20, y=10)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Mot de passe", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*")
        self.password_entry.place(x=580, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)
        # ======== Password icon ================
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)

        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')


def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()






















'''from tkinter import *
from tkinter import messagebox
from subprocess import call
import mysql.connector
from tkinter import ttk

root = Tk()
root.title("Authentification")
root.geometry('600x400')

#connection ?? la base donnee
#db = mysql.connector.connect(host ="localhost",user ="root",password ="",db ="biblio")

#tester la connection
if db:
    mylabel = Label(root,text="connection est reussit")
    mylabel.pack()

labelUser=Label(root,text="Utilisateur")
inputUser=Entry(root,width=50, borderwidth=5)
labelUser.pack()
inputUser.pack()

labelPass=Label(root,text="Mot de passe")
inputPass=Entry(root,width=50, borderwidth=5, show="*")
labelPass.pack()
inputPass.pack()

def login_cnx():
    username = inputUser.get()
    password = inputPass.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", db="biblio")
    mycursor = db.cursor()
    sql = "select Nom_Admin, Mdp_Admin from admins where Nom_Admin=%s and Mdp_Admin=%s"
    val = (username, password)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    if result:
        root.destroy()
        call(["python","menu.py"])
    elif username == "" and password == "":
        messagebox.showerror("Erreur", "les cases sont vide")
    elif username == "":
        messagebox.showerror("Erreur","Case utilisateur est vide")
    elif password == "":
        messagebox.showerror("Erreur", "Case mot de passe est vide")
    else:
        messagebox.showinfo("Erreur","vous n'??tes pas admin")

loginButton=Button(root,text="Connecter",command=login_cnx,bg="Green", fg="White")
loginButton.pack()

root.mainloop()'''