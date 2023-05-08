import customtkinter
from tkcalendar import *
# from Calendar import Calendar
# from CalendarView import CalendarView
from tkinter import *
import tkinter.messagebox
import os
from PIL import Image
import calendar
import datetime


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # задание параметров окна
        self.title("Planerovsschic")
        self.geometry("1900x1200")

        # blanks for the calendar

        # параметры сетки
        self.grid_rowconfigure(0, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        # подгрузка картинок
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.bg = customtkinter.CTkImage(Image.open(os.path.join(image_path, "bg_gradient.jpg")))
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")),
                                                 size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")),
                                                       size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")),
                                                       size=(15, 15))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "R_arrow_black.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "R_arrow_white.png")),
                                                 size=(15, 15))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "projects_black.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "projects_white.png")),
                                                 size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "conspects_black.png")),
            dark_image=Image.open(os.path.join(image_path, "conspects_white.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        # параметры для лого
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Image Example",
                                                             image=self.logo_image,
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)
        # параметры для кнопки календарь
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Calendar",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")
        # параметры для кнопки проекты
        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Projects",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w",
                                                      command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")
        # параметры для кнопки конспекты
        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Conspects",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w",
                                                      command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")
        # параметры для кнопки смены темы
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=100, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="black")
        self.home_frame.grid(row=1, column=1, sticky="nsew", padx=(0, 30), pady=(170, 20))

        self.home_frame1 = customtkinter.CTkFrame(self, corner_radius=0, fg_color="pink", height=150)
        self.home_frame1.grid(row=0, column=1, sticky="nwe", columnspan=3)
        self.home_frame1.grid_rowconfigure(0, weight=2)

        self.cal = Calendar(self.home_frame, selectmode="day", background='pink', borderwidth=25, foreground='white',
                            font="Helvetica 30",
                            showweeknumbers=False, locale='ru', showothermonthdays=False)
        self.cal.pack(fill="both", expand=True)

        self.scroll_ToDo = customtkinter.CTkScrollableFrame(self, width=400, height=600, fg_color='gray')
        self.scroll_ToDo.grid(row=0, column=1, pady=(180, 20))

        def add_todo():
            todo = self.entr.get()
            if todo == "":
                return
            self.Ttodo = customtkinter.CTkCheckBox(self.scroll_ToDo, text=todo)
            self.Ttodo.grid(column=0, pady=5, sticky='w', padx=15)
            self.entr.delete(0, END)

        self.daily = customtkinter.CTkLabel(self.scroll_ToDo, text="Daily Tasks", justify='center',
                                            font=customtkinter.CTkFont(size=20, weight="bold"))
        self.daily.grid(row=0, column=0, padx=150, pady=4)

        self.entr = customtkinter.CTkEntry(self.scroll_ToDo, placeholder_text="...", placeholder_text_color='white',
                                           width=50)
        self.entr.grid(column=0, row=1, pady=10, sticky="sew", padx=(10, 20))

        self.add_button = customtkinter.CTkButton(self.scroll_ToDo, text='add some shit', command=add_todo)
        self.add_button.grid(column=0, row=2)

        # self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="black")
        # self.home_frame.grid(row=0, column=0, sticky="nsew")
        #
        # self.home_frame1 = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color="pink", height=150)
        # self.home_frame1.grid(row=0, column=0, sticky="nwe", columnspan=3)
        # self.home_frame1.grid_rowconfigure(0, weight=2)
        #
        # self.cal = Calendar(self.home_frame, selectmode="day", background='pink', borderwidth=25, foreground='white',
        #                     font="Helvetica 30",
        #                     showweeknumbers=False, locale='ru', showothermonthdays=False)
        # self.cal.grid()
        #
        # self.scroll_ToDo = customtkinter.CTkScrollableFrame(self.home_frame, width=400, height=600, fg_color='gray')
        # self.scroll_ToDo.grid(row=0, column=1, pady=(180, 20))
        #
        # def add_todo():
        #     todo = self.entr.get()
        #     if todo == "":
        #         return
        #     self.Ttodo = customtkinter.CTkCheckBox(self.scroll_ToDo, text=todo)
        #     self.Ttodo.grid(column=0, pady=5, sticky='w', padx=15)
        #     self.entr.delete(0, END)
        #
        # self.daily = customtkinter.CTkLabel(self.scroll_ToDo, text="Daily Tasks", justify='center',
        #                                     font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.daily.grid(row=0, column=0, padx=150, pady=4)
        #
        # self.entr = customtkinter.CTkEntry(self.scroll_ToDo, placeholder_text="...", placeholder_text_color='white',
        #                                    width=50)
        # self.entr.grid(column=0, row=1, pady=10, sticky="sew", padx=(10, 20))
        #
        # self.add_button = customtkinter.CTkButton(self.scroll_ToDo, text='add some shit', command=add_todo)
        # self.add_button.grid(column=0, row=2)
        #

        # self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        # self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        # параметры для Отображения месяца нв календаре

        # self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        # self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=2, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    import login
    app = App()
    app.mainloop()
