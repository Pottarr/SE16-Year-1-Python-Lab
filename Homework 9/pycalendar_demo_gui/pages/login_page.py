from tkinter import *

pastel_blue = "#abcdef"
pastel_green = "#aae5a4"

class LoginPage :
    def __init__(self, root) :
        self.root = root
        self.login_page_frame = Frame(self.root, bg = pastel_blue)
        self.login_page_frame.grid_columnconfigure(0, weight = 1)
        self.login_page_frame.grid_rowconfigure((0, 1, 2), weight = 1)
        self.login_page_frame.grid(row = 0, column = 0, sticky = "nsew")
        
        
        
        self.label_frame = Frame(self.login_page_frame, bg = pastel_blue)
        self.label_frame.grid_columnconfigure(0, weight = 1)
        self.label_frame.grid_rowconfigure((0, 1, 2, 3), weight = 1)
        self.label_frame.grid(row = 0, column = 0, sticky = "s")
        
        self.title_label = Label(self.label_frame, text = "PyCalendar", font = 40, bg = pastel_blue)
        self.title_label.grid(row = 0, column = 0)
        
        self.login_label = Label(self.label_frame, text = "Login", bg = pastel_blue)
        self.login_label.grid(row = 1, column = 0)




        self.login_frame = Frame(self.login_page_frame, bg = pastel_blue)
        self.login_frame.grid_columnconfigure(0, weight = 1)
        self.login_frame.grid_rowconfigure((0, 1), weight = 1)
        self.login_frame.grid(row = 1, column = 0, sticky = "n")

        self.entry_frame = Frame(self.login_frame, bg = pastel_blue)
        self.entry_frame.grid_columnconfigure(0, weight = 1)
        self.entry_frame.grid_columnconfigure(1, weight = 2)
        self.entry_frame.grid_rowconfigure((0, 1), weight = 1)
        self.entry_frame.grid(row = 1, column = 0, sticky = "s")
        
        self.username_entry_label = Label(self.entry_frame, text = "Username: ", bg = pastel_blue)
        self.username_entry_label.grid(row = 0, column = 0)
        
        self.password_entry_label = Label(self.entry_frame, text = "Password: ", bg = pastel_blue)
        self.password_entry_label.grid(row = 1, column = 0)
        
        self.username_entry = Entry(self.entry_frame)
        self.username_entry.grid(row = 0, column = 1)
        
        self.password_entry = Entry(self.entry_frame, show = "*")
        self.password_entry.grid(row = 1, column = 1)
        
        
        
        self.button_hint_frame = Frame(self.login_frame, bg = pastel_blue)
        self.button_hint_frame.columnconfigure(0, weight = 1)
        self.button_hint_frame.rowconfigure((0, 1), weight = 1)
        self.button_hint_frame.grid(row = 2, column = 0, sticky = "n")
        
        self.login_button = Button(self.button_hint_frame, text = "Login", command = self.login)
        self.login_button.grid(row = 2, column = 0, pady = 10)
        
        self.hint = Label(self.button_hint_frame, text = "FOR DEMO: USERNAME = admin PASSWORD = 123", fg = "red", bg = pastel_blue)
        self.hint.grid(row = 3, column = 0)
        
        
        
        self.go_to_register_page_button = Button(self.login_page_frame, text = "Go to Register", command = self.go_to_register_page)
        self.go_to_register_page_button.grid(row = 2, column = 0, sticky = "n")
        
    def login(self) :
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "123" :
            from pages.home_page import HomePage
            self.login_page_frame.destroy()
            HomePage(self.root)
            
    def go_to_register_page(self) :
        from pages.register_page import RegisterPage
        self.login_page_frame.destroy()
        RegisterPage(self.root)