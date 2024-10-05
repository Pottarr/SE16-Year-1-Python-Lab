from tkinter import *

pastel_blue = "#abcdef"
pastel_green = "#aae5a4"
pastel_pink = "#fcd1eb"

class HomePage :
    def __init__(self, root) :
        self.root = root
        self.home_page_frame = Frame(self.root, bg = pastel_blue)
        self.home_page_frame.grid_columnconfigure(tuple(i for i in range(32)), weight = 1)
        self.home_page_frame.grid_rowconfigure(tuple(i for i in range(18)), weight = 1)
        self.home_page_frame.grid(row = 0, column = 0, sticky = "nsew")
        
        
        
        self.calendar_frame = Frame(self.home_page_frame, bg = "#ffffff")
        self.calendar_frame.grid_columnconfigure(0, weight = 1)
        self.calendar_frame.grid_rowconfigure(0, weight = 1)
        self.calendar_frame.grid(row = 1, column = 1, rowspan = 10, columnspan = 4, sticky = "nsew")
        
        self.calendar = Label(self.calendar_frame, text = "The calendar used in this project needs pip install TkCalendar to generate.")
        self.calendar.grid(row = 0, column = 0, sticky = "nsew")
        
        
        
        self.latest_action_log_frame = Frame(self.home_page_frame, bg = "#ffffff")
        self.latest_action_log_frame.grid_columnconfigure(0, weight = 1)
        self.latest_action_log_frame.grid_rowconfigure(0, weight = 1)
        self.latest_action_log_frame.grid(row = 12, column = 1, rowspan = 5, columnspan = 4, sticky = "nsew")
        
        self.latest_action_log_title = Label(self.latest_action_log_frame, text = "Latest Action")
        self.latest_action_log_title.grid(row = 0, column = 0, sticky = "nsew")
        
        
        
        self.create_activity_frame = Frame(self.home_page_frame, bg = pastel_pink)
        self.create_activity_frame.grid_columnconfigure(0, weight = 1)
        self.create_activity_frame.grid_rowconfigure((tuple(i for i in range(16))), weight = 1)
        self.create_activity_frame.grid(row = 1, column = 6, rowspan = 16, columnspan = 11, sticky = "nsew")
        
        self.create_activity_label = Label(self.create_activity_frame, text = "Create", bg = pastel_pink, font = 20)
        self.create_activity_label.grid(row = 0, column = 0, sticky = "nsew")
        
        
        
        self.activity_logs_frame = Frame(self.home_page_frame, bg = pastel_green)
        self.activity_logs_frame.columnconfigure(0, weight = 1)
        self.activity_logs_frame.rowconfigure(tuple((i for i in range(16))), weight = 1)
        self.activity_logs_frame.grid(row = 1, column = 18, rowspan= 16, columnspan = 13, sticky = "nsew")
        
        self.activity_logs_title = Label(self.activity_logs_frame, text = "Activity Log", bg = pastel_green,font = 20)
        self.activity_logs_title.grid(row = 0, column = 0, sticky = "nsew")
        
        self.normal_activity_logs_title = Label(self.activity_logs_frame, text = "Normal Activity Log", bg = pastel_green)
        self.normal_activity_logs_title.grid(row = 1, column = 0, sticky = "nsew")
        
        self.activity_logs_title = Label(self.activity_logs_frame, text = "Repeatable Activity Log", bg = pastel_green)
        self.activity_logs_title.grid(row = 9, column = 0, sticky = "nsew")
        