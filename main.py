import tkinter as tk 
from PIL import ImageTk, Image
from login_page import LoginPage

class AppEngine(tk.Tk): 

    def __init__(self): 

        super().__init__()
        self.title("MTE")
        self.geometry("1400x900")

        self.images = {
            "logo": self.ready_img("logo.png", (120, 130))
        }

        interface = tk.Canvas(self, bg = "#00FF66")
        interface.place(relwidth = 1, relheight = 1)

        image = tk.Label(interface, image = self.images.get("logo"), bg = "#00FF66", relief = "flat")
        image.place(relx = 0.009, rely = 0.015)

        status_bar = tk.Label(
            interface, text = "MECHATRONICS", bg = "#00FF66", 
            relief = "flat", 
            anchor = "n",
            font = ("My Font", 100),     
        )

        status_bar.place(relwidth = .8, relheight = .185, relx = .16, rely = 0.015) 

        firstpage = LoginPage(interface, self)
        firstpage.place(relwidth = 0.8, relheight = 0.7, relx = 0.1, rely = 0.2)


    def ready_img(self, path, size): 

        return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))




app = AppEngine()
app.mainloop()