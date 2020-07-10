from encryption import Encryption
from PIL import ImageTk, Image
import tkinter as tk 

class InfoPage(tk.Canvas): 

    def __init__(self, parent, main_page, user_name): 

        #for recreating after destrying the object
        self.main_page = main_page
        self.parent = parent
        self.user_name = user_name
        self.informations = self.main_page.connection.MechatronicsDB.Informations

        self.__bg = "#58d68d"

        super().__init__(parent, bg = self.__bg, highlightbackground = "#f44336", highlightthickness = "3", relief = "flat")

        self.checker = Encryption()

        #image_path_reference 
        self.images = {
            "user_image" : self.load_image(self.informations.find_one({"user_name" : self.user_name}).get("info").get("image"))
        }

        #for holding the user_image
        self.image_holder = tk.Label(
            self, image = self.images.get("user_image"),
            bg = self.__bg,
            relief = "flat"
        )
        self.image_holder.place(relwidth = 0.145, relheight = .25, relx = 0.852, rely = 0.009)


        #for the top label
        self.top_label = tk.Label(
            self, text = "personal information", font = ("qualy", 35),
            bg = self.__bg, 
        )
        self.top_label.place(relwidth = 0.4, relheight = 0.08, relx = .225, rely = 0.18)

        
        self.name_label = tk.Label(
            self, text = "Name", font = ("comfortaa", 30, "bold"), 
            bg = self.__bg,
        )
        self.name_label.place(relwidth = 0.1, relheight = .06, relx = 0.063, rely = 0.35)

        self.id_label = tk.Label(
            self, text = "Id", font = ("comfortaa", 30, "bold"), 
            bg = self.__bg,
        )
        self.id_label.place(relwidth = 0.1, relheight = 0.06, relx = 0.063, rely = 0.45)

        self.email_label = tk.Label(
            self, text = "Email", font = ("comfortaa", 30, "bold"), 
            bg = self.__bg,
        )
        self.email_label.place(relwidth = 0.1, relheight = 0.06, relx = 0.063, rely = 0.55)



        self.colon1 = tk.Label(
            self, text = ":", font = ("comfortaa", 30, "bold"),
            bg = self.__bg,
        )
        self.colon1.place(relheight = 0.06, relx = .17, rely = .35)

        self.colon2 = tk.Label(
            self, text = ":", font = ("comfortaa", 30, "bold"),
            bg = self.__bg,
        )
        self.colon2.place(relheight = 0.06, relx = .17, rely = .45)

        self.colon3 = tk.Label(
            self, text = ":", font = ("comfortaa", 30, "bold"),
            bg = self.__bg,
        )
        self.colon3.place(relheight = 0.06, relx = .17, rely = .55)



        self.name_holder = tk.Label(
            self, text = self.informations.find_one({"user_name" : self.user_name}).get("info").get("name"), font = ("comfortaa", 25), anchor = "w",
            bg = self.__bg,
        )
        self.name_holder.place(relwidth = .5, relheight = 0.06, relx = .2, rely = 0.35)

        self.id_holder = tk.Label(
            self, text = self.informations.find_one({"user_name" : self.user_name}).get("info").get("ID"), font = ("comfortaa", 25), anchor = "w",
            bg = self.__bg,
        )
        self.id_holder.place(relwidth = .5, relheight = 0.06, relx = .2, rely = 0.45)

        self.email_holder = tk.Label(
            self, text = self.informations.find_one({"user_name" : self.user_name}).get("info").get("email"), font = ("comfortaa", 25), anchor = "w",
            bg = self.__bg,
        )
        self.email_holder.place(relwidth = .5, relheight = 0.06, relx = .2, rely = 0.55)





        #logout button
        self.button1 = tk.Button(
            self, bd = 2, text = "Log_out", font = ("skate brand", 20),
            bg = self.__bg, fg = "#f44336", activebackground = "#f44336", 
            command = lambda: self.load_page("login_page"), 
            relief = "groove"
        )
        self.button1.place(relwidth = 0.095, relheight = 0.06, relx = 0.9, rely = 0.935)


    def load_image(self, path): 

        return ImageTk.PhotoImage(Image.open(path).resize((200, 180), Image.ANTIALIAS))


    def load_page(self, page_name): 

        self.destroy()
        self.__init__(self.parent, self.main_page, self.user_name)

        self.main_page.show_canvas(page_name)
