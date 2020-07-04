from tkinter import messagebox
import tkinter as tk
from encryption import Encryption
from info_page import InfoPage
import time

class LoginPage(tk.Canvas): 

    def __init__(self, parent, main_page): 

        #for recreating after destroying and using outside the namspace of __init__() if needed
        self.parent = parent
        self.main_page = main_page
        
        
        self.__bg = "#00FF96"
        self.__fg = "#f44336"

        super().__init__(parent, bg = self.__bg, highlightbackground = "#f44336", highlightthickness = "2", relief = "flat") 

        #user_name Label
        self.__labelUser = tk.Label(
            self, text = "User Name:", font = ("Qualy", 30), 
            bg = self.__bg, fg = self.__fg, 
            relief = "flat"
        )
        self.__labelUser.place(relwidth = 0.2, relheight = 0.1, relx = 0.05, rely = 0.2)

        #password_label
        self.__labelPassword = tk.Label(
            self, text = "Password:", font = ("Qualy", 30), 
            bg = self.__bg, fg = self.__fg, 
            relief = "flat"
        )
        self.__labelPassword.place(relwidth = 0.2, relheight = 0.1, relx = 0.05, rely = 0.4)

        #user_entry_box
        self.__user_entry = tk.Entry(
            self, bd = 0, font = ("comfortaa", 30), 
            highlightcolor = "#f44336", highlightthickness = "2", 
            relief = "flat"
        )
        self.__user_entry.place(relheight = .1, relwidth = .7, relx = 0.25, rely = 0.2)

        #password_enrty_box
        self.__password_entry = tk.Entry(
            self, bd = 0, font = ("comfortaa", 30), show = "*",
            highlightcolor = "#f44336", highlightthickness = "2", 
            relief = "flat"
        )
        self.__password_entry.place(relheight = .1, relwidth = .7, relx = 0.25, rely = 0.4)


        #submit button
        self.__button1 = tk.Button(
            self, bd = 4, text = "Submit", font = ("Skate Brand", 30), 
            bg =  self.__bg, fg = self.__fg, activebackground = "#4fc3f7", 
            command = self.post_checking,  relief = "groove"
        )
        
        self.__password_entry.bind("<Return>", self.post_checking)
        self.__button1.place(relwidth = .2, relheight = 0.1, relx = .4, rely = .6)


    def post_checking(self, *kwargs): 

        if (len(self.__user_entry.get()) == 0 or len(self.__password_entry.get()) == 0): 

            messagebox.showerror("Error", "Username or Password is Empty!")

        else:

            self.checker = Encryption()

            if self.__user_entry.get().rstrip() in self.checker.mod_decrypt("credentials.encrypted").keys(): 

                if self.__password_entry.get() == self.checker.mod_decrypt("credentials.encrypted").get(self.__user_entry.get().rstrip()):

                    messagebox.showinfo("WELCOME!", (self.__user_entry.get().split("_")[0]).title())       

                    self.main_page.canvases.update({"info_page": InfoPage(self.main_page.interface, self.main_page, self.__user_entry.get())})

                    self.destroy()
                    self.__init__(self.parent, self.main_page)

                    self.main_page.show_canvas("info_page")
                
                else: 

                    messagebox.showerror("Error!", "Incorrect Password!\nCheck for white space at the end!!")
                
            else: 

                messagebox.showerror("Error!", "No user found.\nCheck user name.")
                self.__password_entry.delete(0, "end")
