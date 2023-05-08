from tkinter import messagebox
import tkinter
import customtkinter as CTk
from PIL import Image
import os
import pymysql

CTk.set_appearance_mode("System")
CTk.set_default_color_theme("dark-blue")

app = CTk.CTk()
app.geometry("1920x1080")
app.config(bg="#242320")
app.title('Login')
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")


def login():
    if entry_username1.get() == '' or entry_password1 == '':
        messagebox.showwarning(title='Error', message='All fields should be filled.')
    else:
        try:
            con = pymysql.connect(host='localhost', user='Dorwai', password='Kt0_ProchitalTotL0x', database='usersinfo')
            cur = con.cursor()
            cur.execute('select * from users9 where username=%s and password1=%s', (entry_username1.get(),
                                                                                   entry_password1.get()))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror(title='Error', message='Username or password is invalid.')
            else:
                login_successed()
        except Exception as E:
            messagebox.showerror(title='Error', message=f'Error due to: {E}')


def register():
    if entry_username2.get() == '' or entry_password2.get() == '' or entry_password_confirm.get() == '':
        messagebox.showwarning(title='Error', message='All fields should be filled.')
    elif entry_password2.get() != entry_password_confirm.get():
        messagebox.showerror(title='Error', message='Passwords aren`t matching.')
    else:
        try:
            con = pymysql.connect(host='localhost', user='Dorwai', password='Kt0_ProchitalTotL0x',
                                  database='usersinfo')
            cur = con.cursor()
            cur.execute('select * from users9 where username=%s', entry_username2.get())
            row = cur.fetchone()
            if row != None:
                messagebox.showerror(title='Error', message='User already exists')
            else:
                cur.execute('insert into users9 (id, username, password1) values(%s,%s,%s)',
                            (0, entry_username2.get(), entry_password2.get()))
                con.commit()
                con.close()
                messagebox.showinfo(title='Registration status', message='Registration complete!')

        except Exception as E:
            messagebox.showerror(title='Error', message=f'Error due to: {E}')


def login_successed():
    app.destroy()
    import main


img1 = CTk.CTkImage(Image.open(os.path.join(image_path, "tempbglololo.jpg")), size=(1920, 1080))
l0 = CTk.CTkLabel(master=app, image=img1, text="")
l0.pack()

frame_login_screen = CTk.CTkLabel(master=app, width=320, height=360, corner_radius=15)
frame_login_screen.place(relx=0.45, rely=0.5, anchor=tkinter.E)

l1 = CTk.CTkLabel(master=frame_login_screen, text="Login into your account", font=('Century Gothic', 20))
l1.place(x=50, y=45)

entry_username1 = CTk.CTkEntry(master=frame_login_screen, width=220, placeholder_text="Username")
entry_username1.place(x=50, y=110)
entry_password1 = CTk.CTkEntry(master=frame_login_screen, width=220, placeholder_text="Password")
entry_password1.place(x=50, y=165)

login_button = CTk.CTkButton(master=frame_login_screen, width=220, text="Login", corner_radius=6, fg_color='green',
                             command=login)
login_button.place(x=50, y=290)

###
###

frame_register_screen = CTk.CTkLabel(master=app, width=320, height=360, corner_radius=15)
frame_register_screen.place(relx=0.55, rely=0.5, anchor=tkinter.W)
l2 = CTk.CTkLabel(master=frame_register_screen, text="Register your account", font=('Century Gothic', 20))
l2.place(x=50, y=45)
entry_username2 = CTk.CTkEntry(master=frame_register_screen, width=220, placeholder_text="Enter Username")
entry_username2.place(x=50, y=110)
entry_password2 = CTk.CTkEntry(master=frame_register_screen, width=220, placeholder_text="Enter Password")
entry_password2.place(x=50, y=165)
entry_password_confirm = CTk.CTkEntry(master=frame_register_screen, width=220,
                                      placeholder_text="Confirm Password")
entry_password_confirm.place(x=50, y=220)
register_button2 = CTk.CTkButton(master=frame_register_screen, width=220, text="Register", corner_radius=6,
                                 fg_color='blue', command=register)
register_button2.place(x=50, y=290)

app.mainloop()
