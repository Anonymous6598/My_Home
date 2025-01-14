import customtkinter, tkintermapview, typing, geocoder, CTkMenuBar, locale, My_Maps_Interface, os, subprocess, sys, platform

class Program(customtkinter.CTk, My_Maps_Interface.My_Maps_Interface):
    
    TITLE: typing.Final[str] = f"My Maps  "
    ICON: typing.Final[str] = f"Apps\My_Maps\my maps icon.ico"
    WIDGET_SCALING: typing.Final[int] = 1.251
    
    def __init__(self: typing.Self, *args: typing.Any, **kwargs: typing.Any) -> None:
        customtkinter.CTk.__init__(self, *args, **kwargs)
        
        customtkinter.deactivate_automatic_dpi_awareness()
        customtkinter.set_widget_scaling(self.WIDGET_SCALING)
        
        self.title(self.TITLE)
        self.protocol(f"WM_DELETE_WINDOW", lambda: self.destroy())
        
        if platform.system() == f"Windows":
            self.iconbitmap(self.ICON)


        if platform.system() == f"Linux":
            self.main_screen_menu: CTkMenuBar.CTkMenuBar = CTkMenuBar.CTkMenuBar(master=self)
		
        else:
            self.main_screen_menu: CTkMenuBar.CTkTitleMenu = CTkMenuBar.CTkTitleMenu(master=self)

        self.main_screen_current_cordinates: tuple[float, float] = geocoder.ip(f"me")

        self.main_screen_menu_menu_button: customtkinter.CTkButton = self.main_screen_menu.add_cascade(text=f"☰")

        self.main_screen_menu_dropdownmenu: CTkMenuBar.CustomDropdownMenu = CTkMenuBar.CustomDropdownMenu(widget=self.main_screen_menu_menu_button)

        self.main_screen_map: tkintermapview.TkinterMapView = tkintermapview.TkinterMapView(master=self, corner_radius=0)
        self.main_screen_map.pack(fill=f"both", expand=True)
        
        self.main_screen_map.set_position(self.main_screen_current_cordinates.latlng[0], self.main_screen_current_cordinates.latlng[1])

        if locale.getdefaultlocale()[0] == f"sr_RS":
            self.main_screen_menu_dropdownmenu.add_option(option=f"🔎 (претрага)", command=self.__search__)
            self.main_screen_menu_dropdownmenu.add_option(option=f"AI", command=lambda: self.__open_ai_window__())
        
        elif locale.getdefaultlocale()[0] == f"ru_RU":
            self.main_screen_menu_dropdownmenu.add_option(option=f"🔎 (поиск)", command=self.__search__)
            self.main_screen_menu_dropdownmenu.add_option(option=f"ИИ (Нейро сеть)", command=lambda: self.__open_ai_window__())
        
        else:
            self.main_screen_menu_dropdownmenu.add_option(option=f"🔎 (search)", command=self.__search__)
            self.main_screen_menu_dropdownmenu.add_option(option=f"AI", command=lambda: self.__open_ai_window__())

    @typing.override
    def __search__(self: typing.Self) -> None:
        if locale.getdefaultlocale()[0] == f"sr_RS":
            self.main_screen_search_dialog: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(text=f"претрага", title=f"претрага", button_fg_color=f"green")
            self.after(250, lambda: self.main_screen_search_dialog.iconbitmap(self.ICON))
            
            self.main_screen_map.set_address(self.main_screen_search_dialog.get_input())
        
        elif locale.getdefaultlocale()[0] == f"ru_RU":
            self.main_screen_search_dialog: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(text=f"поиск", title=f"поиск", button_fg_color=f"green")
            self.after(250, lambda: self.main_screen_search_dialog.iconbitmap(self.ICON))
            
            self.main_screen_map.set_address(self.main_screen_search_dialog.get_input())

        else:
            self.main_screen_search_dialog: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(text=f"search", title=f"search", button_fg_color=f"green")
            self.after(250, lambda: self.main_screen_search_dialog.iconbitmap(self.ICON))
            
            self.main_screen_map.set_address(self.main_screen_search_dialog.get_input())

    def __open_ai_window__(self: typing.Self) -> None:
        if platform.system() == f"Linux":
            os.popen(f"python3 Apps\My_Maps\My_Maps_AI_window.py")

        else:
            os.startfile(f"Apps\My_Maps\My_Maps_AI_window.py", show_cmd=False)
        
if __name__ == f"__main__":
    program: Program = Program().mainloop()