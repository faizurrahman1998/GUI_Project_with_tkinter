from PIL import ImageTk, Image
from tkinter import messagebox
from encryption import Encryption
from info_page import InfoPage
from sign_up import SignUP
import tkinter as tk
import io

class LoginPage(tk.Canvas): 

    def __init__(self, parent, main_page): 

        #for recreating after destroying and using outside the namspace of __init__() if needed
        self.parent = parent
        self.main_page = main_page
        self.credentials = self.main_page.connection.MechatronicsDB.Credentials
        self.icons = self.main_page.connection.MechatronicsDB.Iconbase
        
        
        self.__bg = "#00FF96"
        self.__fg = "#1565C0"
        self.highlightbackground = "#1976D2"
        self.highlightcolor = "#f44336"
        self.active_colour = "#42A5F5"

        super().__init__(
            parent, bg = self.__bg, highlightbackground = self.highlightbackground, highlightthickness = "2", highlightcolor = self.highlightcolor,
            relief = "flat"
        ) 

        self.bind("<Button-1>", lambda var : [self.focus_set(), self.active()])

        #user_name Label
        self.__labelUser = tk.Label(
            self, text = "User Name", font = ("Qualy", 30), 
            bg = self.__bg, fg = self.__fg, 
            relief = "flat", anchor = "w"
        )
        self.__labelUser.place(relwidth = 0.2, relheight = 0.1, relx = 0.05, rely = 0.15)

        #password_label
        self.__labelPassword = tk.Label(
            self, text = "Password", font = ("Qualy", 30), 
            bg = self.__bg, fg = self.__fg, 
            relief = "flat", anchor = "w"
        )
        self.__labelPassword.place(relwidth = 0.2, relheight = 0.1, relx = 0.05, rely = 0.38)

        #user_entry_box
        self.__user_entry = tk.Entry(
            self, bd = 5, font = ("comfortaa", 30), 
            bg = self.__bg, highlightbackground = self.highlightbackground, highlightthickness = "2", highlightcolor = self.highlightcolor,
            relief = "flat"
        )
        self.__user_entry.bind("<Button-1>", lambda var: [self.__user_entry.focus_set(), self.active()])
        self.__user_entry.bind("<Return>", lambda var: [self.__password_entry.focus_set(), self.active()])
        self.__user_entry.place(relheight = .1, relwidth = .9, relx = 0.05, rely = 0.26)

        #password_enrty_box
        self.__password_entry = tk.Entry(
            self, bd = 0, font = ("comfortaa", 30), show = "*",
            bg = self.__bg, highlightbackground = self.highlightbackground, highlightcolor = self.highlightcolor, highlightthickness = "2", 
            relief = "flat"
        )
        self.__password_entry.bind("<Button-1>", lambda var: [self.__password_entry.focus_set(), self.active()])
        self.__password_entry.bind("<Return>", lambda var: [self.__button1.focus_set(), self.active()])
        self.__password_entry.place(relheight = .1, relwidth = .9, relx = 0.05, rely = 0.49)

        self.loaded_icons = {
            "hide" : ImageTk.PhotoImage(Image.open(io.BytesIO(self.icons.find_one({"_id" : "hide"}).get("image"))).resize((45, 45), Image.ANTIALIAS)), 
            "show" : ImageTk.PhotoImage(Image.open(io.BytesIO(self.icons.find_one({"_id" : "show"}).get("image"))).resize((45, 45), Image.ANTIALIAS))
        }

        #hide_and_seek_button
        self.hide_n_seek = tk.Button(
            self, image = self.loaded_icons.get("show"), 
            bg = self.__bg, highlightbackground = self.__bg, activebackground = self.__bg, 
            command = self.hide_and_seek, relief = "flat"
        )
        self.bind("<Button-1>", lambda var: self.active())
        self.hide_n_seek.place(relwidth = 0.04, relheight = 0.08, relx = 0.905, rely = 0.5)


        #submit button
        self.__button1 = tk.Button(
            self, text = "Submit", font = ("Skate Brand", 25), 
            bg =  self.__bg, fg = self.__fg, highlightbackground = "#FF5722", activebackground = self.__fg, activeforeground = self.__bg,
            command = self.post_checking,  relief = "groove"
        )
        self.__button1.place(relwidth = .2, relheight = 0.1, relx = .4, rely = .705)


        #sign_up_section
        self.__messagelabel = tk.Label(
            self, text = "Don't have an account?", font = ("comfortaa", 15), 
            bg = self.__bg,
            relief = "flat", anchor = "e"
        )
        self.__messagelabel.place(relwidth = 0.22, relheight = 0.05, relx = 0.65, rely = 0.92)

        self.__button2 = tk.Button(
            self, bd = 0, text = "Sign Up?", font = ("qualy", 15), 
            bg = self.__bg, fg = "#1976D2", activebackground = "#2E4053", activeforeground = self.__bg, highlightbackground = "#1976D2", 
            command = lambda : SignUP(self.main_page), 
            relief = "flat"
        )
        self.__button2.place(relwidth = 0.1, relheight = 0.08, relx = 0.88, rely = 0.9)

    
    
    def active(self):

        self.frame_name = str(self.focus_get()).rsplit("!", 1)[0]

        if str(self.focus_get()) == f"{self.frame_name}!entry":

            self.__labelUser.configure(fg = self.highlightcolor)
            self.__user_entry.configure(bg = self.active_colour)
        
        else:
            self.__labelUser.configure(fg = self.__fg)
            self.__user_entry.configure(bg = self.__bg)


        if str(self.focus_get()) == f"{self.frame_name}!entry2":

            self.__labelPassword.configure(fg = self.highlightcolor)
            self.__password_entry.configure(bg = self.active_colour)
            self.hide_n_seek.configure(bg = self.active_colour, activebackground = self.active_colour, highlightcolor = self.active_colour)
        
        else:
            self.__labelPassword.configure(fg = self.__fg)
            self.__password_entry.configure(bg = self.__bg)
            self.hide_n_seek.configure(bg = self.__bg, activebackground = self.__bg, highlightcolor = self.__bg)
        
        
    def hide_and_seek(self):
        
        if self.__password_entry.cget("show") == "*" : 

            self.__password_entry.configure(show = "")
            self.hide_n_seek.configure(image = self.loaded_icons.get("hide"))

        else: 

            self.__password_entry.configure(show = "*")
            self.hide_n_seek.configure(image = self.loaded_icons.get("show"))
       



                

    def post_checking(self, *kwargs): 

        if (len(self.__user_entry.get()) == 0 or len(self.__password_entry.get()) == 0): 

            messagebox.showerror("Error", "Username or Password is Empty!")

        else:
            self.checker = Encryption()

            try:
            
                if self.__user_entry.get().rstrip() == self.credentials.find_one({"user_name" : self.__user_entry.get().rstrip()}).get("user_name"): 

                    if self.__password_entry.get() == self.checker.decrypt(self.credentials.find_one({"user_name" : self.__user_entry.get().rstrip()}).get("password").encode()).decode():

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
            
            except:
                
                messagebox.showerror("Error", "Username doesn't exist.")
