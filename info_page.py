import tkinter as tk 

class InfoPage(tk.Frame): 

    def __init__(self, parent, main_page): 

        #for recreating after destrying the object
        self.main_page = main_page
        self.parent = parent

        super().__init__(parent, bg = "#58d68d", highlightbackground = "#f44336", highlightthickness = "2", relief = "flat")

        self.button1 = tk.Button(self, text = "front_page", command = lambda: self.load_page("login_page"))
        self.button1.pack()

    

    def load_page(self, page_name): 

        self.destroy()
        self.__init__(self.parent, self.main_page)

        self.main_page.show_frame(page_name)