from tkinter import *

class Main :
    def __init__(self) :
        self.root = Tk()
        self.num = 0
        self.number_display = Label(self.root, text = self.num)
        self.number_display.pack()
        self.button_frame = Frame(self.root)
        self.button_frame.pack()
        self.increment_button = Button(self.button_frame, text = "+", command = self.increment_num)
        self.increment_button.pack()
        self.decrement_button = Button(self.button_frame, text = "-", command = self.decrement_num)
        self.decrement_button.pack()
        self.reset_button = Button(self.button_frame, text = "Reset", command = self.reset_num)
        self.reset_button.pack()
        
    def increment_num(self) :
        self.num += 1
        self.number_display["text"] = self.num
        
    def decrement_num(self) :
        self.num -= 1
        self.number_display["text"] = self.num
        
    def reset_num(self) :
        self.num = 0
        self.number_display["text"] = self.num
        
    def run(self):
        self.root.mainloop()
    
app = Main()
app.run()