from tkinter import messagebox, filedialog, simpledialog
from PIL import ImageTk, Image
from shutil import copyfile
from encryption import Encryption
import tkinter as tk 
import io

class SignUP(tk.Toplevel): 

    def __init__(self, main_page):

        self.main_page = main_page

        self.bg = "#2E4053"
        self.fg = "#2ECC71"
        self.entry_fg = "#E53935"
        self.highlightbackground = "#3498DB"
        self.highlightcolor = "#f44336"
        self.icons = self.main_page.connection.MechatronicsDB.Iconbase

        self.image_locations = {
            "no_image" : self.load_image("//home//fayezblank//Coding//PythonWorks//GUI_Project_with_tkinter//image_base//none.png"), 
            "hide" : ImageTk.PhotoImage(Image.open(io.BytesIO(self.icons.find_one({"_id" : "hide"}).get("image"))).resize((30, 30), Image.ANTIALIAS)), 
            "show" : ImageTk.PhotoImage(Image.open(io.BytesIO(self.icons.find_one({"_id" : "show"}).get("image"))).resize((30, 30), Image.ANTIALIAS))
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
        self.id_entry.bind("<Return>", lambda var: [self.name_entry.focus_set(), self.active()])
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
        self.name_entry.bind("<Return>", lambda var: [self.email_entry.focus_set(), self.active()])
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
        self.email_entry.bind("<Return>", lambda var: [self.img_path_entry.focus_set(), self.active()])
        self.email_entry.place(relwidth = 0.9, relheight = 0.05, relx = 0.05, rely = .45)



        self.image_label = tk.Label(
            self.interface, text = "Add an image", font = ("qualy", 20), 
            bg = self.bg, fg = self.fg, 
            anchor = "w"
        )
        self.image_label.place(relwidth = 0.3, relheight = 0.05, relx = 0.05, rely = 0.52)

        self.img_path_entry = tk.Entry(
            self.interface, bd = 0, font = ("", 15), text = tk.StringVar(self.interface, " No Image Selected. Click to add an Image."), justify = "center",
            readonlybackground = self.bg,  fg = self.fg, highlightbackground = self.highlightbackground, highlightcolor = self.highlightcolor, 
            state = "readonly"
        )
        self.img_path_entry.bind("<Button-1>", lambda var: [self.img_path_entry.focus_set(), self.active(), self.add_image()])
        self.img_path_entry.place(relwidth = 0.57, relheight = 0.05, relx = 0.05, rely = 0.61)

        self.image_holder = tk.Label(
            self.interface, image = self.image_locations.get("no_image"), 
            bg = self.bg, relief = "flat"
        )
        self.image_holder.place(relwidth = 0.35, relheight = 0.22, relx = 0.636, rely = 0.52)



        self.contact_label = tk.Label(
            self.interface, text = "Phone Number", font = ("qualy", 20), 
            bg = self.bg, fg = self.fg,
            relief = "flat", anchor = "w"
        )
        self.contact_label.place(relwidth = 0.3, relheight = 0.05, relx = 0.05, rely = 0.7)

        self.contact_entry = tk.Entry(
            self.interface, bd = 0, font = ("comfortaa", 20, "bold"), 
            bg = self.bg, fg = self.fg, highlightbackground = self.highlightbackground, highlightcolor = self.highlightcolor
        )
        self.contact_entry.bind("<Button-1>", lambda var: [self.contact_entry.focus_set(), self.active()])
        # self.contact_entry.bind("<Return>", lambda var: self.submit_button.focus_set())
        self.contact_entry.place(relwidth = 0.9, relheight = 0.05, relx = 0.05, rely = 0.76)



        self.submit_button = tk.Button(
            self.interface, bd = 2, text = "Submit", font = ("skate brand", 25), 
            bg = self.bg, fg = self.fg, activebackground = "#00FF96", activeforeground = self.bg, highlightbackground = "#FF5722",
            command = self.post_checking, relief = "flat",
        )
        self.submit_button.place(relwidth = 0.2, relheight = 0.05, relx = .4, rely = 0.88)
    

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
        
        #entry 4
        if str(self.focus_get()) == ".!signup.!canvas.!entry4":
            self.image_label.configure(fg = "#f44336")
            self.img_path_entry.configure(readonlybackground = self.active_color, fg = self.entry_fg)
        
        else: 
            self.image_label.configure(fg = self.fg)
            self.img_path_entry.configure(readonlybackground = self.bg, fg = self.fg)

        #entry 4
        if str(self.focus_get()) == ".!signup.!canvas.!entry5":
            self.contact_label.configure(fg = "#f44336")
            self.contact_entry.configure(readonlybackground = self.active_color, fg = self.entry_fg)
        
        else: 
            self.contact_label.configure(fg = self.fg)
            self.contact_entry.configure(readonlybackground = self.bg, fg = self.fg)



    def load_image(self, path): 

        return ImageTk.PhotoImage(Image.open(path).resize((220, 200), Image.ANTIALIAS))
    

    def add_image(self):

        try:

            image_location = filedialog.askopenfile(
                initialdir = "//home//fayezblank//Downloads", title = "Add an Image", 
                filetypes = (("jpg files", "*.jpg"), ("png files", "*.png"))
            ).name.replace("/", "//")

            self.image_locations.update({
                "added_image" : self.load_image(image_location), 
                "new_location" : "".join(("", "/home/fayezblank/Coding/PythonWorks/GUI_Project_with_tkinter/image_base/".replace("/", "//"), image_location.split("//")[-1]))
            })
            self.img_path_entry.configure(text = tk.StringVar(self.interface, image_location))
            self.image_holder.configure(image = self.image_locations.get("added_image"))

            copyfile(image_location, self.image_locations.get("new_location"))
        
        except:
            pass

    
    def hide_and_seek(self, identifier):

        if identifier == 1: 

            if self.password_entry.cget("show") == "*":

                self.password_entry.configure(show = "")
                self.hide_n_seek1.configure(image = self.image_locations.get("hide"))
            
            else : 

                self.password_entry.configure(show = "*")
                self.hide_n_seek1.configure(image = self.image_locations.get("show"))
        
        else: 

            if self.confirm_password_entry.cget("show") == "*":

                self.confirm_password_entry.configure(show = "")
                self.hide_n_seek2.configure(image = self.image_locations.get("hide"))
            
            else : 

                self.confirm_password_entry.configure(show = "*")
                self.hide_n_seek2.configure(image = self.image_locations.get("show"))
    



    def inner_check(self):
        
        if self.password_entry.get().rstrip() == self.confirm_password_entry.get().rstrip():
            
            self.cred_dict = {
                "user_name" : self.user_name_entry.get().rstrip(), 
                "password" : (self.checker.encrypt(self.password_entry.get().rstrip().encode())).decode()
            }

            if self.credentials.find_one({"user_name" : self.cred_dict.get("user_name").rstrip()}):
                messagebox.showerror("Error", "User Name Already Exists.\nTo try a Different Username Press SUBMIT again.")
                self.user_name_entry.delete(0, "end")
        
            else:

                self.user_pass_window.destroy()

                self.info_dict = {
                    "user_name" : self.cred_dict.get("user_name"), 
                    "info" : {
                        "name" : self.name_entry.get().rstrip(), 
                        "ID" : self.id_entry.get().rstrip(), 
                        "email" : self.email_entry.get().rstrip(), 
                        "image" : self.image_locations.get("new_location").rstrip()
                    }
                }

                self.credentials.insert_one(self.cred_dict)
                self.informations.insert_one(self.info_dict)

                messagebox.showinfo("Congratulations", "Account Created")
                self.destroy()

        else: 

            messagebox.showerror("Error", "Passwords don't match.")
            self.password_entry.delete(0, "end")
            self.confirm_password_entry.delete(0, "end")


    def post_checking(self):

        if len(self.id_entry.get().rstrip()) == 0 or len(self.name_entry.get().rstrip()) == 0 or len(self.email_entry.get().rstrip()) == 0 or (self.img_path_entry.get().rstrip())[1] == "N" or len(self.contact_entry.get()) == 0:

            messagebox.showwarning("Warning", "Every Field is Required.")
        
        else :

            try:

                if int(self.contact_entry.get().rstrip()) and len(self.contact_entry.get().rstrip()) >= 11: 

                    try: 

                        self.email_domains = [
                            "stud.kuet.ac.bd", 
                            "gmail.com", 
                            "outlook.com", 
                            "yahoo.com", 
                            "hotmail.com"
                        ]
                        
                        if (int(self.id_entry.get().rstrip()) and len(self.id_entry.get().rstrip()) == 9):

                            try: 

                                if self.email_entry.get().rstrip().split("@", 1)[1] in self.email_domains:

                                    self.informations = self.main_page.connection.MechatronicsDB.Informations

                                    try:

                                        if (self.informations.find_one({"info.ID" : self.id_entry.get().rstrip()})) or self.informations.find_one(({"info.email": self.email_entry.get().rstrip()})):
                                            
                                            messagebox.showerror("Error", "ID or Email already exists.")
                                    
                                        else:

                                            self.checker = Encryption()

                                            self.credentials = self.main_page.connection.MechatronicsDB.Credentials

                                            self.user_pass_window = tk.Toplevel(bg = self.bg)
                                            self.user_pass_window.title("Username and Password")
                                            self.user_pass_window.geometry("800x500")


                                            self.top_label = tk.Label(
                                                self.user_pass_window, text = "Choose Username & Password", font = ("my font", 30), 
                                                bg = self.bg, fg = "#3498DB", relief = "flat"
                                            )
                                            self.top_label.place(relwidth = 0.9, relheight = 0.1, relx = 0.05, rely = 0.03)



                                            self.user_name_label = tk.Label(
                                                self.user_pass_window, text = "Username", font = ("qualy", 20), 
                                                bg = self.bg, fg = self.fg, relief = "flat", anchor = "w"
                                            )
                                            self.user_name_label.place(relwidth = 0.3, relheight = 0.09, relx = 0.05, rely = 0.15)

                                            self.user_name_entry = tk.Entry(
                                                self.user_pass_window, font = ("confortaa", 20), 
                                                bg = self.bg, fg = self.fg, highlightbackground = self.highlightbackground, highlightcolor = self.highlightcolor, 
                                                relief = "flat"
                                            )
                                            self.user_name_entry.bind("<Return>", lambda var: self.password_entry.focus_set())
                                            self.user_name_entry.place(relwidth = 0.9, relheight = 0.09, relx = 0.05, rely = .25)


                                            self.password_label = tk.Label(
                                                self.user_pass_window, text = "Password", font = ("qualy", 20), 
                                                bg = self.bg, fg = self.fg, relief = "flat", anchor = "w"
                                            )
                                            self.password_label.place(relwidth = 0.2, relheight = 0.09, relx = 0.05, rely = 0.36)

                                            self.password_entry = tk.Entry(
                                                self.user_pass_window, font = ("comfortaa", 20), 
                                                bg = self.bg, fg = self.fg, highlightbackground = self.highlightbackground, highlightcolor = self.highlightcolor, 
                                                show = "*", relief = "flat"
                                            )
                                            self.password_entry.bind("<Return>", lambda var: self.confirm_password_entry.focus_set())
                                            self.password_entry.place(relwidth = 0.9, relheight = 0.09, relx = 0.05, rely = 0.46)

                                            self.hide_n_seek1 = tk.Button(
                                                self.user_pass_window, image = self.image_locations.get("show"), 
                                                bg = self.bg, highlightbackground = self.bg, highlightcolor = self.bg, activebackground = self.bg,
                                                command = lambda: self.hide_and_seek(1), relief = "flat"
                                            )
                                            self.hide_n_seek1.place(relwidth = 0.05, relheight = 0.075, relx = 0.895, rely = 0.468)



                                            self.confirm_password_label = tk.Label(
                                                self.user_pass_window, text = "Confirm Password", font = ("qualy", 20), 
                                                bg = self.bg, fg = self.fg, relief = "flat", anchor = "w"
                                            )
                                            self.confirm_password_label.place(relwidth = 0.35, relheight = 0.09, relx = 0.05, rely = 0.56)

                                            self.confirm_password_entry = tk.Entry(
                                                self.user_pass_window, font = ("comfortaa", 20), 
                                                bg = self.bg, fg = self.fg, highlightbackground = self.highlightbackground, highlightcolor = self.highlightcolor, 
                                                show = "*", relief = "flat"
                                            )
                                            self.confirm_password_entry.place(relwidth = 0.9, relheight = 0.09, relx = 0.05, rely = 0.66)


                                            self.hide_n_seek2 = tk.Button(
                                                self.user_pass_window, image = self.image_locations.get("show"), 
                                                bg = self.bg, highlightbackground = self.bg, highlightcolor = self.bg, activebackground = self.bg,
                                                command = lambda: self.hide_and_seek(2), relief = "flat"
                                            )
                                            self.hide_n_seek2.place(relwidth = 0.05, relheight = 0.075, relx = 0.895, rely = 0.668)


                                            self.done_button = tk.Button(
                                                self.user_pass_window, text = "Confirm", font = ("skate brand", 20), 
                                                bg = self.bg, fg = self.fg, activebackground = "#00FF96", activeforeground = self.bg, highlightbackground = "#FF5722",
                                                command = lambda : [self.inner_check()], relief = "flat"
                                            )                                     
                                            self.done_button.place(relwidth = 0.15, relheight = .1, relx = 0.84, rely = 0.825)    

                                    except ValueError:
                                        pass

                                else:

                                    raise IndexError

                            except IndexError:
                                messagebox.showerror("Error", "Email not acceptable.")  
                        
                        else:
                            raise ValueError

                    except ValueError: 
                        messagebox.showerror("Error", "ID is not acceptable.")
                
                else:
                    raise ValueError

            except ValueError:
                messagebox.showerror("Error", "Enter Valid Phone Number.")

        


# interface = tk.Tk()

# obj = SignUP("main_page")

# interface.mainloop()