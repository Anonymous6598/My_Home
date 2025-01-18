import customtkinter, tkinter.messagebox, typing, platform, CTkMenuBar, locale, My_Home_interface, os, PIL.Image, subprocess, sys

class Program(customtkinter.CTk, My_Home_interface.My_Home_interface):
    
    TITLE: typing.Final[str] = f"My Home  "
    COLOR_THEME: typing.Final[str] = f"green"
    ICON: typing.Final[str] = f"Images\my_home_icon.ico"
    WIDGET_SCALING: typing.Final[float] = 1.251
    THEME: typing.Final[str] = f"system"

    def __init__(self: typing.Self, *args, **kwargs) -> None:
        customtkinter.CTk.__init__(self, *args, **kwargs)

        customtkinter.set_widget_scaling(self.WIDGET_SCALING)
        customtkinter.set_default_color_theme(self.COLOR_THEME)
        customtkinter.set_appearance_mode(self.THEME)
        customtkinter.deactivate_automatic_dpi_awareness()

        self.title(self.TITLE)
        self.protocol(f"WM_DELETE_WINDOW", lambda: self.__exit__())
        if platform.system() == f"Windows":
            self.iconbitmap(self.ICON)

        if platform.system() == f"Linux":
            self.main_screen_menu: CTkMenuBar.CTkMenuBar = CTkMenuBar.CTkMenuBar(master=self)
		
        else:
            self.main_screen_menu: CTkMenuBar.CTkTitleMenu = CTkMenuBar.CTkTitleMenu(master=self)

        if locale.getdefaultlocale()[0] == f"sr_RS":
            self.main_screen_application_menu_button: customtkinter.CTkButton = self.main_screen_menu.add_cascade(text=f"Апликације")
            self.main_screen_about_us_button: customtkinter.CTkButton = self.main_screen_menu.add_cascade(text=f"О нама", command=self.__about_us__)   
        
        elif locale.getdefaultlocale()[0] == f"ru_RU":
            self.main_screen_application_menu_button: customtkinter.CTkButton = self.main_screen_menu.add_cascade(text=f"Приложения")
            self.main_screen_about_us_button: customtkinter.CTkButton = self.main_screen_menu.add_cascade(text=f"О нас", command=self.__about_us__)

        else:
            self.main_screen_application_menu_button: customtkinter.CTkButton = self.main_screen_menu.add_cascade(text=f"Applications")
            self.main_screen_about_us_button: customtkinter.CTkButton = self.main_screen_menu.add_cascade(text=f"About Us", command=self.__about_us__)

        self.main_screen_application_menu_submenu: CTkMenuBar.CustomDropdownMenu = CTkMenuBar.CustomDropdownMenu(widget=self.main_screen_application_menu_button, fg_color=f"transparent")

        self.main_screen_my_diary_button: customtkinter.CTkButton = self.main_screen_application_menu_submenu.add_option(option=f"My Diary", command=lambda: self.__start_app__(f"Apps\My_Diary\My_Diary.py"))

        self.main_screen_my_code_button: customtkinter.CTkButton = self.main_screen_application_menu_submenu.add_option(option=f"My Code", command=lambda: self.__start_app__(f"Apps\My_Code\My_Code.py"))

        self.main_screen_my_calculus_button: customtkinter.CTkButton = self.main_screen_application_menu_submenu.add_option(option=f"My Calculus", command=lambda: self.__start_app__(f"Apps\My_Calculus\My_Calculus.py"))
		
        self.main_screen_my_reminder_button: customtkinter.CTkButton = self.main_screen_application_menu_submenu.add_option(option=f"My Reminder", command=lambda: self.__start_app__(f"Apps\My_Reminder\My_Reminder.py"))
		
        self.main_screen_my_reminder_button: customtkinter.CTkButton = self.main_screen_application_menu_submenu.add_option(option=f"My Maps", command=lambda: self.__start_app__(f"Apps\My_Maps\My_Maps.py"))

        self.main_screen_logo: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, image=customtkinter.CTkImage(light_image=PIL.Image.open(f"Images\My_Home_logo.png"), dark_image=PIL.Image.open(f"Images\My_Home_logo.png"), size=(int(self.winfo_screenwidth()), int(self.winfo_screenheight()))), text=f"")
        self.main_screen_logo.pack(expand=True, fill=f"both")

    @typing.override
    def __start_app__(self: typing.Self, app: str) -> None:
        if platform.system() == f"Linux":
            os.popen(f"python3 {app}")

        else:
            os.startfile(f"{app}", show_cmd=False)

    @typing.override
    def __about_us__(self: typing.Self) -> None:
        if locale.getdefaultlocale()[0] == f"sr_RS":
            tkinter.messagebox.showinfo(f"О нама", f"Ово је супер апликација, која има револуционарно корисничко искуство. Уместо 6 - 1 апликација. \nАутори: \n anonymous6598 \n Rastko14 \n Milao671")

        elif locale.getdefaultlocale()[0] == f"ru_RU":
            tkinter.messagebox.showinfo(f"О нас", f"Это суперапп, которое имеет революционный пользовательский щпыт. Вместо 6 - 1 приложения. \nАвторы: \nanonymous6598 \nRastko14 \n Milao671")

        else:
            tkinter.messagebox.showinfo(f"About Us", f"This is a super app, that has a revolutionary user experience. Instead of 6 - 1 app. \nAuthors: \nanonymous6598 \n Rastko14 \n Milao671")

    @typing.override
    def __exit__(self: typing.Self) -> None:
        if platform.system() == f"Windows":
            subprocess.call(f"TASKKILL /F /IM Python.exe", shell=False)
            sys.exit()
				
        else:
            subprocess.call(f"kill python3", shell=False)
            sys.exit()

if __name__ == f"__main__":
    program: Program = Program()
    program.mainloop()