import tkinter as tk 
from PIL import ImageTk, Image
from login_page import LoginPage
from info_page import InfoPage

class AppEngine(tk.Tk): 

    def __init__(self): 

        super().__init__()
        self.title("MTE")
        self.geometry("1400x900")


        #main_canvas
        self.interface = tk.Canvas(self, bg = "#00FF66")
        self.interface.place(relwidth = 1, relheight = 1)

        #image_directories
        self.images = {
            "logo": self.ready_img("logo.png", (120, 130))
        }

        #all the sikns(frames)
        self.frames = { 
            "login_page": LoginPage(self.interface, self), 
            "info_page": InfoPage(self.interface, self)
        }

        #adding the logo
        self.image = tk.Label(self.interface, image = self.images.get("logo"), bg = "#00FF66", relief = "flat")
        self.image.place(relx = 0.009, rely = 0.015)

        #adding the statusbar
        self.status_bar = tk.Label(
            self.interface, text = "MECHATRONICS", bg = "#00FF66", 
            relief = "flat", 
            anchor = "n",
            font = ("My Font", 100),     
        )
        self.status_bar.place(relwidth = .8, relheight = .185, relx = .16, rely = 0.015) 

        self.firstpage = LoginPage(self.interface, self)
        self.firstpage.place(relwidth = 0.85, relheight = 0.7, relx = 0.075, rely = 0.2)


    def ready_img(self, path, size): 

        return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))


    def show_frame(self, page_name):

        load = self.frames.get(page_name) 
        
        if page_name == "info_page": 
            load.place(relwidth = 1, relheight = 0.8,rely = 0.2)

        elif page_name == "login_page": 
            load.place(relwidth = 0.85, relheight = 0.7, relx = 0.075, rely = 0.2)







app = AppEngine()
app.mainloop()