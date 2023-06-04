import datetime
from calendar import Calendar
from pathlib import Path
import os
from tkinter import END
from tkinter.messagebox import askyesno, askokcancel, showinfo

import customtkinter
import customtkinter as CTk
from PIL import Image
from tkcalendar import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"F:\proba\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # задание параметров окна
        self.title("ПЛАНЕР")
        self.geometry("1280x720")

        self.navigation_frame = customtkinter.CTkFrame(
            master=self,
            width=340.0,
            height=720.0,
            fg_color="#77AB85",
            corner_radius=0
            )
        self.navigation_frame.place(x=0.0, y=0.0)

        self.month = customtkinter.CTkFrame(master=self, corner_radius=0,
                                            fg_color="#D8F8DF",
                                            height=720,
                                            width=940,
                                            )
        self.month.place(x=340,y=0)

        #лейбл
        self.image_1 = CTk.CTkImage(
            Image.open(os.path.join(ASSETS_PATH, "image_1.png")),size=(306,81))
        self.img1=CTk.CTkLabel(master=self.navigation_frame, image=self.image_1, text="", width=306, height=81, bg_color="#77AB85")
        self.img1.place(
            x=17.0,
            y=37.0,
        )

        #иконка пользователя
        self.image_2 = CTk.CTkImage(
            Image.open(os.path.join(ASSETS_PATH, "image_2.png")),size=(70,70))

        # картинка линии
        self.image_3 = CTk.CTkImage(
            Image.open(os.path.join(ASSETS_PATH, "image_3.png")),size=(857,1))

        # иконка выхода
        self.image_4 = CTk.CTkImage(
            Image.open(os.path.join(ASSETS_PATH, "image_4.png")),size=(40,40))

        # иконка календаря
        self.image_5 = CTk.CTkImage(
            Image.open(os.path.join(ASSETS_PATH, "image_5.png")),size=(40,40))

        # иконка месяца недели 3
        self.image_6 = CTk.CTkImage(
            Image.open(os.path.join(ASSETS_PATH, "image_6.png")),size=(40,40))

        # иконка конспектов
        self.image_7 = CTk.CTkImage(
            Image.open(os.path.join(ASSETS_PATH, "image_7.png")),size=(40,40))

        self.image_8 = CTk.CTkImage(
            Image.open(os.path.join(ASSETS_PATH, "arrow_1.png")), size=(24.52, 49))

        self.image_9 = CTk.CTkImage(
            Image.open(os.path.join(ASSETS_PATH, "arrow_2.png")), size=(24.52, 49))

        self.galka = CTk.CTkImage(
            Image.open(os.path.join(ASSETS_PATH, "galka.png")), size=(40, 40))

        self.Z1 = CTk.CTkLabel(master=self.month, width=918, height=569, text="",
                              bg_color="#F4F6F4", corner_radius=10, font=("Inter Bold", 20))
        self.Z1.place(
            x=11,
            y=136,
        )

        self.CalendarZ = CTk.CTkLabel(master=self.month, width=655, height=528, text="",
                               bg_color="#EBF0EB", corner_radius=10, font=("Century Gothic", 20))
        self.CalendarZ.place(
            x=262,
            y=159,
        )


        self.cal = Calendar(self.CalendarZ, selectmode="day", background='#BBDBC4', borderwidth=25, foreground='white',
                            font="Helvetica 35", width=655, height=528, headersbackground="#D3E1D5",
                            showweeknumbers=False, locale='ru', showothermonthdays=False, selectbackground="#D3E1D5",
                            weekendbackground="#E4F5E7")
        self.cal.place(x=5,y=70)

        # имя пользователя
        self.user_name=CTk.CTkTextbox(
            master=self.month,
            font=("Century Gothic", 20 * -1),
            width=100,
            height=40
        )
        self.user_name.insert("0.0","#USER2")
        self.user_name.place(x=812, y=60)

        self.scroll_ToDo = customtkinter.CTkScrollableFrame(self.month, width=185, height=381, fg_color='#EBF0EB',)
        self.scroll_ToDo.place(x=42, y=294)

        def add_todo():
            todo = self.entr.get()
            if todo == "":
                return
            self.Ttodo = customtkinter.CTkCheckBox(self.scroll_ToDo, text=todo,hover_color=("gray75", "gray25"),
                                                   fg_color="#6AAC74")
            self.Ttodo.grid(column=0, pady=5, sticky='w', padx=15)
            self.entr.delete(0, END)

        self.entr = CTk.CTkEntry(
            master=self.month,
            font=("Century Gothic", 20 * -1),
            width=175,
            height=26
        )
        self.entr.place(x=70, y=261)

        self.add_button = customtkinter.CTkButton(self.month,
                                                  text='+', command=add_todo,
                                                  width=27, height=27, fg_color="#D9D9D9",
                                                  text_color="#000000", corner_radius=5,
                                                  hover_color=("gray75", "gray25"))
        self.add_button.place(x=42, y=263)

        self.Z = CTk.CTkLabel(master=self.month, text="Задачи на ", width=200, height=79,
                                 bg_color="#BBDBC4", corner_radius=100, font=("Century Gothic",20))
        self.Z.place(
            x=42,
            y=175,
        )

        self.img2 = CTk.CTkLabel(master=self.month, image=self.image_2, text="", width=70, height=70,
                                 bg_color="#D8F8DF")
        self.img2.place(
            x=715.0,
            y=38.0,
        )

        self.img3 = CTk.CTkLabel(master=self.month, image=self.image_3, text="", width=857, height=1,
                                 bg_color="#D8F8DF")
        self.img3.place(
            x=41.5,
            y=121.5,
        )

        self.citate=CTk.CTkTextbox(
            master=self.month,
            font=("Century Gothic", 20 * -1),
            width=511,
            height=48
        )
        self.citate.insert("0.0","Treat your habits like your plants")
        self.citate.place(x=44, y=60)

        self.button_6 = CTk.CTkLabel(master=self.navigation_frame,
                                     width=340, height=80,
                                     text="Календарь",
                                     text_color="#F4F6F4",
                                     font=("Century Gothic", 32),
                                     )
        self.button_6.place(
            x=23, y=160
        )

        self.image_cal = CTk.CTkLabel(master=self.navigation_frame, height=80, image=self.image_5, text='')
        self.image_cal.place(x=65, y=160)

        self.month_b = CTk.CTkButton(
            master=self.navigation_frame,
            text="Месяц",
            corner_radius=0,
            image=self.image_7,
            hover_color=( "#578E63","#77AB85"),
            compound="left",
            fg_color="#77AB85",
            font=("Century Gothic", 32),
            command=self.month_b_event,
            width=355.0,
            height=80.0
        )
        self.month_b.place(
            x=0.0,
            y=240.0,
        )

        self.week_b = CTk.CTkButton(
            master=self.navigation_frame,
            text="Привычки",
            corner_radius=0,
            image=self.galka,
            compound="left",
            hover_color=( "#578E63","#77AB85"),
            border_spacing=0,
            fg_color="#77AB85",
            font=("Inter Light", 32),
            command=self.week_b_event,
            width=340.0,
            height=80.0
        )
        self.week_b.place(
            x=0.0,
            y=480.0,

        )


        self.days_b = CTk.CTkButton(
            master=self.navigation_frame,
            text="3 дня",
            corner_radius=0,
            image=self.image_7,
            hover_color=( "#578E63","#77AB85"),
            fg_color="#77AB85",
            font=("Inter Light", 32),
            command=self.days_b_event,
            width=340.0,
            height=80.0
        )
        self.days_b.place(
            x=0.0,
            y=320.0,

        )


        self.conspect_b = CTk.CTkButton(
            master=self.navigation_frame,
            text="Конспекты",
            corner_radius=0,
            image=self.image_6,
            hover_color=( "#578E63","#77AB85"),
            fg_color="#77AB85",
            font=("Inter Semi Bold", 32),
            width=340.0,
            command=self.conspect_b_event,
            height=80.0
        )
        self.conspect_b.place(
            x=0.0,
            y=400.0,

        )


        self.button_1 = CTk.CTkButton(
            master=self.navigation_frame,
            text="Выход",
            corner_radius=0,
            border_spacing=10,
            hover_color=( "#578E63","#77AB85"),
            fg_color="#77AB85",
            font=("Inter", 30),
            width=340.0,
            height=80.0,
            image=self.image_4
        )
        self.button_1.place(
            x=0.0,
            y=620.0,
        )

        #ТРЕКЕР ПРИВЫЧЕК
        self.trek = customtkinter.CTkFrame(master=self, corner_radius=0,
            fg_color = "#D8F8DF",
            height = 720,
            width = 940,
        )

        self.F = CTk.CTkLabel(master=self.trek, text="", width=928, height=713,
                               bg_color="#ECF3EC", font=('Inter', 40), text_color="white")
        self.F.place(
            x=7, y=7
        )

        self.text = CTk.CTkLabel(master=self.trek, text="Трекер привычек", width=846, height=30,
                              bg_color="#ECF3EC", font=('Inter', 30), )
        self.text.place(
            x=48, y=7
        )

        self.F1 = CTk.CTkLabel(master=self.trek, text="", width=853, height=671,
                              bg_color="#D3E1D5", font=('Inter', 20), text_color="white")
        self.F1.place(
            x=46, y=38
        )
        yy1=55
        for i in range(13):
            self.priv=CTk.CTkTextbox(master=self.trek, height=30, width=180)
            self.priv.place(x=57, y=yy1)
            yy1+=45


        xx=247
        yy=63
        for i in range (13):
            for j in range (25):
                self.ch = CTk.CTkCheckBox(master=self.trek, width=16, height=16, text="",
                                          hover_color=("gray75", "gray25"),
                                          fg_color="#6AAC74")
                self.ch.place(x=xx, y=yy)
                xx+=25
            xx=247
            yy += 45
        
        self.chistka=CTk.CTkButton(master=self.trek, hover_color=( "#578E63","#77AB85"),
            fg_color="#9BAAA5", text="Очистить",
            font=("Inter Semi Bold", 22),
            width=170.0,
            height=40.0 )
        self.chistka.place(x=60,y=653)

        self.sohr = CTk.CTkButton(master=self.trek, hover_color=("#578E63", "#77AB85"),
                                     fg_color="#9BAAA5", text="Сохранить",
                                     font=("Inter Semi Bold", 22),
                                     width=170.0,
                                     height=40.0)
        self.sohr.place(x=718, y=653)


        # 3 ДНЕВНЫЙ ФРЕЙМ
        self.days = customtkinter.CTkFrame(self, corner_radius=0,
                                           fg_color="#D8F8DF",
                                           height=720,
                                           width=940,
                                           )

        self.BGD = CTk.CTkLabel(master=self.days, text="", width=918, height=569,
                                 bg_color="#ECF3EC")
        self.BGD.place(
            x=11.0,
            y=136.0,
        )

        self.BGD2 = CTk.CTkLabel(master=self.days, text="", width=894, height=538,
                                bg_color="#F4F6F4")
        self.BGD2.place(
            x=23.0,
            y=152.0,
        )

        self.scroll_ToDo1 = customtkinter.CTkScrollableFrame(self.days, width=268, height=391, fg_color='#D3E1D5', )
        self.scroll_ToDo1.place(x=34, y=281)

        self.scroll_ToDo2 = customtkinter.CTkScrollableFrame(self.days, width=268, height=391, fg_color='#D3E1D5', )
        self.scroll_ToDo2.place(x=326, y=281)

        self.scroll_ToDo3 = customtkinter.CTkScrollableFrame(self.days, width=268, height=391, fg_color='#D3E1D5', )
        self.scroll_ToDo3.place(x=618, y=281)

        def add_todo1():
            todo = self.entr1.get()
            if todo == "":
                return
            self.Ttodo = customtkinter.CTkCheckBox(self.scroll_ToDo1, text=todo, hover_color=("gray75", "gray25"),
                                                   fg_color="#6AAC74")
            self.Ttodo.grid(column=0, pady=5, sticky='w', padx=15)
            self.entr1.delete(0, END)

        def add_todo2():
            todo = self.entr2.get()
            if todo == "":
                return
            self.Ttodo = customtkinter.CTkCheckBox(self.scroll_ToDo2, text=todo, hover_color=("gray75", "gray25"),
                                                    fg_color="#6AAC74")
            self.Ttodo.grid(column=0, pady=5, sticky='w', padx=15)
            self.entr2.delete(0, END)

        def add_todo3():
            todo = self.entr3.get()
            if todo == "":
                return
            self.Ttodo = customtkinter.CTkCheckBox(self.scroll_ToDo3, text=todo, hover_color=("gray75", "gray25"),
                                                   fg_color="#6AAC74")
            self.Ttodo.grid(column=0, pady=5, sticky='w', padx=15)
            self.entr3.delete(0, END)


        self.add_button1 = customtkinter.CTkButton(self.days,
                                                  text='+', command=add_todo1,
                                                  width=36, height=36, fg_color="#D9D9D9",
                                                  text_color="#000000", corner_radius=5, font=('Inter',25),
                                                  hover_color=("gray75", "gray25"))
        self.add_button1.place(x=34, y=240)

        self.add_button2 = customtkinter.CTkButton(self.days,
                                                   text='+', command=add_todo2,
                                                   width=36, height=36, fg_color="#D9D9D9",
                                                   text_color="#000000", corner_radius=5, font=('Inter',25),
                                                   hover_color=("gray75", "gray25"))
        self.add_button2.place(x=326, y=240)

        self.add_button3 = customtkinter.CTkButton(self.days,
                                                  text='+', command=add_todo3,
                                                  width=36, height=36, fg_color="#D9D9D9",
                                                  text_color="#000000", corner_radius=5, font=('Inter',25),
                                                  hover_color=("gray75", "gray25"))
        self.add_button3.place(x=618, y=240)

        self.entr1 = CTk.CTkEntry(
            master=self.days,
            font=("Inter Regular", 20 * -1),
            width=240,
            height=36
        )
        self.entr1.place(x=73, y=240)

        self.entr2 = CTk.CTkEntry(
            master=self.days,
            font=("Inter Regular", 20 * -1),
            width=240,
            height=36
        )
        self.entr2.place(x=365, y=240)

        self.entr3 = CTk.CTkEntry(
            master=self.days,
            font=("Inter Regular", 20 * -1),
            width=240,
            height=36
        )
        self.entr3.place(x=657, y=240)

        d1 = datetime.date.today().strftime("%d.%m")
        self.D1 = CTk.CTkLabel(master=self.days, text=d1, width=285, height=56,
                                 bg_color="#A6C7AB", font=('Inter',40), text_color="white")
        self.D1.place(
            x=34, y=170
        )

        d2 = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d.%m")
        self.D2 = CTk.CTkLabel(master=self.days, text=d2, width=285, height=56,
                               bg_color="#A6C7AB", font=('Inter', 40), text_color="white")
        self.D2.place(
            x=326, y=170
        )

        d3 = (datetime.date.today() + datetime.timedelta(days=2)).strftime("%d.%m")
        self.D3 = CTk.CTkLabel(master=self.days, text=d3, width=285, height=56,
                               bg_color="#A6C7AB", font=('Inter', 40), text_color="white")
        self.D3.place(
            x=618, y=170
        )

        self.next_button1 = customtkinter.CTkButton(self.days,
                                                    text='', command=add_todo1,
                                                    width=24.52, height=49, fg_color="#D9D9D9",
                                                    text_color="#000000", corner_radius=5, font=('Inter', 25),
                                                    hover_color=("gray75", "gray25"), image=self.image_8)
        self.next_button1.place(x=10, y=170.0)


        self.next_button2 = customtkinter.CTkButton(self.days,
                                                    text='', command=add_todo1,
                                                    width=24.52, height=49, fg_color="#D9D9D9",
                                                    text_color="#000000", corner_radius=5, font=('Inter', 25),
                                                    hover_color=("gray75", "gray25"), image=self.image_9)
        self.next_button2.place(x=891, y=170.0)

        self.user_name = CTk.CTkTextbox(
            master=self.days,
            font=("IrishGrover Regular", 20 * -1),
            width=100,
            height=40
        )
        self.user_name.insert("0.0", "#USER2")
        self.user_name.place(x=812, y=60)

        self.img2 = CTk.CTkLabel(master=self.days, image=self.image_2, text="", width=70, height=70,
                                 bg_color="#D8F8DF")
        self.img2.place(
            x=715.0,
            y=38.0,
        )

        self.img3 = CTk.CTkLabel(master=self.days, image=self.image_3, text="", width=857, height=1,
                                 bg_color="#D8F8DF")
        self.img3.place(
            x=41.5,
            y=121.5,
        )

        self.citate = CTk.CTkTextbox(
            master=self.days,
            font=("IrishGrover Regular", 20 * -1),
            width=511,
            height=48
        )
        self.citate.insert("0.0", "Treat your habits like your plants")
        self.citate.place(x=44, y=60)

        # КОНСПЕКТНЫЙ ФРЕЙМ
        self.conspect = customtkinter.CTkFrame(self, corner_radius=0,
                                           fg_color="#D8F8DF",
                                           height=720,
                                           width=940,
                                           )

        self.rectengle1 = CTk.CTkLabel(master=self.conspect, text="",
                                       width=911,
                                       height=687,
                                       bg_color="#ECF3EC",
                                       )

        self.rectengle1.place(x=14, y=18)

        self.rectengle2 = CTk.CTkLabel(master=self.conspect, text="", width=885, height=650, bg_color="#F4F6F4", )
        self.rectengle2.place(x=27, y=37)

        self.rectengle3 = CTk.CTkFrame(master=self.conspect, width=859, height=574, fg_color="#D3E1D5", )
        self.rectengle3.place(x=41, y=90)

        self.text = CTk.CTkLabel(master=self.rectengle2,
                                 width=885,
                                 text="Конспекты",
                                 text_color="#000000",
                                 fg_color="#F4F6F4",
                                 font=("Inter Regular", 32 * -1),
                                 )
        self.text.place(x=0, y=10)
  
        # Функция, сделанная для того, чтобы окно добавления конспекта нельзя было "миновать"
        def dismiss(window):
            window.grab_release()
            window.destroy()

        # Функция добавления конспекта. Создается окно, которое создаёт конспект с названием, которое было написано пользователем
        def add_task():
            window = CTk.CTkToplevel()
            window.title('Добавить конспект')
            window.geometry('300x80')

            task_text = CTk.CTkEntry(window, width=250)
            task_text.pack(pady=5)

            window.protocol("WM_DELETE_WINDOW", lambda: dismiss(window))
            CTk.CTkButton(window, text='Добавить', font=('Times New Roman', 20),
                          fg_color="#77AB85", bg_color="#D3E1D5", hover_color=("#578E63", "#77AB85"),
                          command=lambda: [add(task_text.get()), dismiss(window)]).pack()
            window.grab_set()

        # первый фрейм, занимающий все окно, на нем располагаются конспекты
        mainframe = CTk.CTkScrollableFrame(self.rectengle3, width=839, height=574, fg_color="#D3E1D5", )
        mainframe.pack(fill="both", expand=True)
        # кнопка добавления конспекта
        btn_add_task = CTk.CTkButton(mainframe, width=825, text='Добавить конспект', bg_color="#D3E1D5",
                                     font=('Times New Roman', 20),
                                     fg_color="#77AB85", hover_color=("#578E63", "#77AB85"), command=add_task)
        btn_add_task.pack(anchor='nw', side='bottom', pady=10, padx=10, )

        def add(task):
            if not task in lst:
                f = CTk.CTkFrame(mainframe)
                file = open("conspects\\" + task + '.txt', 'w')
                file.close()
                CTk.CTkButton(f, text=task, width=790, bg_color="#D3E1D5", font=('Times New Roman', 20),
                              fg_color="#77AB85", hover_color=("#578E63", "#77AB85"),
                              command=lambda: openfile(task)).pack(side='left')
                CTk.CTkButton(f, text='✕', width=30, bg_color="#D3E1D5", font=('Times New Roman', 20),
                              fg_color="#77AB85", hover_color=("#B9464C", "#77AB85"),
                              command=lambda: delete(task, f)).pack(side='left')
                f.pack(anchor='nw', padx=10, pady=10)
                lst.append(task)
            else:
                showinfo(title="Добавление", message="У вас уже есть данный конспект")

        # "Фальшивое" добавление конспекта, сделанное для того, чтобы при запуске программы сразу загружались ранее созданные конспекты
        def fake_add(task):
            f = CTk.CTkFrame(mainframe)

            CTk.CTkButton(f, text=task, width=790, bg_color="#D3E1D5", font=('Times New Roman', 20), fg_color="#77AB85",
                          hover_color=("#578E63", "#77AB85"), command=lambda: openfile(task)).pack(side='left')
            CTk.CTkButton(f, text='✕', width=30, bg_color="#D3E1D5", font=('Times New Roman', 20), fg_color="#77AB85",
                          hover_color=("#B9464C", "#77AB85"), command=lambda: [delete(task, f), ]).pack(side='left')
            f.pack(anchor='nw', padx=10, pady=10, )

        # Сохранение текста конспекта в файл
        def Save(task, inf):
            with open("conspects\\" + task + '.txt', 'w') as file:
                file.write(inf)
                file.close()

        # Эта функция начинает использваться, когда открывается какой-либо конспект. Создается новый фрейм и
        # выдвигается на передний план, а старый скрывается. Добавляется текстовое поле и 2 кнопки.
        def openfile(name):
            mainframe.pack_forget()
            secframe = CTk.CTkFrame(self.rectengle3)
            secframe.place(x=0, y=0)
            secframe.pack(fill="both", expand=True)
            secframe.tkraise()

            text_area = CTk.CTkTextbox(secframe, height=524, width=840)
            text_area.pack(fill="both", expand=True, padx=10, pady=10, )
            text_area.configure(fg_color='white', font=('Times New Roman', 18))  # цвет фона в конспекте здесь
            with open("conspects\\" + name + '.txt', 'r') as file:
                text = file.read()
                text_area.insert("1.0", text)

            c = CTk.CTkButton(secframe, text='сохранить', font=('Times New Roman', 20), fg_color="#77AB85",
                              hover_color=("#578E63", "#77AB85"),
                              command=lambda: Save(name, text_area.get('1.0', END)[:-1]))
            c.pack(anchor='e', side='right', pady=[0, 9], padx=10)

            b = CTk.CTkButton(secframe, font=('Times New Roman', 20), text='назад', fg_color="#77AB85",
                              hover_color=("#578E63", "#77AB85"),
                              command=lambda: (back(name, text_area.get('1.0', END)[:-1],
                                                    secframe)))  # [secframe.destroy(), mainframe.pack(fill="both", side="top", expand=True)]
            b.pack(anchor='w', side='left', padx=10, pady=[0, 9])

        # def pos_replace(a,b):

        # Функция, вызываемая нажатием кнопки "назад". Проверяет, был ли изменен текст с конспекте, по сравнению с данными в файле,
        # и при наличии изменений появляется окно. В зависимости от выбора либо происходит сохранение и последующее разрушение
        # фрейма конспекта, либо разрушение фрейма без сохранения
        def back(name, inf, secframe):
            with open("conspects\\" + name + '.txt', 'r') as file:
                text = file.read()
                if text != inf:
                    result = askokcancel(title="Подтвержение операции", message="Файл был изменен, сохранить?")
                    if result:
                        Save(name, inf)
                        secframe.destroy()
                        mainframe.pack(fill="both", side="top", expand=True)
                    elif not result:
                        secframe.destroy()
                        mainframe.pack(fill="both", side="top", expand=True)
                else:
                    secframe.destroy()
                    mainframe.pack(fill="both", side="top", expand=True)

        # Функция вызывется при попытке удалить конспект. Сделано для того, чтобы конспект случайно не удалили.
        # С удалением конспекта удаляется и связанный с ним файл
        def delete(task, f):
            result = askyesno(title="Подтвержение операции", message="Подтвердить операцию?")
            if result:
                os.remove("conspects\\" + task + '.txt')
                f.pack_forget()

        # основное окно

        # картинка крестика

        # То самое "фальшивое" создание кнопок, о котором я писал выше, сделано так, потому что нормальное создание кнопок не подходит
        a = 0
        lst = os.listdir('conspects')
        for i in lst:
            res_lst = lst[a].replace('.txt', '')
            lst[a] = res_lst
            fake_add(res_lst)
            a += 1
        self.select_frame_by_name("month")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.month_b.configure(fg_color=("#8CBA98", "#AFDFBC") if name == "month" else "transparent")
        self.week_b.configure(fg_color=("#8CBA98", "#AFDFBC") if name == "trek" else "transparent")
        self.days_b.configure(fg_color=("#8CBA98", "#AFDFBC") if name == "days" else "transparent")
        self.conspect_b.configure(fg_color=("#8CBA98", "#AFDFBC") if name == "conspect" else "transparent")

        # show selected frame
        if name == "month":
            self.month.place(x=340, y=0)
        else:
            self.month.place_forget()
        if name == "trek":
            self.trek.place(x=340, y=0)
        else:
            self.trek.place_forget()
        if name == "days":
            self.days.place(x=340, y=0)
        else:
            self.days.place_forget()
        if name == "conspect":
            self.conspect.place(x=340, y=0)
        else:
            self.conspect.place_forget()


    def month_b_event(self):
        self.select_frame_by_name("month")

    def week_b_event(self):
        self.select_frame_by_name("trek")

    def days_b_event(self):
        self.select_frame_by_name("days")

    def conspect_b_event(self):
        self.select_frame_by_name("conspect")



    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    import login
    app=App()
    app.resizable(False, False)
    app.mainloop()
