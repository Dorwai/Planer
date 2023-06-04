from tkinter import messagebox
import tkinter
import customtkinter as CTk
from PIL import Image
import os
from pathlib import Path
import pymysql

CTk.set_appearance_mode("System")          # Далее я для всех вас буду обьяснять что значат какие-то куски кода, для лучшего понимания
CTk.set_default_color_theme("dark-blue")

app = CTk.CTk()
app.geometry("1280x720")
app.config(bg="#242320")
app.title('Login')

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"F:\proba\build\assets\frame0")


def login(): # Функция для входа в аккаунт
    if entry_username1.get() == '' or entry_password1 == '':
        messagebox.showwarning(title='Error', message='All fields should be filled.')
    else:
        try:
            con = pymysql.connect(host='localhost', user='Dorwai', password='Kt0_ProchitalTotL0x', database='usersinfo') # Подключение к серверу SQL
            cur = con.cursor()
            cur.execute('select * from users9 where username=%s and password1=%s', (entry_username1.get(), # Берет значения из вписанных ранее энтри...
                                                                                   entry_password1.get()))
            row = cur.fetchone()
            if row == None: # ...и проверяет есть ли такой акк в базе
                messagebox.showerror(title='Error', message='Username or password is invalid.')
            else:
                login_successed()
        except Exception as E: # вывод ошибки если что то пойдет не так, чтобы легче искать было, напишите если что то будет не работать - помогу
            messagebox.showerror(title='Error', message=f'Error due to: {E}')


def register(): # Функция регистрации
    if entry_username2.get() == '' or entry_password2.get() == '' or entry_password_confirm.get() == '':  # Проверка, что что-нибудь вообще записано в энитри
        messagebox.showwarning(title='Error', message='All fields should be filled.')
    elif entry_password2.get() != entry_password_confirm.get(): # Проверка на одинаковость пароля
        messagebox.showerror(title='Error', message='Passwords aren`t matching.')
    else:
        try:
            con = pymysql.connect(host='localhost', user='Dorwai', password='Kt0_ProchitalTotL0x', # Подключение к серверу
                                  database='usersinfo')
            cur = con.cursor()
            cur.execute('select * from users9 where username=%s', entry_username2.get()) # Эта команда смотрит на значение 'username', которые УЖЕ есть в базе данных...
            row = cur.fetchone()
            if row != None: # ...если такой есть, то выводится ошибка (некст строка)
                messagebox.showerror(title='Error', message='User already exists')
            else: # иначе создается новое значение в датабазе
                cur.execute('insert into users9 (id, username, password1) values(%s,%s,%s)', # здесь идут записи id, пароля и ника в базу
                            (0, entry_username2.get(), entry_password2.get()))
                con.commit()
                con.close()
                messagebox.showinfo(title='Registration status', message='Registration complete!')

        except Exception as E:
            messagebox.showerror(title='Error', message=f'Error due to: {E}')


def login_successed(): # Охренительная функция, выключает это окно и запускает само приложение, правда круто?)
    app.destroy()
    import gui


img1 = CTk.CTkImage(Image.open(os.path.join(ASSETS_PATH, "ris.jpg")), size=(1280, 720)) # Тут ничего впринципе интересного, просто создание окошек, лэйблов и тп,
l0 = CTk.CTkLabel(master=app, image=img1, text="")                                               # до следующих 'решеток' будет создание всего барахла для логина
l0.pack()

frame_login_screen = CTk.CTkFrame(master=app, width=320, height=360, corner_radius=15, fg_color="#D3E1D5")
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

frame_register_screen = CTk.CTkFrame(master=app, width=320, height=360, corner_radius=15, fg_color="#D3E1D5")
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