from tkinter import *
from pages.login_page import *
from pages.register_page import *

pastel_blue = "#abcdef"
pastel_green = "#aae5a4"

class Application :
    def __init__(self) :
        self.root = Tk()
        self.root.title("PyCalendar DEMO")
        self.root.geometry("1280x720")
        self.root.grid_columnconfigure(0, weight = 1)
        self.root.grid_rowconfigure(0, weight = 1)
        LoginPage(self.root)
        
    def run(self) :
        self.root.mainloop()
        
        


    
        
        
app = Application()
app.run()