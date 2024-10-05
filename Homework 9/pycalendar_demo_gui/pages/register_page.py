from tkinter import *

pastel_blue = "#abcdef"
pastel_green = "#aae5a4"

class RegisterPage :
    def __init__(self, root) :
        self.root = root
        self.register_page_frame = Frame(self.root, bg = pastel_blue)
        self.register_page_frame.grid_columnconfigure(0, weight = 1)
        self.register_page_frame.grid_rowconfigure((0, 1, 2), weight = 1)
        self.register_page_frame.grid(row = 0, column = 0, sticky = "nsew")
        
        
        
        
        self.register_label = Label(self.register_page_frame, text = "Register", bg = pastel_blue)
        self.register_label.grid(row = 0, column = 0, sticky = "s")
        
        
        
        self.register_frame = Frame(self.register_page_frame, bg = pastel_blue)
        self.register_frame.grid_columnconfigure(0, weight = 1)
        self.register_frame.grid_columnconfigure((0, 1), weight = 1)
        self.register_frame.grid(row = 1, column = 0, sticky = "n")
        
        self.entry_frame = Frame(self.register_frame, bg = pastel_blue)
        self.entry_frame.grid_columnconfigure(0, weight = 2)
        self.entry_frame.grid_columnconfigure(1, weight = 3)
        self.entry_frame.grid_rowconfigure((0, 1, 2), weight = 1)
        self.entry_frame.grid(row = 0, column = 0, sticky = "s")
        
        self.username_entry_label = Label(self.entry_frame, text = "Username: ", bg = pastel_blue)
        self.username_entry_label.grid(row = 0, column = 0)
        
        self.password_entry_label = Label(self.entry_frame, text = "Password: ", bg = pastel_blue)
        self.password_entry_label.grid(row = 1, column = 0)
        
        self.confirm_password_entry_label = Label(self.entry_frame, text = "Password: ", bg = pastel_blue)
        self.confirm_password_entry_label.grid(row = 2, column = 0)
        
        self.username_entry = Entry(self.entry_frame)
        self.username_entry.grid(row = 0, column = 1)
        
        self.password_entry = Entry(self.entry_frame, show = "*")
        self.password_entry.grid(row = 1, column = 1)
        
        self.confirm_password_entry = Entry(self.entry_frame, show = "*")
        self.confirm_password_entry.grid(row = 2, column = 1)
        
        
        
        self.go_to_login_page_button = Button(self.register_page_frame, text = "Go to Login", command = self.go_to_login_page)
        self.go_to_login_page_button.grid(row = 2, column = 0, sticky = "n")
        
    def go_to_login_page(self) :
        from pages.login_page import LoginPage
        self.register_page_frame.destroy()
        LoginPage(self.root)