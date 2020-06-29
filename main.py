import tkinter as tk 
from PIL import ImageTk, Image

class AppEngine(tk.Tk): 

    def __init__(self): 

        super().__init__()
        self.title("MTE")
        self.geometry("1400x900")

        self.images = {
            "logo": self.ready_img("logo.png", (120, 130))
        }

        interface = tk.Canvas(self, bg = "#2ecc71")
        interface.place(relwidth = 1, relheight = 1)

        image = tk.Label(interface, image = self.images.get("logo"), bg = "#2ecc71", relief = "flat")
        image.place(relx = 0.009, rely = 0.015)

        status_bar = tk.Label(
            self, text = "MECHATRONICS", bg = "#2ecc71", 
            relief = "flat", 
            font = ("Skate Brand", 100),     
        )

        status_bar.place(relwidth = .8, relheight = .185, relx = .16, rely = .009)
    

    def ready_img(self, path, size): 

        return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))




app = AppEngine()
app.mainloop()