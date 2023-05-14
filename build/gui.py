from calendar import Calendar
from pathlib import Path
import os
from tkinter import END
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
            Image.open(os.path.join(ASSETS_PATH, "image_4.png")),size=(50,50))

        # иконка календаря
        self.image_5 = CTk.CTkImage(
            Image.open(os.path.join(ASSETS_PATH, "image_5.png")),size=(50,50))

        # иконка месяца недели 3
        self.image_6 = CTk.CTkImage(
            Image.open(os.path.join(ASSETS_PATH, "image_6.png")),size=(50,50))

        # иконка конспектов
        self.image_7 = CTk.CTkImage(
            Image.open(os.path.join(ASSETS_PATH, "image_7.png")),size=(40,40))

        self.image_8 = CTk.CTkImage(
            Image.open(os.path.join(ASSETS_PATH, "arrow_1.png")), size=(24.52, 49))

        self.image_9 = CTk.CTkImage(
            Image.open(os.path.join(ASSETS_PATH, "arrow_2.png")), size=(24.52, 49))

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


        self.cal = Calendar(self.CalendarZ, selectmode="day", background='green', borderwidth=25, foreground='white',
                            font="Helvetica 30", width=655, height=528,
                            showweeknumbers=False, locale='ru', showothermonthdays=False)
        self.cal.place(x=70,y=110)

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

        self.button_6 = CTk.CTkButton(
            master=self.navigation_frame,
            text="Календарь",
            corner_radius=0,
            image=self.image_5,
            hover_color=( "#578E63","#77AB85"),
            border_spacing=0,
            fg_color="#77AB85",
            font=("Century Gothic", 32),
            width=340.0,
            height=80.0

        )
        self.button_6.place(
            x=0.0,
            y=160.0,
        )

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
            text="Неделя",
            corner_radius=0,
            image=self.image_7,
            compound="left",
            hover_color=( "#578E63","#77AB85"),
            border_spacing=0,
            fg_color="#77AB85",
            font=("Inter Light", 32),
            command=self.week_b_event,
            width=375.0,
            height=80.0
        )
        self.week_b.place(
            x=0.0,
            y=320.0,
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
            y=400.0,
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
            y=480.0,
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

        #НЕДЕЛЬНЫЙ ФРЕЙМ
        self.week = customtkinter.CTkFrame(master=self, corner_radius=0,
            fg_color = "#D8F8DF",
            height = 720,
            width = 940,

        )

        self.user_name = CTk.CTkTextbox(
            master=self.week,
            font=("IrishGrover Regular", 20 * -1),
            width=100,
            height=40
        )
        self.user_name.insert("0.0", "#USER2")
        self.user_name.place(x=812, y=60)

        self.img2 = CTk.CTkLabel(master=self.week, image=self.image_2, text="", width=70, height=70,
                                 bg_color="#D8F8DF")
        self.img2.place(
            x=715.0,
            y=38.0,
        )

        self.img3 = CTk.CTkLabel(master=self.week, image=self.image_3, text="", width=857, height=1,
                                 bg_color="#D8F8DF")
        self.img3.place(
            x=41.5,
            y=121.5,
        )

        self.citate = CTk.CTkTextbox(
            master=self.week,
            font=("IrishGrover Regular", 20 * -1),
            width=511,
            height=48
        )
        self.citate.insert("0.0", "Treat your habits like your plants")
        self.citate.place(x=44, y=60)

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

        self.D1 = CTk.CTkLabel(master=self.days, text="1 DAY", width=285, height=56,
                                 bg_color="#A6C7AB", font=('Inter',40), text_color="white")
        self.D1.place(
            x=34, y=170
        )

        self.D2 = CTk.CTkLabel(master=self.days, text="2 DAY", width=285, height=56,
                               bg_color="#A6C7AB", font=('Inter', 40), text_color="white")
        self.D2.place(
            x=326, y=170
        )

        self.D3 = CTk.CTkLabel(master=self.days, text="3 DAY", width=285, height=56,
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

        self.user_name = CTk.CTkTextbox(
            master=self.conspect,
            font=("IrishGrover Regular", 20 * -1),
            width=100,
            height=40
        )
        self.user_name.insert("0.0", "#USER2")
        self.user_name.place(x=812, y=60)

        self.img2 = CTk.CTkLabel(master=self.conspect, image=self.image_2, text="", width=70, height=70,
                                 bg_color="#D8F8DF")
        self.img2.place(
            x=715.0,
            y=38.0,
        )

        self.img3 = CTk.CTkLabel(master=self.conspect, image=self.image_3, text="", width=857, height=1,
                                 bg_color="#D8F8DF")
        self.img3.place(
            x=41.5,
            y=121.5,
        )

        self.citate = CTk.CTkTextbox(
            master=self.conspect,
            font=("Century Gothic", 20 * -1),
            width=511,
            height=48
        )
        self.citate.insert("0.0", "Treat your habits like your plants")
        self.citate.place(x=44, y=60)



        self.select_frame_by_name("month")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.month_b.configure(fg_color=("#8CBA98", "#AFDFBC") if name == "month" else "transparent")
        self.week_b.configure(fg_color=("#8CBA98", "#AFDFBC") if name == "week" else "transparent")
        self.days_b.configure(fg_color=("#8CBA98", "#AFDFBC") if name == "days" else "transparent")
        self.conspect_b.configure(fg_color=("#8CBA98", "#AFDFBC") if name == "conspect" else "transparent")

        # show selected frame
        if name == "month":
            self.month.place(x=340, y=0)
        else:
            self.month.place_forget()
        if name == "week":
            self.week.place(x=340, y=0)
        else:
            self.week.place_forget()
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
        self.select_frame_by_name("week")

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
