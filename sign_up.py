from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import tkinter as tk 

class SignUP(tk.Toplevel): 

    def __init__(self, main_page):

        self.main_page = main_page

        self.bg = "#2E4053"
        self.fg = "#2ECC71"
        self.entry_fg = "#E53935"
        self.highlightbackground = "#3498DB"
        self.highlightcolor = "#f44336"

        self.image_locations = {
            "no_image" : self.load_image("//home//fayezblank//Coding//PythonWorks//GUI_Project_with_tkinter//image_base//none.png")
        }

        super().__init__()
        self.title("Create Account")
        self.geometry("800x900")

        

        self.interface = tk.Canvas(
            self, bg = self.bg, highlightbackground = self.bg
        )
        self.interface.bind("<Button-1>", lambda x: [self.interface.focus_set(), self.active()])
        self.interface.place(relwidth = 1, relheight = 1)



        self.toplabel = tk.Label(
            self.interface, text = "Create Your Account", font = ("my font", 30), 
            bg = self.bg, fg = "#3498DB"
        )
        self.toplabel.place(relwidth = 0.8, relheight = 0.08, relx = 0.1, rely = 0.03)



        self.id_label = tk.Label(
            self.interface, text = "ID", font = ("qualy", 20), 
            bg = self.bg, fg = self.fg

        )
        self.id_label.place(relwidth = 0.05, relheight = 0.05, relx = 0.05, rely = 0.13)

        self.id_entry = tk.Entry(
            self.interface, bd = 0, font = ("comfortaa", 20, "bold"),
            bg = self.bg, fg = self.entry_fg, highlightbackground = self.highlightbackground, highlightcolor = self.highlightcolor,
            relief = "flat"
        )
        self.id_entry.bind("<Button-1>", lambda var: [self.id_entry.focus_set(), self.active()])
        self.id_entry.place(relwidth = 0.9, relheight = 0.05, relx = 0.05, rely = .19)



        self.name_label = tk.Label(
            self.interface, text = "Name", font = ("qualy", 20), 
            bg = self.bg, fg = self.fg
        )
        self.name_label.place(relwidth = 0.1, relheight = 0.05, relx = 0.05, rely = 0.26)

        self.name_entry = tk.Entry(
            self.interface, bd = 0, font = ("comfortaa", 20, "bold"),
            bg = self.bg, fg = self.entry_fg, highlightbackground = self.highlightbackground, highlightcolor = self.highlightcolor,
            relief = "flat"
        )
        self.name_entry.bind("<Button-1>", lambda var: [self.name_entry.focus_set(), self.active()])
        self.name_entry.place(relwidth = 0.9, relheight = 0.05, relx = 0.05, rely = .32)



        self.email_label = tk.Label(
            self.interface, text = "Email", font = ("qualy", 20), 
            bg = self.bg, fg = self.fg
        )
        self.email_label.place(relwidth = 0.1, relheight = 0.05, relx = 0.05, rely = 0.39)

        self.email_entry = tk.Entry(
            self.interface, bd = 0, font = ("comfortaa", 20, "bold"), 
            bg = self.bg, fg = self.entry_fg, highlightbackground = self.highlightbackground, highlightcolor = self.highlightcolor,
        )
        self.email_entry.bind("<Button-1>", lambda var: [self.email_entry.focus_set(), self.active()])
        self.email_entry.place(relwidth = 0.9, relheight = 0.05, relx = 0.05, rely = .45)



        self.image_label = tk.Label(
            self.interface, text = "Add an image", font = ("qualy", 20), 
            bg = self.bg, fg = self.fg, 
            anchor = "w"
        )
        self.image_label.place(relwidth = 0.3, relheight = 0.05, relx = 0.05, rely = 0.52)

        self.img_path_entry = tk.Entry(
            self.interface, bd = 0, font = ("", 15), text = tk.StringVar(self.interface, "No Image Selected. Click to add Image."), 
            readonlybackground = self.bg,  fg = self.fg, highlightbackground = self.highlightbackground, highlightcolor = self.highlightcolor, 
            state = "readonly"
        )
        self.img_path_entry.bind("<Button-1>", lambda var: self.add_image())
        self.img_path_entry.place(relwidth = 0.9, relheight = 0.05, relx = 0.05, rely = 0.58)

        self.image_holder = tk.Label(
            self.interface, image = self.image_locations.get("no_image"), 
            bg = self.bg, relief = "flat", anchor = "w"
        )
        self.image_holder.place(relwidth = 0.5, relheight = 0.22, relx = 0.05, rely = 0.65)
    

    def active(self):

        self.active_color = "#1B4F72"

        #entry 1
        if str(self.focus_get()) == ".!signup.!canvas.!entry":
            self.id_label.configure(fg = "#f44336")
            self.id_entry.configure(bg = self.active_color, fg = self.entry_fg)
        
        else: 
            self.id_label.configure(fg = self.fg)
            self.id_entry.configure(bg = self.bg, fg = self.fg)

        #entry 2
        if str(self.focus_get()) == ".!signup.!canvas.!entry2":
            self.name_label.configure(fg = "#f44336")
            self.name_entry.configure(bg = self.active_color, fg = self.entry_fg)
        
        else: 
            self.name_label.configure(fg = self.fg)
            self.name_entry.configure(bg = self.bg, fg = self.fg)

        #entry 3
        if str(self.focus_get()) == ".!signup.!canvas.!entry3":
            self.email_label.configure(fg = "#f44336")
            self.email_entry.configure(bg = self.active_color, fg = self.entry_fg)
        
        else: 
            self.email_label.configure(fg = self.fg)
            self.email_entry.configure(bg = self.bg, fg = self.fg)
        
        

        print(self.focus_get())

    def load_image(self, path): 

        return ImageTk.PhotoImage(Image.open(path).resize((220, 200), Image.ANTIALIAS))
    
    def add_image(self):

        image_location = filedialog.askopenfile(
            initialdir = "//home//fayezblank//Downloads", title = "Add an Image", 
            filetypes = (("jpg files", "*.jpg"), ("png files", "*.png"))
        ).name.replace("/", "//")

        self.image_locations.update({
            "added_image" : self.load_image(image_location)
        })
        self.image_holder.configure(image = self.image_locations.get("added_image"))





        
interface = tk.Tk()

obj = SignUP("mainpage")


interface.mainloop()