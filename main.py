import customtkinter
import os
from PIL import Image
import calendar
import datetime

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Planerovsschic")
        self.geometry("1100x700")

        #blanks for the calendar
        def fill():
            self.info_label['text'] = calendar.month_name[month] + ', ' + str(year)

            month_days = calendar.monthrange(year, month)[1]
            if month == 1:
                back_month_days = calendar.monthrange(year - 1, 12)[1]
            else:
                back_month_days = calendar.monthrange(year, month - 1)[1]
            week_day = calendar.monthrange(year, month)[0]

            for n in range(month_days):
                days[n + week_day]['text'] = n + 1
                days[n + week_day]['fg'] = 'black'
                if year == now.year and month == now.month and n == now.day:
                    days[week_day]['bg'] = 'green'
                    days[n + week_day]['bg'] = 'grey'
                else:
                    days[n + week_day]['bg'] = 'gray'



        days=[]
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day





                    # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(15, 15))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "R_arrow_black.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "R_arrow_white.png")), size=(15, 15))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "projects_black.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "projects_white.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "conspects_black.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "conspects_white.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Image Example", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Calendar",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Projects",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Conspects",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=100, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent", )
        self.home_frame.grid_columnconfigure(4, weight=5)



        #self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        #self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)


        self.back_button = customtkinter.CTkButton(self.home_frame,  corner_radius=0, height=50,width=50,
                                                     border_spacing=1, text="<", compound="left" )
        self.back_button.grid(row=0, column=0, padx=0, pady=0)

        self.next_button = customtkinter.CTkButton(self.home_frame, corner_radius=0, height=50, border_spacing=1,width=50,
                                                     text=">", compound="left")
        self.next_button.grid(row=0, column=6, padx=0, pady=0)

        self.info_label = customtkinter.CTkLabel(self.home_frame, text='012', width=1, height=1)
        self.info_label.grid(row=0, column=1, columnspan=5, sticky="NSEW")

        for n in range (0,7):
            self.dni=customtkinter.CTkLabel(self.home_frame, text=calendar.day_abbr[n], width=50, height=50, fg_color='blue')
            self.dni.grid(row=1, column=n, sticky="NSEW", )
        for row in range(5):
            for col in range(7):
                self.dni= customtkinter.CTkButton(self.home_frame, text="0", width=100, height=100)
                self.dni.grid(row=row+2, column=col, sticky="NSEW")
                days.append(self.dni)

        #self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        #self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        fill()

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

    app = App()
    app.mainloop()
