from encryption import Encryption
from PIL import ImageTk, Image
import tkinter as tk 

class InfoPage(tk.Canvas): 

    def __init__(self, parent, main_page, user_name): 

        #for recreating after destrying the object
        self.main_page = main_page
        self.parent = parent
        self.user_name = user_name

        super().__init__(parent, bg = "#58d68d", highlightbackground = "#f44336", highlightthickness = "3", relief = "flat")

        #image_path_reference 
        self.images = {
            "user_image" : self.load_image(".//image_base//nilan_001.png")
        }

        #for holding the user_image
        self.image_holder = tk.Label(
            self, image = self.images.get("user_image"),
            bg = "#00FF66",
            relief = "flat"
        )
        self.image_holder.place(relwidth = 0.145, relheight = .25, relx = 0.852, rely = 0.009)
        
        #logout button
        self.button1 = tk.Button(
            self, bd = 2, text = "Log_out", font = ("skate brand", 20),
            bg = "#58d68d", fg = "#f44336", activebackground = "#f44336", 
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
