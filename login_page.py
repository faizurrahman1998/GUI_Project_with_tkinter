from tkinter import messagebox
import tkinter as tk

class LoginPage(tk.Frame): 

    def __init__(self, parent, main_app): 
        
        self.__bg = "#00FF96"
        self.__fg = "#f44336"

        super().__init__(parent, bg = self.__bg, highlightbackground = "#f44336", highlightthickness = "2", relief = "flat") 

        #user_name Label
        self.__labelUser = tk.Label(
            self, text = "User Name:", font = ("Qualy", 20), bg = self.__bg, 
            fg = self.__fg, relief = "flat"
        )
        self.__labelUser.place(relwidth = 0.2, relheight = 0.1, relx = 0.05, rely = 0.2)

        #password_label
        self.__labelPassword = tk.Label(
            self, text = "Password:", font = ("Qualy", 20), bg = self.__bg, 
            fg = self.__fg, relief = "flat"
        )
        self.__labelPassword.place(relwidth = 0.19, relheight = 0.1, relx = 0.05, rely = 0.4)

        #user_entry_box
        self.__user_entry = tk.Entry(self, bd = 0, font = ("comfortaa", 35), highlightcolor = "#f44336", highlightthickness = "2", relief = "flat")
        self.__user_entry.place(relheight = .1, relwidth = .7, relx = 0.25, rely = 0.2)

        #password_enrty_box
        self.__password_entry = tk.Entry(
            self, bd = 0, font = ("comfortaa", 35), highlightcolor = "#f44336", highlightthickness = "2", relief = "flat", show = "*"
        )
        self.__password_entry.place(relheight = .1, relwidth = .7, relx = 0.25, rely = 0.4)


        #submit button
        self.button1 = tk.Button(
            self, bd = 4, text = "Submit", font = ("Skate Brand", 30), 
            bg =  self.__bg, fg = self.__fg, activebackground = "#4fc3f7", 
            command = self.post_checking,  relief = "groove"
        )

        self.button1.place(relwidth = .2, relheight = 0.1, relx = .4, rely = .6)

    def post_checking(self): 

        if (len(self.__user_entry.get()) == 0 or len(self.__password_entry.get()) == 0): 

            messagebox.showerror("Error", "Username or Password is Empty!")

        else: 

            pass
